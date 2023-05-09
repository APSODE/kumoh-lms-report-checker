from typing import Optional

import requests


class StatusChecker:
    @staticmethod
    def isCorrect(response: requests.Response) -> Optional[bool]:
        if response.status_code == 200:
            return True

        else:
            raise ConnectionError(f"response status code is not 200\ncurrent status code : {response.status_code}")


