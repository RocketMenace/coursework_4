import json
import logging
from pathlib import Path
from src.base_file_manager import BaseFileManager


class JSONFileManager(BaseFileManager):
    FILE_PATH = Path("../data/vacancies.json")

    def write_vacancy_to_file(self, vacancy) -> None:

        try:
            with JSONFileManager.FILE_PATH.open(mode="w", encoding="utf-8") as file:
                json.dump(vacancy, file, indent=4, ensure_ascii=False)
        except OSError as err:
            logging.error("Writing to a file %s failed due to: %s", JSONFileManager.FILE_PATH, err)

    def delete_vacancy_from_file(self):
        pass

    def get_vacancy_from_file(self):

        try:
            with JSONFileManager.FILE_PATH.open(mode="r", encoding="utf-8") as file:
                return json.load(file)
        except OSError as err:
            logging.error("Reading rom a file %s failed due to: %s", JSONFileManager.FILE_PATH, err)



