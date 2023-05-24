from typing import Optional
from datetime import datetime
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

    
