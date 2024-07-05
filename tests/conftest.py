import pytest
from src.parser_hh import ParserHH
from entities.salary import Salary
from entities.vacancy_description import VacancyDescription
from entities.employer import Employer


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
    return Employer(name="Test", link="https://test.com")
