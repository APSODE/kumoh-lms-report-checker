import discord
from discord.ext import commands, tasks
from discord import Intents
from src.DataTransferObject.TokenData import TokenData
from src.Bot.cogs.CogHandler import CogHandler


class NoticeBot(commands.Bot):
    def __init__(self, token_data_object: TokenData):
        default_intents = Intents.default()
        default_intents.message_content = True

        super(NoticeBot, self).__init__(
            command_prefix = "!",
            intents = default_intents,
            sync_command = True
        )
        self._cog_handler = CogHandler(
            bot_object = self
        )
        self._token_data_object = token_data_object
        self._start()

    def _start(self):
        self.run(
            self._token_data_object.Token
        )

    async def on_ready(self):
        print("봇이 정상적으로 실행되었습니다.")
        current_bot_activity = discord.Game("과제")
        await self.change_presence(status = discord.Status.online, activity = current_bot_activity)
        await self._cog_handler.setup_cogs()








