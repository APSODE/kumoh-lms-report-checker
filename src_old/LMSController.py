import os
from typing import Optional, Union, Dict, List

import bs4.element
from bs4 import BeautifulSoup
from datetime import datetime as dt

from src_old.ReportData import ReportData
from src_old.StatusChecker import StatusChecker
from src_old.LMSQueryStringParamsEnum import LMSQueryStringParamsEnum
from src_old.JsonReadWriteTools import JsonReadWrite
from src_old.LectureData import LectureData
import requests
import json
import time


class LMSController:
    def __init__(self, current_year: str = str(dt.now().year), semester: str = "1"):
        self._lms_url = "https://elearning.kumoh.ac.kr/"
        self._lms_login_url = "https://elearning.kumoh.ac.kr/User.do"
        self._cookie = "caaZXPrIHYEGDaI4fmoCy3sef0ymHjXfeMbsYvjqNm_CBLxXNqPoR-C2OYvn"
        self._lecture_data_file_dir = "lecture_data.json" if __name__ == "__main__" else ".\\src_old\\lecture_data.json"
        self._report_data_file_dir = "report_data.json" if __name__ == "__main__" else ".\\src_old\\report_data.json"
        self._session = requests.Session()
        self._y_semester = current_year + semester

    def _get_site_html(self,
                       url_or_response: Union[Optional[str], Optional[requests.Response]] = None
                       ) -> Optional[BeautifulSoup]:
        site_response = self._session.get(url_or_response) if type(url_or_response) is str else url_or_response

        if StatusChecker.isCorrect(response = site_response):
            return BeautifulSoup(site_response.text, "html.parser")

    def _login_lms(self) -> Optional[requests.Response]:
        self._session.get(self._lms_url)
        login_result_response = self._session.post(
            url = self._lms_login_url,
            data = self._create_login_payload(),
            verify = False
        )
        if StatusChecker.isCorrect(response = login_result_response):
            return login_result_response

    @staticmethod
    def _create_login_payload() -> Dict[str, str]:
        return {
            "cmd": "loginUser",
            "userId": os.environ.get("lms_id"),
            "password": os.environ.get("lms_pw")
        }

    def _set_login_cookie(self) -> None:
        self._session.get(self._lms_url)
        self._session.cookies.update(
            other = {
                "RSN_JSESSIONID": self._cookie
            }
        )

    def _get_lecture_url_qsp(self, query_target_file: str,  qs_params: Dict[str, str]) -> str:
        result_qsp_url = self._lms_url + query_target_file + "?"

        if qs_params.get("cmd") is not None:
            result_qsp_url += f"cmd={qs_params.get('cmd')}&"

        if qs_params.get("courseDTO.courseId") is not None:
            result_qsp_url += f"courseDTO.courseId={qs_params.get('courseDTO.courseId')}&"

        if qs_params.get("boardInfoDTO.boardInfoGubun") is not None:
            result_qsp_url += f"boardInfoDTO.boardInfoGubun={qs_params.get('boardInfoDTO.boardInfoGubun')}&"

        if qs_params.get("boardGubun") is not None:
            result_qsp_url += f"boardGubun={qs_params.get('boardGubun')}&"

        if qs_params.get("gubun") is not None:
            result_qsp_url += f"gubun={qs_params.get('gubun')}"

        if qs_params.get("mainDTO.parentMenuId") is not None:
            result_qsp_url += f"mainDTO.parentMenuId={qs_params.get('mainDTO.parentMenuId')}"

        if qs_params.get("mainDTO.menuId") is not None:
            result_qsp_url += f"mainDTO.menuId={qs_params.get('mainDTO.menuId')}"

        return result_qsp_url

    def _create_qs_params(self,
                          lecture_code: Optional[str] = None,
                          href_js_cmd: Optional[str] = None,
                          board_info_gubun: Optional[str] = None,
                          board_gubun: Optional[str] = None,
                          gubun: Optional[str] = None,
                          p_menuid: Optional[str] = None,
                          menuid: Optional[str] = None) -> Dict[str, str]:
        return {
            "cmd": href_js_cmd,
            "courseDTO.courseId": (self._y_semester + lecture_code) if lecture_code is not None else None,
            "boardInfoDTO.boardInfoGubun": board_info_gubun,
            "boardGubun": board_gubun,
            "gubun": gubun,
            "mainDTO.parentMenuId": p_menuid,
            "mainDTO.menuId": menuid
        }

    def _create_qs_params_enum(self,
                               lecture_code: str,
                               default_params_enum: LMSQueryStringParamsEnum) -> Dict[str, str]:
        return {
            "cmd": default_params_enum.href_js_cmd,
            "courseDTO.courseId": self._y_semester + lecture_code,
            "boardInfoDTO.boardInfoGubun": default_params_enum.board_info_gubun,
            "boardGubun": default_params_enum.board_gubun,
            "gubun": default_params_enum.gubun,
            "mainDTO.parentMenuId": default_params_enum.p_menuid,
            "mainDTO.menuId": default_params_enum.menuid
        }

    def _create_lecture_url_list(self, page_type: Optional[str] = "c"):
        lecture_code_data = JsonReadWrite.ReadJson(
            json_file_dir = self._lecture_data_file_dir
        )
        for lecture_name, lecture_code in lecture_code_data.items():
            qsp_url = self._get_lecture_url_qsp(
                query_target_file = "Report.do" if page_type == "r" else "Course.do",
                qs_params = self._create_qs_params_enum(
                    lecture_code = lecture_code,
                    default_params_enum = LMSQueryStringParamsEnum.REPORT
                )
            )
            lecture_code_data[lecture_name]["url"] = qsp_url

        # with open(data_file_dir, "w")

    def _update_lecture_data(self):
        lms_main_html = self._get_site_html(url_or_response = self._login_lms())
        lms_lecture_list_html = lms_main_html.find("ul", {"class": "my-class"})

        lecture_data = {}
        for element in lms_lecture_list_html.find_all("a"):
            edited_element_text = element.text.replace(" ", "").replace("\n", "")
            lecture_name = edited_element_text.split("/")[0]
            lecture_code = edited_element_text.split("/")[2] + edited_element_text.split("/")[1]
            lecture_data[lecture_name] = {}
            lecture_data[lecture_name]["url"] = {}
            lecture_data[lecture_name]["code"] = lecture_code
            
            for page_type in ["c", "r"]:
                qsp_url = self._get_lecture_url_qsp(
                    query_target_file = "Report.do" if page_type == "r" else "Course.do",
                    qs_params = self._create_qs_params_enum(
                        lecture_code = lecture_code,
                        default_params_enum = LMSQueryStringParamsEnum.REPORT
                    )
                )

                lecture_data[lecture_name]["url"][page_type] = qsp_url

        with open(self._lecture_data_file_dir, "w", encoding = "utf-8") as write_file:
            json.dump(
                lecture_data,
                write_file,
                indent = 4,
                ensure_ascii = False
            )

    def _update_report_data(self):
        total_report_data = {}
        for lecture_name in self._get_lecture_name_list():
            lecture_data = LectureData.CreateDataObject(lecture_name = lecture_name)
            lecture_report_page_html = self._get_site_html(
                url_or_response = lecture_data.ReportUrl
            )
            total_report_data[lecture_name] = {}
            for number, report_element in enumerate(lecture_report_page_html.find_all(
                    "div", {"class": "listContent pb20"})):

                report_title = report_element.find_next(
                    "dl", {"class": "element"}
                ).find_next(
                    "dt"
                ).find_next(
                    "h4", {"class": "f14"}
                )
                report_title = self._replace_element_text(element = report_title)
                report_period_element = report_element.find_next(
                    "dl", {"class": "element"}
                ).select_one(
                    "dd:nth-child(3)"
                ).find_next(
                    "table", {"class": "boardListInfo"}
                ).find_next(
                    "tbody"
                ).find_next(
                    "tr"
                )
                report_data = ReportData.CreateDataObject(
                    report_name = report_title,
                    period_element = report_period_element
                )
                total_report_data[lecture_name][str(number + 1)] = report_data.GetDataByDict()
        with open(self._report_data_file_dir, "w", encoding = "utf-8") as write_file:
            json.dump(
                total_report_data,
                write_file,
                indent = 4,
                ensure_ascii = False
            )

    def _get_lecture_name_list(self) -> List[str]:
        return [lecture_name for lecture_name in JsonReadWrite.ReadJson(json_file_dir = self._lecture_data_file_dir)]

    @staticmethod
    def _replace_element_text(element: bs4.element.Tag) -> str:
        return element.text.replace(
            "\n", ""
        ).replace(
            "\t", ""
        ).replace(
            "\r", ""
        )

    def ReportSubmissionCheck(self):
        report_data = JsonReadWrite.ReadJson(
            json_file_dir = self._report_data_file_dir
        )

        for lecture_name in report_data:
            if len([key for key in report_data.get(lecture_name)]) > 0:
                for each_report_data in \
                        [report_data.get(lecture_name).get(key) for key in report_data.get(lecture_name)]:
                    report_data_object = ReportData.CreateDataObject(
                        report_data = each_report_data
                    )
                    if report_data_object.SubmissionStatus == "미제출":
                        print(report_data_object)

    def Run(self) -> None:
        if self._login_lms().ok:
            ft = time.perf_counter()
            self._update_lecture_data()
            self._update_report_data()
            self.ReportSubmissionCheck()
            st = time.perf_counter()
            print(f"running time : {round(st - ft, 2)}")
        else:
            raise ConnectionError("lms에 로그인하는 도중 에러가 발생하였습니다.\n"
                                  "lms서버에 보낸 로그인 request의 response가 200이 아닙니다.")

        self._session.close()


if __name__ == '__main__':
    LC = LMSController()
    LC.Run()
