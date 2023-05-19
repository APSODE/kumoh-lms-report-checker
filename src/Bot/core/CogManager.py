import os
from discord.ext import commands


class CogManager:
    def __init__(self, bot_object: commands.Bot):
        self._bot = bot_object

    async def setup_cogs(self):
        for cog_file in os.listdir(".\\src\\Bot\\cogs\\"):
            if cog_file in ["BaseCommand.py", "__pycache__"]:
                pass
            else:
                try:
                    await self._bot.load_extension(f"src.Bot.cogs.{cog_file[:-3]}")

                except Exception as error:
                    print(f"{cog_file}을 cog등록에 실패하였습니다.")
