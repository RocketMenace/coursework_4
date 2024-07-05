from src.base_vacancy import BaseVacancy
from src.parser_hh import ParserHH


class Vacancy(BaseVacancy):
    name: str
    link: str
    pay: int
    description: str

    def __init__(self, name, link, description, pay):
        self.name = name
        self.link = link
        self.pay = pay
        self.description = description

    @classmethod
    def new_vacancy(cls, name, link, pay, description):
        return cls(
            name,
            link,
            pay,
            description,
        )

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.link}, {self.description}, {self.pay})"

    def __str__(self):
        return f"{self.name},\n {self.link},\n {self.description},\n {self.pay}\n"

    def __eq__(self, other) -> bool:
        return self.pay == other.pay

    def __ne__(self, other) -> bool:
        return self.pay != other.pay

    def __gt__(self, other) -> bool:
        return self.pay > other.pay

    def __lt__(self, other) -> bool:
        return self.pay < other.pay


parser = ParserHH()
parser.load_vacancies("Python")
content = parser.vacancies[:3]
print(content)
# vacancies = []
# for item in content:
#     vacancy = Vacancy.new_vacancy(
#         item["name"],
#         item["alternate_url"],
#         item["snippet"]["responsibility"],
#         item["snippet"]["requirement"],
#         item["salary"]["to"],
#     )
#     vacancies.append(vacancy)
# for v in vacancies:
#     print(str(v))
