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
        return self._pay

    @pay.setter
    def pay(self, value):
        if value is None:
            self._pay = "Зарплата не указана."
        else:
            self._pay = value

    @classmethod
    def cast_to_list_of_objects(cls, data: list[dict]):
        vacancies = []
        for item in data:
            name = item["name"]
            link = item["alternate_url"]
            pay = Salary(**item["salary"]) if item["salary"] else None
            description = VacancyDescription(**item["snippet"])
            employer = Employer(
                item["employer"]["name"], item["employer"].get("alternate_url")
            )
            vacancy = cls(name, link, pay, description, employer)
            vacancies.append(vacancy)

        return vacancies

    def encode_to_dict(self):
        """Method for serialization Vacancy class object."""
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
