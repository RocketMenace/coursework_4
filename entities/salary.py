class Salary:
    bottom_salary: int
    top_salary: int
    currency: str
    gross: bool

    def __init__(self, bottom_salary, top_salary, currency, gross):
        self.bottom_salary = bottom_salary
        self.top_salary = top_salary
        self.currency = currency
        self.gross = gross

    @property
    def bottom_salary(self):
        return self._bottom_salary

    @bottom_salary.setter
    def bottom_salary(self, value):
        if not value:
            self._bottom_salary = "Не указано"
        else:
            self._bottom_salary = value

    @property
    def top_salary(self):
        return self._top_salary

    @top_salary.setter
    def top_salary(self, value):
        if not value:
            self._top_salary = "Не указано"
        else:
            self._top_salary = value

    def __str__(self):
        if not self.gross:
            return f"Заработная плата до вычета налогов от {self.bottom_salary} {self.currency}. -> до {self.top_salary} {self.currency}."
        return f"Заработная плата за вычетом налогов от {self.bottom_salary} {self.currency}. -> до {self.top_salary} {self.currency}."



