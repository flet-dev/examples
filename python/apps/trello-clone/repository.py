from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError

    @abstractmethod
    def remove(self, id):
        raise NotImplementedError

    @abstractmethod
    def create(self, model):
        raise NotImplementedError
