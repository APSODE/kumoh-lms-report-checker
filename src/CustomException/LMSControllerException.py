class LoginFailException(Exception):
    def __str__(self):
        return "로그인에 실패하였습니다."

class MainPageLoadError(Exception):
    def __str__(self):
        return "메인페이지 로드에 실패하였습니다."