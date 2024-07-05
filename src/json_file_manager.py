import json
import logging
from pathlib import Path
from src.base_file_manager import BaseFileProcessor


class JSONWriter(BaseFileProcessor):

    def write_to_file(self) -> None:
        file_path = Path("../data/vacancies.json")

        try:
            with file_path.open(mode="w") as file:
                json.load(file)
        except OSError as err:
            logging.error("Writing to a file %s failed due to: %s", file_path, err)


