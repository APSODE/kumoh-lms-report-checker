class ConfigDataSetterNotExistError(Exception):
    def __str__(self):
        return "ConfigData의 구성 데이터중 필요한 데이터가 존재하지 않습니다."


class ConfigDataInvalidSetterDataError(Exception):
    def __str__(self):
        return "ConfigData의 setter의 입력값이 올바르지 않습니다.\nSetter구현부를 다시 확인하십시오."
