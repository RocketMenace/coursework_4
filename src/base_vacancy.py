from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def encode_to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def cast_to_list_of_objects(cls, data: list[dict]):
        pass
