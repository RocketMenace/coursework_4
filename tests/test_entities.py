def test_salary_init(salary_example):
    assert salary_example.bottom_salary == "не указано"
    assert salary_example.top_salary == 400
    assert salary_example.currency == "USD"
    assert salary_example.gross is False
    salary_example.gross = True
    assert (
        str(salary_example)
        == f"Заработная плата за вычетом налогов от {salary_example.bottom_salary} {salary_example.currency}. -> до {salary_example.top_salary} {salary_example.currency}."
    )


def test_salary_description_init(vacancy_description_example):
    assert (
        vacancy_description_example.responsibility
        == "Обязанности: \nВыполнение указанных работ"
    )
    assert vacancy_description_example.requirement == "Требования: \nВысшее образование"


def test_employer_init(employer_example):
    assert employer_example.name == "Test"
    assert employer_example.link == "https://test.com"
