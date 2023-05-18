class ConfigFileNotExistError(Exception):
    def __str__(self):
        return "Config파일이 해당 경로에 존재하지 않습니다."
