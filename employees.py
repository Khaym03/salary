from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def salary(self) -> float:
        pass


class RegularEmployee(Employee):
    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def salary(self, worked_hours: int) -> float:
        return self.rate * worked_hours
