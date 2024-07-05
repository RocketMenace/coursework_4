from abc import ABC, abstractmethod


class BaseParser(ABC):
    """Abstract base class for parser creation."""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Function for fetching raw data from specified self.url."""
        pass


