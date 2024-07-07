from config import FILE_WORKER_PATH, VACANCIES_JSON_PATH
from src.api import HeadHunterAPI
from src.file_manager import JSONSaver
from src.vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI(FILE_WORKER_PATH)

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы контструктора класса с одной вакансией
vacancy1 = Vacancy("Python Developer", "https://example.com", {'from': 80000, 'to': 120000},
                   "Experience with Python required")
vacancy2 = Vacancy("Java Developer", "https://example.com", {'from': 800000, 'to': 1200000},
                   "Experience with Java required")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver(VACANCIES_JSON_PATH)
json_saver.add_vacancy(vacancy1)
json_saver.add_vacancy(vacancy2)
json_saver.delete_vacancies()


