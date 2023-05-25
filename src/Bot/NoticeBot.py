from typing import Optional

import discord
from discord.ext import commands, tasks
from discord import Intents
from src.Bot.core.ConfigManager import ConfigManager
from src.Bot.core.CogManager import CogManager


class NoticeBot(commands.Bot):
    def __init__(self, custom_config_manager: Optional[ConfigManager] = None):
        default_intents = Intents.default()
        default_intents.message_content = True

        super(NoticeBot, self).__init__(
            command_prefix = "!",
            intents = default_intents,
            sync_command = True
        )

        if custom_config_manager is None:
            self._config_manager = ConfigManager()

        else:
            self._config_manager = custom_config_manager

        self._cog_manager = CogManager(
            bot_object = self
        )

        self._start()

    @property
    def ConfigManager(self):
        return self._config_manager

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
