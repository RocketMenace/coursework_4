from abc import ABC, abstractmethod


class BaseWriter(ABC):

    @abstractmethod
    def write_to_file(self):
        pass