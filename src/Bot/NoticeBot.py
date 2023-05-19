import discord
from discord.ext import commands, tasks
from discord import Intents
from src.Bot.core.ConfigManager import ConfigManager
from src.Bot.core.CogManager import CogManager


class NoticeBot(commands.Bot):
    def __init__(self):
        default_intents = Intents.default()
        default_intents.message_content = True

        super(NoticeBot, self).__init__(
            command_prefix = "!",
            intents = default_intents,
            sync_command = True
        )

        self._cog_manager = CogManager(
            bot_object = self
        )

        self._config_manager = ConfigManager()

    def _start(self):
        self.run(
            self._config_manager.ConfigDTO.Token
        )

    async def on_ready(self):
        print("봇이 정상적으로 실행되었습니다.")
        current_bot_activity = discord.Game("과제")

        await self.change_presence(
            status = discord.Status.online,
            activity = current_bot_activity
        )
        await self._cog_manager.setup_cogs()
