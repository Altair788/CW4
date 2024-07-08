from abc import ABC, abstractmethod
import json

from config import VACANCIES_JSON_PATH
from src.mixin_get_average_salary import GetAverageSalaryMixin
from src.vacancy import Vacancy

class AbstractFileManager(ABC):

    @abstractmethod
    def save_to_file(self, *args, **kwargs):
        """
        Метод добавления вакансий в файл
        """
        pass

    @abstractmethod
    def get_vacancies_from_file(self, *args, **kwargs):
        """
        Метод получения данных из файла по критериям
        """
        pass

    @abstractmethod
    def delete_vacancies(self):
        """
        Метод удаления информации о вакансиях.
        """
        pass


class JSONSaver(AbstractFileManager, GetAverageSalaryMixin):
    def __init__(self, file_path):
        self.vacancies = []
        self.file_path = file_path
        super().__init__()

    def save_to_file(self, data):
        with open(self.file_path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        self.vacancies = []
        self.save_to_file(self.vacancies)

    def get_vacancies_from_file(self):
        with open(self.file_path, "r", encoding="UTF-8") as file:
            vacancies_data = json.load(file)
        vacancies_list = Vacancy.cast_to_object_list(vacancies_data)

        return vacancies_list
