from typing import Optional, Dict, Any, List
from src.Bot.utils.JsonReadWrite import JsonReadWrite
from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject
from src.CustomException.DTOException import *


class ConfigData(BaseDataTransferObject):
    def __init__(self,
                 notice_time_datas: List[Dict[str, int]],
                 update_check_term: int,
                 token: str,
                 bot_id: int
                 ):
        self._notice_time_datas = notice_time_datas
        self._update_check_term = update_check_term
        self._token = token
        self._bot_id = bot_id

    @property
    def NoticeTime(self) -> Optional[List[Dict[str, int]]]:
        return self._notice_time_datas

    @NoticeTime.setter
    def NoticeTime(self, new_time_datas: List[Dict[str, int]]):
        for new_time_data in new_time_datas:
            if new_time_data.get("hour") is None or new_time_data.get("minute") is None:
                raise ConfigDataSetterNotExistError()

        self._notice_time_datas = new_time_datas

    @property
    def UpdateCheckTerm(self) -> Optional[int]:
        return self._update_check_term

    @UpdateCheckTerm.setter
    def UpdateCheckTerm(self, new_check_term: int):
        if not new_check_term >= 0:
            raise ConfigDataInvalidSetterDataError()

        self._update_check_term = new_check_term

    @property
    def Token(self) -> Optional[str]:
        return self._token

    @property
    def ID(self) -> Optional[int]:
        return self._bot_id

    def GetAllDataByDict(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateObject(
                     notice_time_datas: List[Dict[str, int]],
                     update_check_term: int,
                     token: str,
                     bot_id: int
                     ):

        return ConfigData(
            notice_time_datas = notice_time_datas,
            update_check_term = update_check_term,
            token = token,
            bot_id = bot_id
        )

    @staticmethod
    def CreateObjectByDir(config_file_dir: str) -> "ConfigData":
        read_config_file_data = JsonReadWrite.ReadJson(config_file_dir)

        return ConfigData(
            notice_time_datas = read_config_file_data.get("notice_time_datas"),
            update_check_term = read_config_file_data.get("update_check_term"),
            token = read_config_file_data.get("token"),
            bot_id = read_config_file_data.get("bot_id")
        )

    @staticmethod
    def SerializeData(data_dict: Dict[str, Any]) -> "ConfigData":
        return ConfigData(
            notice_time_datas = data_dict.get("notice_time_datas"),
            update_check_term = data_dict.get("update_check_term"),
            token = data_dict.get("token"),
            bot_id = data_dict.get("bot_id")
        )

    @staticmethod
    def CreateBasicObject() -> "ConfigData":
        return ConfigData(
            notice_time_datas = [{"hour": 9, "minute": 0}],
            update_check_term = 10,
            token = "",
            bot_id = 0
        )

