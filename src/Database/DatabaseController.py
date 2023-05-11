from typing import Type, Union, List, TypeVar
from src.Database.DatabaseCreator import DatabaseCreator
from src.Database.Model.ReportModel import ReportModel
from src.Database.Model.SubjectModel import SubjectModel
from sqlalchemy import ClauseElement


class DatabaseController:
    def __init__(self, db_creator: DatabaseCreator):
        self._database_creator = db_creator

    @property
    def DB_Creator(self):
        return self._database_creator

    def AddData(self, model_object: Union[SubjectModel, ReportModel]):
        self._database_creator.Session.add(model_object)

    def CommitData(self):
        self._database_creator.Session.commit()

    def UpdateData(self, model_class: Type[DatabaseCreator.Model], filter_data: bool, update_data: dict):
        self._database_creator.Session.query(
            model_class
        ).filter(
            filter_data
        ).update(
            update_data
        )

