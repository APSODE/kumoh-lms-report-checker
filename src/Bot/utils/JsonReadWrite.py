import json


class JsonReadWrite:
    @staticmethod
    def ReadJson(json_file_dir: str) -> dict:
        with open(f"{json_file_dir}", "r", encoding = "utf-8") as read_target_file:
            read_file_data = json.load(read_target_file)

        return read_file_data

    @staticmethod
    def WriteJson(write_data: dict, write_target_dir: str) -> None:
        with open(f"{write_target_dir}", "w", encoding = "utf-8") as write_target_file:
            json.dump(write_data, write_target_file, indent = 4)


if __name__ == '__main__':
    JsonReadWrite.ReadJson(json_file_dir = "test")