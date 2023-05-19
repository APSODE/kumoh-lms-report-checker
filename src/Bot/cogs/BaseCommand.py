from abc import abstractmethod
from typing import Tuple, Any, Dict
from discord.ext import commands
from discord.ext.commands import Context


class BaseCommand(commands.Cog):
    @staticmethod
    async def CommandArgumentDevider(arguments: Tuple[Any]) -> Dict[str, Any]:
        return {str(arg_num): arg_value for arg_num, arg_value in enumerate(arguments)}

    @abstractmethod
    async def cog_command_error(self, ctx: Context, error: Exception) -> None:
        pass

    @property
    @abstractmethod
    def FileName(self):
        pass
