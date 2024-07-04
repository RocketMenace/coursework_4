import pytest
from src.parser_hh import ParserHH
from entities.salary import Salary



@pytest.fixture
def parser_example():
    return ParserHH()

@pytest.fixture
def salary_example():
    return Salary(None, 400, "USD", False)

