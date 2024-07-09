from abc import ABC, abstractmethod
import json
from typing import Any

from src.mixin_get_average_salary import GetAverageSalaryMixin
from src.vacancy import Vacancy


class AbstractFileManager(ABC):
    """
    Представляет абстрактный класс Файлового менеджера.
    """

    @abstractmethod
    def save_to_file(self, *args: Any, **kwargs: Any) -> None:
        """
        Метод добавления вакансий в файл
        """
        pass

    @abstractmethod
    def get_vacancies_from_file(self, *args: Any, **kwargs: Any) -> list[dict]:
        """
        Метод получения данных из файла по критериям
        """
        pass

    @abstractmethod
    def delete_vacancies(self) -> None:
        """
        Метод удаления информации о вакансиях.
        """
        pass


class JSONSaver(AbstractFileManager, GetAverageSalaryMixin):
    """
    Класс для работы с содержимым файла: сохранения и загрузки вакансий в/из JSON-файла.
    """
    def __init__(self, file_path: str) -> None:
        """
        Конструктор объекта JSONSaver
        Args:
        file_path (str): Путь к файлу для сохранения/загрузки вакансий.
        """
        self.vacancies: list[Vacancy] = []
        self.file_path = file_path

    def save_to_file(self, data: list[dict]) -> None:
        """
        Сохраняет список вакансий в JSON-файл.

        Args:
            data (list[dict]): Список вакансий в формате словарей.
        """
        with open(self.file_path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self) -> None:
        """
        Удаляет все вакансии из списка и сохраняет пустой список в файл.
        """
        self.vacancies = []
        self.save_to_file(self.vacancies)

    def get_vacancies_from_file(self) -> list[Vacancy]:
        """
        Загружает вакансии из JSON-файла и возвращает список вакансий.

        Returns:
            list[Vacancy]: Список вакансий.
        """
        with open(self.file_path, "r", encoding="UTF-8") as file:
            vacancies_data = json.load(file)
        vacancies_list = Vacancy.cast_to_object_list(vacancies_data)

        return vacancies_list
