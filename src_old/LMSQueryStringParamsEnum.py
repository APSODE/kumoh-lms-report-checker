from enum import Enum
from typing import Optional


class LMSQueryStringParamsEnum(Enum):
    REPORT = ("viewReportInfoPageList", None, "report", None, None, "menu_00104", "menu_00063")
    LECTURE = ("viewStudyHome", None, "study_home", "study_course", "study_course", None, None)

    def __init__(self,
                 href_js_cmd: Optional[str] = None,
                 lecture_code: Optional[str] = None,
                 board_info_gubun: Optional[str] = None,
                 board_gubun: Optional[str] = None,
                 gubun: Optional[str] = None,
                 p_menuid: Optional[str] = None,
                 menuid: Optional[str] = None,
                 ):

        self.href_js_cmd = href_js_cmd
        self.lecture_code = lecture_code
        self.board_info_gubun = board_info_gubun
        self.board_gubun = board_gubun
        self.gubun = gubun
        self.p_menuid = p_menuid
        self.menuid = menuid
