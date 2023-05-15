from typing import Optional, Dict, List
from src.DataTransferObject.ConfigData import ConfigData
from src.Bot.utils.JsonReadWrite import JsonReadWrite
from discord import Embed


CONFIG_FILE_DIR = ".\\src\\Bot\\config.json"


class NoticeFunc:
    @staticmethod
    def GetConfigDataObject() -> ConfigData:
        return ConfigData.CreateObject(config_file_dir = CONFIG_FILE_DIR)

    @staticmethod
    def SetConfigData(data_object: ConfigData):
        JsonReadWrite.WriteJson(
            write_data = data_object.GetAllDataByDict(),
            write_target_dir = CONFIG_FILE_DIR
        )

    @staticmethod
    def SetNoticeTimeData(time_datas: List[Dict[str, int]]):
        current_config_data = NoticeFunc.GetConfigDataObject()
        current_config_data.NoticeTime = time_datas

        NoticeFunc.SetConfigData(
            data_object = current_config_data
        )

    @staticmethod
    def SetUpdateCheckTerm(update_check_term: int):
        current_config_data = NoticeFunc.GetConfigDataObject()
        current_config_data.UpdateCheckTerm = update_check_term

        NoticeFunc.SetConfigData(
            data_object = current_config_data
        )

    @staticmethod
    def GetNoticeTimeDataEmbed() -> Embed:
        show_notice_time_data_embed = Embed(
            title = "현재 설정된 알림 시간",
            description = "현재 설정된 알림시간들을 보여줍니다."
        )

        return show_notice_time_data_embed

