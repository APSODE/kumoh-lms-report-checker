import json
from typing import Optional, List
from requests import Session, Response
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime as dt
from src.CustomException.LMSControllerException import LoginFailException, MainPageLoadError
from src.DataTransferObject.UserAccountData import UserAccountData
from src.DataTransferObject.ReportData import ReportData
from src.DataTransferObject.SubjectData import SubjectData


class LMSController:
    def __init__(self, user_account_data: UserAccountData):
        self._lms_main_url = "https://elearning.kumoh.ac.kr/"
        self._login_lms_url = "https://elearning.kumoh.ac.kr/User.do"
        self._semester = self._get_semester()
        self._user_account_data = user_account_data
        self._session = self._create_session()
        self._login_lms()

    @staticmethod
    def _replace_element_text(element: Tag) -> str:
        return element.text.replace(
            "\n", ""
        ).replace(
            "\t", ""
        ).replace(
            "\r", ""
        ).replace(
            "\xa0", " "
        )

    @staticmethod
    def _get_site_html(site_response: Response) -> Optional[BeautifulSoup]:
        if site_response.ok:
            return BeautifulSoup(
                site_response.text,
                "html.parser"
            )
        else:
            raise MainPageLoadError()

    @staticmethod
    def _get_semester() -> int:
        current_month = dt.now().month
        if 3 <= current_month <= 6:
            return 1
        elif 9 <= current_month <= 12:
            return 2
        else:
            return 0

    def _create_session(self):
        s = Session()
        s.get(self._lms_main_url)
        return s

    def _login_lms(self):
        login_response = self._session.post(
            url = self._login_lms_url,
            data = {
                "cmd": "loginUser",
                "userId": self._user_account_data.UserID,
                "password": self._user_account_data.UserPW
            }
        )
        if not login_response.ok:
            raise LoginFailException()

    def _create_report_url(self, division_class: str, subject_code: str):
        report_base_url = "https://elearning.kumoh.ac.kr/Report.do?"
        return report_base_url.join(
            [
                "",  # .join()메소드의 인자로 전달하는 iterable객체의 첫번째 값은 참조하는 값의 맨앞으로 들어가므로 이와 같이 작성해야함
                f"cmd=viewReportInfoPageList&",
                f"boardInfoDTO.boardInfoGubun=report&"
                f"courseDTO.courseId={dt.now().year}{self._semester}{subject_code}{division_class}&"
                f"mainDTO.parentMenuId=menu_00104&",
                f"mainDTO.menuId=menu_00063",
            ]
        )

    def GetSubjectDatas(self) -> List[Optional[SubjectData]]:
        subject_data_list = []
        lms_main_html = self._get_site_html(
            site_response = self._session.get(self._lms_main_url + "Main.do?cmd=viewHome&userDTO.localeKey=ko")
        )

        lms_subject_list_html = lms_main_html.find_all(
            "div", {"class": "sixteen wide tablet eight wide computer column"}
        )[1].find_next(
            "div", {"class": "main-box"}
        ).find_all(
            "div"
        )[1].find_next(
            "ul", {"class": "my-class"}
        ).find_all(
            "li"
        )

        for subject_element in lms_subject_list_html:
            subject_element_text = subject_element.find_next("span").text.replace("/ ", "")
            subject_data = subject_element_text.split()
            current_subject_name = subject_data[0]
            current_subject_division_class = subject_data[1]
            current_subject_code = subject_data[2]

            subject_data_list.append(
                SubjectData.CreateObject(
                    subject_name = current_subject_name,
                    subject_code = current_subject_code,
                    division_class = current_subject_division_class
                )
            )

        return subject_data_list

    def GetReportDatas(self, subject_data: SubjectData) -> List[Optional[ReportData]]:
        report_data_list = []

        subject_report_list_url = self._create_report_url(
            division_class = subject_data.DivisionClass,
            subject_code = subject_data.SubjcetCode
        )

        report_list_page_html = self._get_site_html(
            site_response = self._session.get(subject_report_list_url)
        )

        report_list_html = report_list_page_html.find(
            "div", {"id": "listBox"}
        ).find_all_next(
            "div", {"class": "listContent pb20"}
        )

        for report_html in report_list_html:
            # #listBox > div:nth-child(2) > dl > dd:nth-child(3) > table > tbody > tr
            report_data_html = report_html.find_next(
                "dl", {"class": "element"}
            )

            report_title_element = report_data_html.find_next(
                "dt"
            ).find_next(
                "h4", {"class": "f14"}
            )

            report_data_element_list = report_data_html.find_all_next(
                "dd"
            )[1].find_next(
                "table", {"class", "boardListInfo"}
            ).find_next(
                "tbody"
            ).find_next(
                "tr"
            ).find_all_next(
                "td"
            )

            report_description_element = report_data_html.find_all_next(
                "dd"
            )[1].find_next(
                "div", {"class": "cont pb0"}
            )

            report_title = self._replace_element_text(
                element = report_title_element
            )

            report_deadline = self._replace_element_text(
                element = report_data_element_list[0]
            )

            report_extend_submission = self._replace_element_text(
                element = report_data_element_list[3]
            )

            report_submission_status = self._replace_element_text(
                element = report_data_element_list[4]
            )

            report_description = self._replace_element_text(
                element = report_description_element
            )

            report_data_list.append(
                ReportData.CreateObject(
                    submission_deadline = report_deadline,
                    submission_status = report_submission_status,
                    allow_extended_submission = report_extend_submission,
                    report_title = report_title,
                    report_description = report_description
                )
            )

        return report_data_list

    # def UpdateReportDatas(self):

