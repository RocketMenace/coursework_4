"""
parser_hh.py
=============
This module provides tools for parsing hh.ru website. It includes methods for:

1.Fetching vacancy's raw data.
2.Renames keys in dicts.
"""

from loguru import logger
from requests.exceptions import HTTPError
from requests_cache import CachedSession
from src.baseparser import BaseParser


class ParserHH(BaseParser):
    """Class for working with HeadHunter's API."""

    def __init__(self):
        self.url: str = "https://api.hh.ru/vacancies"
        self.headers: dict[str:str] = {"User-Agent": "api-test-agent"}
        self.params: dict = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list = []

    def __str__(self):
        return f"{type(self).__name__}, url: {self.url}, headers: {self.headers}, params: {self.params}"

    def load_vacancies(self, keyword: str) -> None:
        """Method for fetching raw data from specified self.url."""
        session = CachedSession(cache_name="../cache/vacancy_cache", expire_after=600)

        self.params["text"] = keyword
        while self.params.get("page") != 20:
            try:
                response = session.get(
                    self.url, headers=self.headers, params=self.params
                )
                response.raise_for_status()
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1

            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
                logger.add(
                    "../errors_logs/errors.log",
                    level="ERROR",
                    format="{time} {level} {message}",
                )
                logger.error(f"HTTP error occurred: {http_err}")
                return None

    def rename_keys(self) -> None:
        """Replaces names of keys because of conflict with reserved words."""
        for vacancy in self.vacancies:
            if vacancy["salary"]:
                vacancy["salary"]["bottom_salary"] = vacancy["salary"].pop("from")
                vacancy["salary"]["top_salary"] = vacancy["salary"].pop("to")
            else:
                vacancy["salary"] = None
