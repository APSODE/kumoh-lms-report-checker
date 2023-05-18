from src.DataTransferObject.TokenIdData import TokenIdData
from src.Bot.func.ConfigFunc import ConfigFunc


class TokenIdDataCreator:
    @staticmethod
    def CreateTokenData() -> TokenIdData:
        config_data_object = ConfigFunc.GetConfigDataObject()

        return TokenIdData.CreateObject(
            token = config_data_object.Token,
            id = config_data_object.ID
        )


