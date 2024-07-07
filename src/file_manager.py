from abc import ABC, abstractmethod
import json

from config import VACANCIES_JSON_PATH
from src.vacancy import Vacancy


class AbstractFileManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy_to_db(self, vacancy):
        pass


class JSONSaver(AbstractFileManager):
    def __init__(self, file_path):
        self.file_path = file_path
        self.vacancies = []

    @abstractmethod
    def add_vacancy(self, vacancy):
        self.vacancies.append({
            "name": vacancy.name,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "requirement": vacancy.requirement
        })
        self._save_to_file()

    def _save_to_file(self):
        with open(self.file_path, 'w', encoding="UTF8") as file:
            json.dump(self.vacancies, file, indent=4)

    @abstractmethod
    def get_vacancies(self, key_words):
        result = [v for v in self.vacancies if key_words(v)]
        return result

    @abstractmethod
    def delete_vacancies(self):
        self.vacancies = []
        self._save_to_file()

    def add_vacancy_to_db(self, vacancy):
        pass
#
# # Пример использования класса JSONFileHandler с заглушкой add_vacancy_to_db
# file_handler = JSONFile(VACANCIES_JSON_PATH)
# vacancy1 = Vacancy("Python Developer", "https://example.com", {'from': 80000, 'to': 120000},
# #                    "Experience with Python required")
# file_handler.add_vacancy(vacancy1)
# file_handler.add_vacancy_to_db(vacancy1)  # Вызываем заглушку для добавления в БД
#
#
