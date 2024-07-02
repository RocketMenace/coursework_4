from abc import ABC, abstractmethod


class BaseParser(ABC):
    """Abstract base class for parser creation."""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Function for fetching raw data from specified self.url."""
        pass

    # @abstractmethod
    # def load_vacancies_from_cache(self, json_cache: str):
    #     """Function for fetching data from local cache if request is the same."""
    #     pass
