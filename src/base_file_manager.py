"""
Abstract base class for creating file managers different types. It includes methods for:
1.Write data to file.
2.Delete data from file.
3.Extract data from file.
"""


from abc import ABC, abstractmethod


class BaseFileManager(ABC):

    @abstractmethod
    def write_vacancy_to_file(self, vacancy):
        """Method for writing data to file."""
        pass

    @abstractmethod
    def delete_vacancy_from_file(self):
        """Method for deleting data from file."""
        pass

    @abstractmethod
    def get_vacancy_from_file(self):
        """Method for fetching data from file."""
        pass