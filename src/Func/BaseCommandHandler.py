from abc import abstractmethod

from discord.ext.commands import Context


class BaseCommandHandler:
    def __init__(self, ctx: Context,  ica_result: dict, ica_length: int):
        self._ctx = ctx
        self._command_args = ica_result
        self._command_args_amount = ica_length
        self.HandleCommand()

    @abstractmethod
    def HandleCommand(self):
        pass

