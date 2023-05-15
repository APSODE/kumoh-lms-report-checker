from src.DataTransferObject.TokenIdData import TokenIdData
from src.Bot.utils.JsonReadWrite import JsonReadWrite


class TokenIdDataCreator:
    @staticmethod
    def CreateTokenData(config_file_dir: str) -> TokenIdData:
        read_config_data = JsonReadWrite.ReadJson(
            json_file_dir = config_file_dir
        )

        return TokenIdData.CreateObject(
            token = read_config_data.get("token"),
            id = read_config_data.get("id")
        )


