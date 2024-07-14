"""
This module provides tools for creating Vacancy object. It includes methods for:

1. Class method for creating list of objects of Vacancy type.
2. Method for translating Vacancy's instance into object of type dict for further serialization.

It also includes functionality for comparing Vacancy instances by salary.
"""


from entities.employer import Employer
from entities.salary import Salary
from entities.vacancy_description import VacancyDescription
from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    name: str
    link: str
    pay: Salary
    description: VacancyDescription
    employer: Employer

    def __init__(self, name, link, pay, description, employer):
        self.name = name
        self.link = link
        self.pay = pay
        self.description = description
        self.employer = employer

    @property
    def pay(self):
        """The pay property."""
        return self._pay

    @pay.setter
    def pay(self, value):
        if value is None:
            self._pay = "Зарплата не указана."
        else:
            self._pay = value

    def __eq__(self, other):
        if type(self.pay) is str:
            self.pay = 0
        if isinstance(other, Vacancy):
            return self.pay == other.pay
        raise TypeError("Comparable types must be the same.")

    def __ne__(self, other):
        if isinstance(other, Vacancy):
            return not self.__eq__(other)
        raise TypeError("Comparable types must be the same.")

    def __gt__(self, other):
        if type(self.pay) is str:
            self.pay = 0
        if isinstance(other, Vacancy):
            return self.pay > other.pay
        raise TypeError("Comparable types must be the same.")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return not self.__gt__(other)
        raise TypeError("Comparable types must be the same.")

    def __le__(self, other):
        if type(self.pay) is str:
            self.pay = 0
        if isinstance(other, Vacancy):
            return self.__lt__(other) or self.__eq__(other)
        raise TypeError("Comparable types must be the same.")

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return not self.__le__(other)
        raise TypeError("Comparable types must be the same.")


    @classmethod
    def cast_to_list_of_objects(cls, data: list[dict]) -> list:
        """Returns list of Vacancies objects."""
        vacancies: list = []
        for item in data:
            name: str = item["name"]
            link: str = item["alternate_url"]
            pay: Salary = Salary(**item["salary"]) if item["salary"] else None
            description: VacancyDescription = VacancyDescription(**item["snippet"])
            employer: Employer = Employer(
                item["employer"]["name"], item["employer"].get("alternate_url")
            )
            vacancy: Vacancy = cls(name, link, pay, description, employer)
            vacancies.append(vacancy)

        return vacancies

    def encode_to_dict(self):
        """Method for converting Vacancy object into dict for further serialization."""
        return {
            "name": self.name,
            "link": self.link,
            "pay": str(self.pay),
            "description": str(self.description).replace("\n", " "),
            "employer": str(self.employer),
        }

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.link}, {self.description}, {self.pay})"

    def __str__(self):
        return f"{self.name},\n{self.link},\n{self.description},\n{self.pay}"
