from base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    name: str
    link: str
    pay: int
    description: str
    requirements: str

    def __init__(self, name, link, pay, description, requirements):
        self.name = name
        self.link = link
        self.pay = pay
        self.description = description
        self.requirements = requirements
