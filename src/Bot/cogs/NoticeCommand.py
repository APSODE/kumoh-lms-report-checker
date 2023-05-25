import os
import asyncio
from discord.ext.commands import Context
from discord.ext import commands
from discord import Embed
from src.Bot.core.ConfigManager import ConfigManager
from src.Bot.cogs.BaseCommand import BaseCommand
from src.Func.NoticeCommandHandler import NoticeCommandHandler
from src.Func.NoticeFunc import NoticeFunc
from src.Bot.NoticeBot import NoticeBot


class NoticeCommand(BaseCommand):
    def __init__(self, config_manager: ConfigManager):
        self._config_manager = config_manager

    @commands.command(aliases = ["알림", "ㅇㄹ", "df", "dkffla"])
    async def Notice(self, ctx: Context, *args):
        ica_result = await asyncio.create_task(self.CommandArgumentDevider(args))
        ica_length = len(ica_result.keys())

        command_handler = NoticeCommandHandler(
            ctx = ctx,
            ica_result = ica_result,
            ica_length = ica_length
        )

    async def cog_command_error(self, ctx: Context, error: Exception) -> None:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("해당 커멘드를 찾을수 없습니다.")

    @property
    def FileName(self):
        return os.path.basename(__file__)


async def setup(bot: NoticeBot):
    await bot.add_cog(NoticeCommand(config_manager = bot.ConfigManager))
