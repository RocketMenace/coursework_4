def test_salary_init(salary_example):
    assert salary_example.bottom_salary == "Не указано"
    assert salary_example.top_salary == 400
    assert salary_example.currency == "USD"
    assert salary_example.gross == False
    salary_example.gross = True
    assert (
        str(salary_example)
        == f"Заработная плата за вычетом налогов от {salary_example.bottom_salary} {salary_example.currency}. -> до {salary_example.top_salary} {salary_example.currency}."
    )



