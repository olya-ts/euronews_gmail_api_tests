import json

from framework.utils.logger import Logger


class FileUtils:
    @staticmethod
    def get_data_from_json(json_file_path: str):
        Logger.info("Reading from the json file " + json_file_path)
        with open(json_file_path) as file:
            return json.load(file)
