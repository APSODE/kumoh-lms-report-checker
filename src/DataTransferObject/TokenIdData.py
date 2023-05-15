class TokenIdData:
    def __init__(self, bot_token: str, bot_id: int):
        self._token = bot_token
        self._id = bot_id

    @property
    def Token(self) -> str:
        return self._token

    @property
    def ID(self) -> int:
        return self._id

    @staticmethod
    def CreateObject(token: str, id: int) -> "TokenIdData":
        return TokenIdData(
            bot_token = token,
            bot_id = id
        )

