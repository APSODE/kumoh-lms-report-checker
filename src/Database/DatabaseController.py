from typing import Type
from src.Database.DatabaseCreator import DatabaseCreator


class DatabaseController:
    def __init__(self, model_object: Type[DatabaseCreator]):
        self._model_object = model_object

    @property
    def ModelObject(self) -> Type[DatabaseCreator]:
        return self._model_object

