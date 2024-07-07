from abc import ABC, abstractmethod


class Vacancy:
    """
    Представляет класс Вакансия.
    """
    name: str
    url: str
    salary: str
    requirement: str

    def __init__(self, name: str, url: str, salary: str, requirement: str) -> None:
        self.name = name
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.requirement = requirement

    @classmethod
    def new_vacancy(cls, name, url, salary, requirement):
        return cls(name, url, salary, requirement)

    # Метод валидации данных

    def validate(self):
        if not self.salary:
            self.salary = "Зарплата не указана"

    # Метод сравнения вакансий по зарплате
    def __lt__(self, other):
        try:
            self_salary = int(self.salary.split()[0].replace('руб', '').replace(' ', ''))
            other_salary = int(other.salary.split()[0].replace('руб', '').replace(' ', ''))
            return self_salary < other_salary
        except ValueError:
            return False
        except AttributeError:
            return False

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        try:
            self_salary = int(self.salary.split()[0].replace('руб', '').replace(' ', ''))
            other_salary = int(other.salary.split()[0].replace('руб', '').replace(' ', ''))
            return self_salary > other_salary
        except ValueError:
            return False
        except AttributeError:
            return False

    def __str__(self):
        return f"Vacancy: {self.name} ({self.salary})"

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary})"

# Пример использования
# vacancy1 = Vacancy("Python Developer", "https://example.com", "80 000 руб.", "Experience with Python required")
# vacancy2 = Vacancy("Data Scientist", "https://example.com", "100 000 руб.", "Experience with machine learning required")
#
# print(vacancy1 == vacancy2)  # Сравнение вакансий по зарплате
# print(vacancy1)  # Вывод информации о вакансии
