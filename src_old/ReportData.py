from typing import Optional, Dict

import bs4.element


class ReportData:
    def __init__(self,
                 period: str,
                 submission_status: str,
                 submission_of_extension: str,
                 report_name: str):
        self._period = period
        self._submission_status = submission_status
        self._submission_of_extension = submission_of_extension
        self._report_name = report_name

    @property
    def Period(self) -> str:
        return self._period

    @property
    def ReportName(self) -> str:
        return self._report_name

    @property
    def SubmissionStatus(self) -> str:
        return self._submission_status

    @property
    def SubmissionOfExtension(self) -> str:
        return self._submission_of_extension

    def GetDataByDict(self):
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    def __repr__(self) -> str:
        return f"\n====== report data ======\n" \
               f"report name : {self._report_name}\n" \
               f"report period : {self._period}\n" \
               f"submisson status : {self._submission_status}\n" \
               f"submission of extension : {self._submission_of_extension}\n"

    @staticmethod
    def _replace_element_text(element: bs4.element.Tag) -> str:
        return element.text.replace(
            "\n", ""
        ).replace(
            "\t", ""
        ).replace(
            "\r", ""
        )

    @staticmethod
    def CreateDataObject(report_name: Optional[str] = None,
                         period_element: Optional[bs4.element.Tag] = None,
                         report_data: Optional[Dict[str, str]] = None):

        if period_element is not None and report_name is not None:
            return ReportData(
                period = ReportData._replace_element_text(period_element.select_one('td:nth-child(1)')),
                submission_status = ReportData._replace_element_text(period_element.select_one('td:nth-child(5)')),
                submission_of_extension = ReportData._replace_element_text(period_element.select_one('td:nth-child(4)')),
                report_name = report_name
            )
        # #listBox > div:nth-child(1) > dl > dd:nth-child(3) > table > tbody > tr > td.last
        if report_data is not None:
            return ReportData(
                period = report_data.get("period"),
                submission_status = report_data.get("submission_status"),
                submission_of_extension = report_data.get("submission_of_extension"),
                report_name = report_data.get("report_name")
            )
