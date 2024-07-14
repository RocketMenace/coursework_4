import pytest
from src.parser_hh import ParserHH
from entities.salary import Salary
from entities.vacancy_description import VacancyDescription
from entities.employer import Employer
from src.user import User
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_example():
    return Vacancy(
        "Junior Python разработчик",
        "https://hh_test.ru",
        None,
        VacancyDescription(
            requirement="Высшее образование",
            responsibility="Выполнение указанных работ",
        ),
        Employer(name="Test", url="https://test.com"),
    )


@pytest.fixture
def parser_example():
    return ParserHH()


@pytest.fixture
def salary_example():
    return Salary(None, 400, "USD", False)


@pytest.fixture
def vacancy_description_example():
    return VacancyDescription(
        requirement="Высшее образование", responsibility="Выполнение указанных работ"
    )


@pytest.fixture
def employer_example():
    return Employer(name="Test", url="https://test.com")


@pytest.fixture
def user_example():
    return User("Ryan Gosling")
