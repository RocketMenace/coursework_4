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
            self._bottom_salary = "не указано"
        else:
            self._bottom_salary = value

    @property
    def top_salary(self):
        return self._top_salary

    @top_salary.setter
    def top_salary(self, value):
        if not value:
            self._top_salary = "не указано"
        else:
            self._top_salary = value

    def __str__(self):
        if not self.gross:
            return f"Заработная плата в {self.currency} до вычета налогов от {self.bottom_salary} -> до {self.top_salary}."
        return f"Заработная плата в {self.currency} за вычетом налогов от {self.bottom_salary} -> до {self.top_salary}."

    def __eq__(self, other) -> bool:
        if isinstance(other, Salary):
            return self.top_salary == other.top_salary
        if isinstance(other, (int, float)):
            return self.top_salary == other
        raise TypeError

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        return not self.__lt__(other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Salary):
            return self.top_salary < other.top_salary
        if isinstance(other, (int, float)):
            return self.top_salary < other
        raise TypeError

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other) -> bool:
        return not self.__lt__(other)
