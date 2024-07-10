from src.parser_hh import ParserHH
from src.vacancy import Vacancy
from src.user import User



def user_interaction():
    hh_api = ParserHH()
    username = input("Введите свое имя: ")
    user = User(username)
    print(f"Приветствую вас {user.name}")
    search_query = input("Введите поисковый запрос: ")
    hh_api.load_vacancies(search_query)
    hh_api.rename_keys()
    vacancies = Vacancy.cast_to_list_of_objects(hh_api.vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")
    filtered_vacancies = user.vacancy_filter_by_keywords(vacancies, filter_words)
    ranged_vacancies = user.vacancy_filter_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = user.sort_vacancy_by_salary(ranged_vacancies)
    top_vacancies = user.show_vacancies(sorted_vacancies, top_n)
    return top_vacancies


if __name__ == "__main__":
    print(*user_interaction(), sep="\n", end="\n")
