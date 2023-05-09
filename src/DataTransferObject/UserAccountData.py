from typing import Dict, Union

from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject


class UserAccountData(BaseDataTransferObject):
    def __init__(self, id: str, pw: str):
        self._id = id
        self._pw = pw

    @property
    def UserID(self) -> str:
        return self._id

    @property
    def UserPW(self) -> str:
        return self._pw

    def GetAllDataByDict(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateObject(user_id: str, user_pw: str) -> "UserAccountData":
        return UserAccountData(
            id = user_id,
            pw = user_pw
        )

    @staticmethod
    def SerializeData(data_dict: Dict[str, Union[str, bool]]) -> "UserAccountData":
        return UserAccountData(
            id = data_dict.get("id"),
            pw = data_dict.get("pw")
        )
