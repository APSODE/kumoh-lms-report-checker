from typing import Dict, List, Union
from src.DataTransferObject.BaseDataTransferObject import BaseDataTransferObject
from BotConfig import BotConfig


class ConfigData(BaseDataTransferObject):
    def __init__(self, user_config_object: BotConfig):
        self._notice_time_datas = user_config_object.NOTICE_TIME_DATAS
        self._update_check_term = user_config_object.UPDATE_CHECK_TERM
        self._token = user_config_object.TOKEN
        self._bot_id = user_config_object.BOT_ID

    @property
    def NoticeTimes(self) -> List[Dict[str, int]]:
        return self._notice_time_datas

    @property
    def UpdateCheckTerm(self) -> int:
        return self._update_check_term

    @property
    def Token(self) -> str:
        return self._token

    @property
    def BotID(self) -> int:
        return self._bot_id

    def GetAllDataByDict(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateObject(user_config_object: BotConfig) -> "ConfigData":
        return ConfigData(user_config_object = user_config_object)

    @staticmethod
    def SerializeData(data_dict: Dict[str, Union[str, bool]]):
        # ConfigData는 해당 메서드는 사용하지 않으므로 구현 안함
        pass
