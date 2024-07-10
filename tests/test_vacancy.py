def test_vacancy_init(vacancy_example):
    assert vacancy_example.name == "Junior Python разработчик"
    assert vacancy_example.link == "https://hh_test.ru"
    assert vacancy_example.pay == "Зарплата не указана."
    assert str(vacancy_example.description) == "Требования: \nВысшее образование\nОбязанности: \nВыполнение указанных работ"
    assert str(vacancy_example.employer) == "Test https://test.com"


def test_vacancy_encode_to_dict(vacancy_example):
    assert vacancy_example.encode_to_dict() == {"name": vacancy_example.name,
                                                "link": vacancy_example.link,
                                                "pay": str(vacancy_example.pay),
                                                "description": str(vacancy_example.description).replace("\n", " "),
                                                "employer": str(vacancy_example.employer)}


