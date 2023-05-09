from typing import Dict, Union
from abc import abstractmethod


class BaseDataTransferObject:
    @abstractmethod
    def GetAllDataByDict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def CreateObject(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def SerializeData(data_dict: Dict[str, Union[str, bool]]):
        pass
