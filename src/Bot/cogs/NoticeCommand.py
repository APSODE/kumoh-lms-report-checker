import asyncio
import os

from discord.ext import commands
from discord.ext.commands import Context
from src.Bot.func.NoticeFunc import NoticeFunc
from src.Bot.cogs.BaseCommand import BaseCommand


class NoticeCommand(BaseCommand):
    def __init__(self):
        self._file_name = os.path.basename(__file__)
        super().__init__(
            file_name = self._file_name
        )

    @commands.command(name = "SNT")
    async def SetNoticeTime(self, ctx: Context, *args):
        ica_task = asyncio.create_task(self.CommandArgumentDevider(args))
        ica_result: dict = ica_task.result()
        ica_length = len(ica_result.keys())
        user_input_time_datas = []
        hour_temp = 0

        for idx, command_argument in enumerate(ica_result):
            if int(idx) % 2 == 0:
                hour_temp = command_argument
            else:
                user_input_time_datas.append(
                    {
                        "hour": hour_temp,
                        "minute": command_argument
                    }
                )

        NoticeFunc.SetNoticeTimeData(
            time_datas = user_input_time_datas
        )
        await ctx.send("알림 시간 설정에 성공하였습니다.")

    async def cog_command_error(self, ctx: Context, error: Exception) -> None:
        pass

    @property
    def FileName(self) -> str:
        return self._file_name







