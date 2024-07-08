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
        self.vacancies = self.load_from_file()

    def add_vacancy(self, vacancy):
        self.vacancies["name"] = vacancy.name,
        self.vacancies["url"] = vacancy.url,
        self.vacancies["salary"] = vacancy.salary,
        self.vacancies["requirement"] = vacancy.requirement,
        self.save_to_file()

    def save_to_file(self):
        with open(self.file_path, 'w', encoding="UTF8") as file:
            json.dump(self.vacancies, file, indent=4)

    def get_vacancies(self, key_words):
        result = [v for v in self.vacancies if key_words(v)]
        return result

    def delete_vacancies(self):
        self.vacancies = []
        self.save_to_file()

    def add_vacancy_to_db(self, vacancy):
        pass

    def load_from_file(self):
        try:
            with open(self.file_path, 'r', encoding="UTF8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

# # Пример использования класса JSONFileHandler с заглушкой add_vacancy_to_db
# file_handler = JSONFile(VACANCIES_JSON_PATH)
# vacancy1 = Vacancy("Python Developer", "https://example.com", {'from': 80000, 'to': 120000},
# #                    "Experience with Python required")
# file_handler.add_vacancy(vacancy1)
# file_handler.add_vacancy_to_db(vacancy1)  # Вызываем заглушку для добавления в БД
#
#
