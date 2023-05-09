from typing import Dict, Union
from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject


class ReportData(BaseDataTransferObject):
    def __init__(self, deadline: str, allow_extend: bool, status: bool, title: str, description: str):
        self._deadline = deadline
        self._allow_extend = allow_extend
        self._status = status
        self._title = title
        self._description = description

    @property
    def SubmissionDeadline(self) -> str:
        return self._deadline

    @property
    def AllowExtendedSubmission(self) -> bool:
        return self._allow_extend

    @property
    def SubmissionStatus(self) -> bool:
        return self._status

    @property
    def ReportTitle(self) -> str:
        return self._title

    @property
    def ReportDescription(self) -> str:
        return self._description

    def GetAllDataByDict(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateObject(
            submission_deadline: str,
            allow_extended_submission: str,
            submission_status: str,
            report_title: str,
            report_description: str) -> "ReportData":

        return ReportData(
            deadline = submission_deadline,
            allow_extend = True if allow_extended_submission == "허용" else False,
            status = True if submission_status == "제출" else False,
            title = report_title,
            description = report_description
        )

    @staticmethod
    def SerializeData(data_dict: Dict[str, Union[str, bool]]) -> "ReportData":
        return ReportData(
            deadline = data_dict.get("deadline"),
            allow_extend = data_dict.get("allow_extend"),
            status = data_dict.get("status"),
            title = data_dict.get("title"),
            description = data_dict.get("description")
        )
