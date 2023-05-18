from typing import Optional, Dict, Union, Any, List
from src.Bot.utils.JsonReadWrite import JsonReadWrite
from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject
from src.CustomException.DTOException import *


class ConfigData(BaseDataTransferObject):
    def __init__(self, file_dir: Optional[str] = None, config_data_dict: Optional[Dict[str, Any]] = None):
        self._config_file_data = JsonReadWrite.ReadJson(file_dir) if config_data_dict is None else config_data_dict

        time_data_temp = self._config_file_data.get("time_data")
        update_check_term_temp = self._config_file_data.get("update_check_term")

        self._notice_time_datas = time_data_temp if time_data_temp is not None else [{"hour": 0, "minute": 0}]
        self._update_check_term = update_check_term_temp if update_check_term_temp is not None else 10

    @property
    def NoticeTime(self) -> List[Dict[str, int]]:
        return self._notice_time_datas

    @NoticeTime.setter
    def NoticeTime(self, new_time_datas: List[Dict[str, int]]):
        for new_time_data in new_time_datas:
            if new_time_data.get("hour") is None or new_time_data.get("minute") is None:
                raise ConfigDataSetterNotExistError()

        self._notice_time_datas = new_time_datas

    @property
    def UpdateCheckTerm(self) -> int:
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
    def CreateObject(config_file_dir: str) -> "ConfigData":
        return ConfigData(
            file_dir = config_file_dir
        )

    @staticmethod
    def SerializeData(data_dict: Dict[str, Any]) -> "ConfigData":
        return ConfigData(
            config_data_dict = data_dict
        )
