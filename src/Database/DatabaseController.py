from typing import Type, Union, List, TypeVar
from src.Database.DatabaseCreator import DatabaseCreator
from src.Database.Model.ReportModel import ReportModel
from src.Database.Model.SubjectModel import SubjectModel

DataModel = TypeVar("DataModel")


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

    def GetData(self,
                model_class: Type[DataModel],
                filter_data: Optional[bool] = None,
                data_amount: int = 0) -> List[DataModel]:

        filtered_data = self._database_creator.Session.query(
            model_class
        )

        if filter_data is not None:
            filtered_data = filtered_data.filter(
                filter_data
            )

        filtered_data: Query

        if data_amount == 0:
            return filtered_data.all()

        else:
            return filtered_data.limit(data_amount).all()

    def UpdateData(self, model_class: Union[Type[SubjectModel], Type[ReportModel]], filter_data: bool, update_data: dict):
        self._database_creator.Session.query(
            model_class
        ).filter(
            filter_data
        ).update(
            update_data
        )

    def is_already_exist(self, model_class: Union[Type[SubjectModel], Type[ReportModel]], filter_data: bool) -> bool:
        filtered_data = self._database_creator.Session.query(
            model_class
        ).filter(
            filter_data
        ).first()

        if filtered_data:
            return True

        else:
            return False
