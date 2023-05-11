from sqlalchemy import Column, Integer, String
from src.DataTransferObject.SubjectData import SubjectData
from src.Database.DatabaseCreator import DatabaseCreator
from src.Database.Model.BaseModel import BaseModel


class SubjectModel(DatabaseCreator.Model, BaseModel):
    __tablename__ = "subject"
    id = Column(Integer, primary_key = True)
    subject_name = Column(String, nullable = False)
    subject_code = Column(String, nullable = False)
    div_class = Column(String, nullable = False)

    def __init__(self, subject_data_object: SubjectData):
        self.subject_name = subject_data_object.SubjectName
        self.subject_code = subject_data_object.SubjcetCode
        self.div_class = subject_data_object.DivisionClass

    def GetAllDataByDict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}
