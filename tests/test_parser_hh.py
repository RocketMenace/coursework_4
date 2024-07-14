

def test_parser_hh_init(parser_example):
    assert parser_example.url == "https://api.hh.ru/vacancies"
    assert parser_example.headers == {"User-Agent": "api-test-agent"}
    assert parser_example.params == {'text': '', 'page': 0, "per_page": 100}
    assert parser_example.vacancies == []


# def test_parser_load_vacancies(parser_example):
#     parser_example.load_vacancies()
#     assert parser_example.vacancies ==