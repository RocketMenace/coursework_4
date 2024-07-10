from abc import ABC, abstractmethod


class BaseFileManager(ABC):

    @abstractmethod
    def write_vacancy_to_file(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy_from_file(self):
        pass

    @abstractmethod
    def get_vacancy_from_file(self):
        pass