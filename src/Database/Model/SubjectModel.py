from sqlalchemy import Column, Integer, String
from src.DataTransferObject.SubjectData import SubjectData
from src.Database.DatabaseCreator import DatabaseCreator


class SubjectModel(DatabaseCreator.Model):
    __tablename__ = "subject"
    id = Column(Integer, primary_key = True)
    subject_name = Column(String, nullable = False)
    subject_code = Column(String, nullable = False)
    div_class = Column(String, nullable = False)

    def __init__(self, subject_data_object: SubjectData):
        self.subject_name = subject_data_object.SubjectName
        self.subject_code = subject_data_object.SubjcetCode
        self.div_class = subject_data_object.DivisionClass

