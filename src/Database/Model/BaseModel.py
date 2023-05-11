from abc import abstractmethod


class BaseModel:
    @abstractmethod
    def GetAllDataByDict(self) -> dict:
        pass
