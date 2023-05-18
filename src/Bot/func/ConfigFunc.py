import os
from src.Bot.utils.JsonReadWrite import JsonReadWrite
from src.DataTransferObject.ConfigData import ConfigData
from src.CustomException.BotRelatedException import ConfigFileNotExistError

CONFIG_FILE_DIR = ".\\config.json"


class ConfigFunc:
    @staticmethod
    def _create_config_file():
        basic_config_object = ConfigData(
            notice_time_datas = [{"hour": 9, "minute": 0}],
            update_check_term = 10,
            token = "",
            bot_id = 0
        )

        JsonReadWrite.WriteJson(
            write_data = basic_config_object.GetAllDataByDict(),
            write_target_dir = CONFIG_FILE_DIR
        )

    @staticmethod
    def GetConfigDataObject() -> ConfigData:
        if not os.path.exists(CONFIG_FILE_DIR):
            raise ConfigFileNotExistError()

        return ConfigData.CreateObjectByDir(config_file_dir = CONFIG_FILE_DIR)

    @staticmethod
    def SetConfigData(data_object: ConfigData):
        JsonReadWrite.WriteJson(
            write_data = data_object.GetAllDataByDict(),
            write_target_dir = CONFIG_FILE_DIR
        )

    @staticmethod
    def CheckConfigData() -> bool:
        check_status = True

        config_data_object = ConfigFunc.GetConfigDataObject()
        for check_key in ["token", "id", "update_time_datas", "update_check_term"]:
            check_data = config_data_object.GetAllDataByDict().get(check_key)
            if check_data is None:
                check_status = False

        return check_status


