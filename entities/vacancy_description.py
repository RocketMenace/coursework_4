import re


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
        raw_string = "\n".join(requirements_lines)
        html_pattern = re.compile("<.*?>")
        return re.sub(html_pattern, "", raw_string)

    @requirement.setter
    def requirement(self, value):
        if value:
            self._requirement = value
        else:
            self._requirement = "не указаны"

    @property
    def responsibility(self):
        responsibility_lines = [
            "Обязанности: ",
        ]
        responsibility_lines.extend([x for x in self._responsibility.split(". ") if x])
        raw_string = "\n".join(responsibility_lines)
        html_pattern = re.compile("<.*?>")
        return re.sub(html_pattern, "", raw_string)

    @responsibility.setter
    def responsibility(self, value):
        if value:
            self._responsibility = value
        else:
            self._responsibility = "не указаны"

    def __str__(self):
        return f"{self.requirement}\n{self.responsibility}"
