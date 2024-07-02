from baseparser import BaseParser
from requests.exceptions import HTTPError
from requests_cache import CachedSession
from loguru import logger
from print_mixin_parser import PrintMixin


class ParserHH(BaseParser, PrintMixin):
    """Class for working with HeadHunter's API."""

    def __init__(self):
        self.url: str = "https://api.hh.ru/vacancies"
        self.headers: dict[str:str] = {"User-Agent": "api-test-agent"}
        self.params: dict = {'text': '', 'page': 0, "per_page": 100}
        self.vacancies: list = []
        super().__init__()

    def load_vacancies(self, keyword: str) -> None:
        """Function for fetching raw data from specified self.url."""
        session = CachedSession(
            cache_name="../cache/vacancy_cache",
            expire_after=120
        )

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            try:
                response = session.get(self.url, headers=self.headers, params=self.params)
                response.raise_for_status()
                # self.updated = True
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1

            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
                logger.add('errors.log', level="ERROR", format="{time} {level} {message}")
                logger.error(f"HTTP error occurred: {http_err}")
                return None


parser = ParserHH()
content = parser.load_vacancies("Python")
print(parser.vacancies)
