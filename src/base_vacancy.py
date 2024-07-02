from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self, name, link, pay, description, requirements):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __
