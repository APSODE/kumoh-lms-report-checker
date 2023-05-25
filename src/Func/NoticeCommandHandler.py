from discord.ext.commands import Context
from discord.ext import commands
from src.Func.BaseCommandHandler import BaseCommandHandler
from src.Func.NoticeFunc import NoticeFunc


class NoticeCommandHandler(BaseCommandHandler):
    def __init__(self, ctx: Context, ica_result: dict, ica_length: int):
        super().__init__(
            ctx = ctx,
            ica_result = ica_result,
            ica_length = ica_length
        )

    def HandleCommand(self):
        if self._command_args_amount == 0:
            await self._ctx.send(
                embed = NoticeFunc.NoticeCommandsInfo()
            )

        elif self._command_args_amount == 2:
            first_arg = self._command_args.get("1")
            second_arg = self._command_args.get("2")

            if first_arg == "시간":
                if second_arg not in ["설정", "확인"]:
                    raise commands.MissingRequiredArgument("**`<설정 / 확인>`**")






