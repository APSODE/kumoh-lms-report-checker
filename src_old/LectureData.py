from src_old.JsonReadWriteTools import JsonReadWrite


class LectureData:
    def __init__(self,
                 course_url: str,
                 report_url: str,
                 lecture_code: str,
                 lecture_name: str
                 ):
        self._course_url = course_url
        self._report_url = report_url
        self._lecture_code = lecture_code
        self._lecture_name = lecture_name

    @property
    def CourseUrl(self) -> str:
        return self._course_url

    @property
    def ReportUrl(self) -> str:
        return self._report_url

    @property
    def LectureCode(self) -> str:
        return self._lecture_code

    @property
    def LectureName(self) -> str:
        return self._lecture_name

    def GetDataByDict(self):
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

    @staticmethod
    def CreateDataObject(lecture_name: str):
        lecture_data = JsonReadWrite.ReadJson(
            json_file_dir = "lecture_data.json" if __name__ == "__main__" else ".\\src_old\\lecture_data.json"
        ).get(lecture_name)

        return LectureData(
            course_url = lecture_data["url"]["c"],
            report_url = lecture_data["url"]["r"],
            lecture_code = lecture_data["code"],
            lecture_name = lecture_name
        )
