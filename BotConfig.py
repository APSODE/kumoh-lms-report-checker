from typing import Dict, List


class BotConfig:
    # NOTICE_TIME_DATAS는 업데이트된 과제 목록 중에서 미제출인 과제를 알려주는 알림 시간을 지정하는 값으로,
    # NOTICE_TIME_DATAS: List[Dict[str, int]] = [
    #     {
    #         "hour": 0,
    #         "minute": 0
    #     }
    # ]
    # 와 같이 작성되면 0시 0분에 알림이 작동한다.
    # 또, 여러 시간을 지정하고 싶으면
    # NOTICE_TIME_DATAS: List[Dict[str, int]] = [
    #     {
    #         "hour": 0,
    #         "minute": 0
    #     },
    #     {
    #         "hour": 1,
    #         "minute": 1
    #     }
    # ]
    # 와 같이 작성하면 0시 0분, 1시 1분 에 알림이 작동한다. 최대 갯수의 제한은 없으므로, 원하는 알림 시간을 지정하면 된다.
    # 시간형식은 24시간 형식이다. (ex : 오후 6시 0분 -> 18시 0분)

    NOTICE_TIME_DATAS: List[Dict[str, int]] = [
        {
            "hour": 0,
            "minute": 0
        }
    ]

    # UPDATE_CHECK_TERM은 과제 데이터의 갱신 주기를 지정하는 값으로 단위는 분이다.
    UPDATE_CHECK_TERM: int = 10

    # TOKEN은 BOT의 토큰 값은 문자열로 주어지므로 아래의 빈문자열 속에 집어 넣으면 된다.
    TOKEN: str = ""

    # BOT_ID는 Integer 자료형으로 문자열이 아닌 정수형으로 입력하여야한다.
    BOT_ID: int = 0
