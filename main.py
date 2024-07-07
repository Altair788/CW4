from config import FILE_WORKER_PATH
from src.api import HeadHunterAPI

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI(FILE_WORKER_PATH)

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
