from sqlalchemy import Column, Integer, String, Boolean
from src.DataTransferObject.ReportData import ReportData
from src.Database.DatabaseCreator import DatabaseCreator


class ReportModel(DatabaseCreator.Model):
    __tablename__ = "report"
    id = Column(Integer, primary_key = True)
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


