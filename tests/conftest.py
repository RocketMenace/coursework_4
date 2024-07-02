import pytest
from src.parser_hh import ParserHH



@pytest.fixture
def parser_example():
    return ParserHH()

