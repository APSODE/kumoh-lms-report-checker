from src.DataTransferObject.ConfigData import ConfigData
from BotConfig import BotConfig
from typing import Dict, List


class ConfigManager:
    def __init__(self):
        self._config_data_object = ConfigData.CreateObject(BotConfig())

    @property
    def ConfigDTO(self):
        return self._config_data_object

    @ConfigDTO.setter
    def ConfigDTO(self, new_dto: ConfigData):
        self._config_data_object = new_dto
