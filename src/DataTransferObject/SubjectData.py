from typing import Dict, Union

from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject


class SubjectData(BaseDataTransferObject):
    def __init__(self, sub_name: str, sub_code: str, div_class: str):
        self._name = sub_name
        self._sub_code = sub_code
        self._div_class = div_class

    @property
    def SubjectName(self) -> str:
        return self._name

    @property
    def SubjcetCode(self) -> str:
        return self._sub_code

    @property
    def DivisionClass(self) -> str:
        return self._div_class

    def GetAllDataByDict(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateObject(subject_name: str, subject_code: str, division_class: str) -> "SubjectData":
        return SubjectData(
            sub_name = subject_name,
            sub_code = subject_code,
            div_class = division_class
        )

    @staticmethod
    def SerializeData(data_dict: Dict[str, Union[str, bool]]) -> "SubjectData":
        return SubjectData(
            sub_name = data_dict.get("name"),
            sub_code = data_dict.get("sub_code"),
            div_class = data_dict.get("div_class")
        )
