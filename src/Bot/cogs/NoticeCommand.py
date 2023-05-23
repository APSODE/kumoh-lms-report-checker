import os
import asyncio
from discord.ext.commands import Context
from discord.ext import commands
from discord import Embed
from src.Bot.cogs.BaseCommand import BaseCommand


class NoticeCommand(BaseCommand):
    @commands.command(aliases = ["알림", "ㅇㄹ", "df", "dkffla"])
    async def Notice(self, ctx: Context, *args):
        ica_task = asyncio.create_task(self.CommandArgumentDevider(args))
        ica_result = ica_task.result()
        ica_length = len(ica_result.keys())

        if ica_length == 0:
            notice_commands_embed = Embed(
                title = "알림 명령어",
                description = "알림 명령어 목록"
            )

    async def cog_command_error(self, ctx: Context, error: Exception) -> None:
        pass

    @property
    def FileName(self):
        return os.path.basename(__file__)