from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self, name, link, pay, description):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_vacancy(cls, name, link, pay, description):
        pass
