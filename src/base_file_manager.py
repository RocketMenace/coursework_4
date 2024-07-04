from abc import ABC, abstractmethod


class BaseFileProcessor(ABC):

    @abstractmethod
    def write_to_file(self):
        pass

    @abstractmethod
    def delete_from_file(self):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass