from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from src.DataTransferObject.ReportData import ReportData
from src.Database.DatabaseCreator import DatabaseCreator
from src.Database.Model.BaseModel import BaseModel


class ReportModel(DatabaseCreator.Model, BaseModel):
    __tablename__ = "report"
    id = Column(Integer, primary_key = True)
    # subject = Column(Integer, ForeignKey("subject.id"))
    title = Column(String, nullable = False)
    description = Column(String(20), nullable = False)
    deadline = Column(String, nullable = False)
    submission_status = Column(Boolean, default = False)
    allow_ext_submission = Column(Boolean, default = False)

    def __init__(self, report_data_object: ReportData):
        self.title = report_data_object.ReportTitle
        self.description = report_data_object.ReportDescription
        self.deadline = report_data_object.SubmissionDeadline
        self.submission_status = report_data_object.SubmissionStatus
        self.allow_ext_submission = report_data_object.AllowExtendedSubmission

    def GetAllDataByDict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}

