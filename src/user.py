"""
This module creates object type User for interacting with user in main module program.
It includes methods for :
1.Filtration vacancies by keywords that are located in vacancy description.
2.Filtration vacancies by top salary.
3.Sorting vacancies by salary in ascending order.
4.Presents a list of vacancies to the user in a convenient way.
"""


from src.vacancy import Vacancy


class User:
    name: str

    def __init__(self, name):
        self.name = name.title()

    def vacancy_filter_by_keywords(self, vacancies: list[Vacancy], keywords=None):
        """Filters out items from list by specified keywords."""
        if keywords:
            filtered_vacancies: list = []
            for keyword in keywords:
                for vacancy in vacancies:
                    if keyword.title() in str(vacancy.description) and vacancy not in filtered_vacancies:
                        filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return vacancies

    def vacancy_filter_by_salary(self, vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
        """Returns list of vacancies if salary in specified range."""
        try:
            bottom, top = [int(x) for x in salary_range.split()]
            return [v for v in vacancies if v.pay in range(bottom, top + 1)]
        except ValueError as err:
            print("Диапазон зарплат не указан")
            return [v for v in vacancies]

    def sort_vacancy_by_salary(self, vacancies: list[Vacancy]):
        """Returns list of vacancies are sorted by salary."""
        try:
            return sorted(vacancies)
        except TypeError as err:
            return vacancies

    def show_vacancies(self, list_of_vacancies: list, number_of_vacancies: int) -> list:
        """Returns list of vacancies specified length"""
        return list_of_vacancies[:number_of_vacancies + 1]
