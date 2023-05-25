from typing import Optional
from datetime import datetime

import discord

from src.DataTransferObject.ConfigData import ConfigData


class NoticeFunc:
    @staticmethod
    def isNoticeTime(config_data: ConfigData) -> bool:
        for notice_time_data in config_data.NoticeTimes:
            notice_hour = notice_time_data.get("hour")
            notice_min = notice_time_data.get("minute")

            current_time_data = datetime.today()
            current_hour = current_time_data.hour
            current_min = current_time_data.minute

            if notice_hour == current_hour and notice_min == current_min:
                return True

            else:
                return False

    @staticmethod
    def NoticeCommandsInfo() -> discord.Embed:
        rt_embed = discord.Embed(
            title = "**`!알림`** 명령어 목록"
            # description = "**`!알림`** 명령어의 정보입니다."
        )

        rt_embed.add_field(
            name = "1. 시간",
            value = "알림 예약 시간데이터를 확인 및 설정합니다.\n사용법 : `!알림 시간 <설정 / 확인>`"
        )

        rt_embed.add_field(
            name = "2. 갱신주기",
            value = "과제 데이터 갱신 주기를 확인 및 설정합니다.\n사용법 : `!알림 갱신주기 <설정 / 확인>`"
        )

        return rt_embed

    @staticmethod
    def ShowNoticeTimeData() -> discord.Embed:
        rt_embed = discord.Embed(
            title = "현재 설정된 알림 시간 목록 입니다."

        )




