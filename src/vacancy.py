from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @classmethod
    @abstractmethod
    def new_vacancy(cls, *args, **kwargs):
        pass


class PrintMixin:
    """
    Класс-миксин для печати информации о созданном объекте
    """

    def __init__(self):
        # print(repr(self))
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.url}', {self.salary}, {self.requirement})"


class Vacancy(BaseVacancy, PrintMixin):
    """
    Представляет класс Вакансия.
    """
    name: str
    url: str
    salary: dict
    requirement: str

    # Статическая переменная для хранения всех вакансий
    vacancies = []

    def __init__(self, name: str, url: str, salary: dict, requirement: str) -> None:
        """
        Конструктор экземпляра класса Вакансия.
        """
        self.__name = name if name else ""
        self.__url = url if url else ""
        # Если зарплата не указана, создаем пустой диапазон
        if salary:
            salary_from = salary.get('from', 0) if salary.get('from') is not None else 0
            salary_to = salary.get('to', 0) if salary.get('to') is not None else 0

            self.__salary = {'from': salary_from, 'to': salary_to}
        else:
            self.__salary = {"from": 0, "to": 0}

        self.__requirement = requirement if requirement else ""

        super().__init__()

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def requirement(self):
        return self.__requirement

    def __str__(self):
        """
       Выводит строковое представление объекта класса Вакансия.
        """
        salary_str = ""
        if self.salary.get("from") and self.salary.get("to"):
            salary_str = f"{self.salary['from']} - {self.salary['to']}"
        else:
            salary_value = self.salary.get("from") or self.salary.get("to")
            salary_str = str(salary_value) if salary_value else ""

        return (f"Название вакансии: {self.name}\n"
                f"Ссылка на вакансию: {self.url}\n"
                f"Зарплата: {salary_str}\n"
                f"Требования к вакансии: {self.requirement}")

    @classmethod
    def new_vacancy(cls, vacancy):
        name, url, salary, requirement = vacancy.values()
        return cls(name, url, salary, requirement)

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

    @classmethod
    def cast_to_object_list(cls, data):
        """
        Возвращает список экземпляров класса Vacancy.
        """
        vacancies_list = []
        for item in data:
            salary = item.get("salary")
            if salary:
                salary_from = salary.get('from', 0) if salary.get('from') is not None else 0
                salary_to = salary.get('to', 0) if salary.get('to') is not None else 0
            else:
                # Устанавливаем значения зарплаты по умолчанию, если отсутствует salary
                salary_from, salary_to = 0, 0

            vacancy = cls(
                name=item.get("name", ""),
                url=item.get("url", ""),
                salary={'from': salary_from, 'to': salary_to},
                requirement=item.get("snippet", {}).get("requirement", ""),
            )
            vacancies_list.append(vacancy)
        return vacancies_list
