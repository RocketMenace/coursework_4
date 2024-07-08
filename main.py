from src.parser_hh import ParserHH
from src.vacancy import Vacancy



def user_interaction():
    hh_api = ParserHH()
    search_query = input("Введите поисковый запрос: ")
    hh_api.load_vacancies(search_query)
    hh_api.rename_keys()
    print(Vacancy.cast_to_list_of_objects(hh_api.vacancies))

    # top_n = input("Введите количество вакансий для вывода в топ N: ")













if __name__ == "__main__":
    user_interaction()