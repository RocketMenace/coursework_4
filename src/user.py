from src.vacancy import Vacancy


class User:
    name: str

    def __init__(self, name):
        self.name = name.title()


    def vacancy_filter_by_keywords(self, vacancies:list[Vacancy], keywords:list[str]):


    def vacancy_filter_by_salary(self, vacancies:list[Vacancy], salary_range:str):
