from src.vacancy import Vacancy


class GetAverageSalaryMixin:
    """
    Класс-миксин для вычисления средней зарплаты по списку вакансий.
    """

    @staticmethod
    def calculate_average_salary(vacancies: list[Vacancy]):
        """
        Вычисляет среднюю зарплату по списку вакансий.
        Args:
            vacancies (List['Vacancy']): Список объектов класса Vacancy

        Returns:
            float: Средняя зарплата
        """

        total_salaries = sum(
            [(vacancy.salary.get("from", 0) + vacancy.salary.get("to", 0)) / 2 for vacancy in vacancies])
        total_vacancies = len(vacancies)
        if total_vacancies > 0:
            return total_salaries / total_vacancies
        else:
            return 0
