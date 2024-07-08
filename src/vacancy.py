from abc import ABC, abstractmethod


class Vacancy:
    """
    Представляет класс Вакансия.
    """
    name: str
    url: str
    salary: dict
    requirement: str

    def __init__(self, name: str, url: str, salary: dict, requirement: str) -> None:
        self.name = name
        self.url = url if url else ""
        # Если зарплата не указана, создаем пустой диапазон
        self.salary = salary if salary else {"from": 0, "to": 0}
        self.requirement = requirement

    @classmethod
    def new_vacancy(cls, name, url, salary, requirement):
        return cls(name, url, salary, requirement)

    @classmethod
    def cast_to_object_list(cls, data: list[dict[any:any]]):
        """
        Возвращает список экземпляров класса Вакансия
        :param data:
        :return:
        """
        vacancies_list = []
        for item in data:
            vacancy = Vacancy(
                name=item.get('name'),
                url=item.get('url'),
                salary=item.get('salary'),
                requirement=item.get('requirement'),
            )

            vacancies_list.append(vacancy)
        return vacancies_list

    # Метод сравнения вакансий по зарплате
    def compare_salaries(self, other):
        from1 = self.salary.get('from', 0)
        to1 = self.salary.get('to', from1)
        from2 = other.salary.get('from', 0)
        to2 = other.salary.get('to', from2)

        if to1 < from2:
            return -1
        elif from1 > to2:
            return 1
        else:
            return 0

    def __lt__(self, other):
        return self.compare_salaries(other) == -1

    def __eq__(self, other):
        return self.compare_salaries(other) == 0

    def __gt__(self, other):
        return self.compare_salaries(other) == 1

    def __str__(self):
        return f"Vacancy: {self.name} ({self.salary}), требования: {self.requirement}, ссылка: {self.url}"

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.requirement}, {self.url})"



# Пример использования
# vacancy1 = Vacancy("Python Developer", "https://example.com", {'from': 80000, 'to': 120000},
#                    "Experience with Python required")
# vacancy2 = Vacancy("Data Scientist", "https://example.com", {'from': 100000},
#                    "Experience with machine learning required")
#
# print(vacancy1 == vacancy2)  # Сравнение вакансий по зарплате
# print(vacancy1)  # Вывод информации о вакансии

# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")