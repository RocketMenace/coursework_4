from src.parser_hh import ParserHH


class VacancyDescription:
    requirement: str
    responsibility: str

    def __init__(self, requirement, responsibility):
        self.requirement = requirement
        self.responsibility = responsibility

    @property
    def requirement(self):
        requirements_lines = [
            "Требования: ",
        ]
        requirements_lines.extend([x for x in self._requirement.split(". ") if x])
        return "\n".join(requirements_lines)

    @requirement.setter
    def requirement(self, value):
        self._requirement = value

    @property
    def responsibility(self):
        responsibility_lines = [
                     "Обязанности: ",
                ]
        responsibility_lines.extend([x for x in self._responsibility.split(". ") if x])
        return "\n".join(responsibility_lines)

    @responsibility.setter
    def responsibility(self, value):
        self._responsibility = value

    def __str__(self):
        return f"{self.requirement}\n{self.responsibility}"




