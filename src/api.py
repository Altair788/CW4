import json
from abc import ABC, abstractmethod
from pathlib import Path

import requests

from config import TEXT, PAGE, PER_PAGE


class API(ABC):
    """
    Представляет абстрактный класс API.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Абстрактный метод для инициализации класса API.
        Args:
            file_worker_path: Path - ссылка на файл с данными для работы.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Абстрактный метод для получения вакансий по ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.
        """

        pass

    @abstractmethod
    def post_data(self, url_post: str):
        """
       Абстрактный метод для отправки запроса по эндпоинту.

       Args:
           url_post (str): URL запроса
       """
        pass


class Parser(API):
    """
    Представляет класс для парсинга и обработки данных по вакансиям.

    Наследует функциональность от абстрактного класса API.
    """

    def __init__(self, file_worker_path: Path):
        """
        Метод для инициализации класса API.

        Args:
            file_worker_path (Path): Путь к файлу для работы.
        """
        self.file_worker_path = file_worker_path

        with open(self.file_worker_path, 'r', encoding="UTF8") as file:
            file_worker = json.load(file)
            self.url: str = file_worker.get('url', 'https://api.hh.ru/vacancies')
            self.headers: dict = file_worker.get('headers', {'User-Agent': 'HH-User-Agent'})
            self.params: dict = file_worker.get('params', {'text': TEXT, 'page': PAGE, 'per_page': PER_PAGE})
            self.vacancies: list = file_worker.get('vacancies', [])

    def get_vacancies(self, keyword: str) -> list:
        """
        Метод ля получения вакансий в формате JSON.
        Args:
            keyword (str): Ключевое слово для поиска вакансий.
        Returns:
            self.vacancies(list(dict): Список с вакансиями
        """

        pass

    def post_data(self, url_post):
        pass


class HeadHunterAPI(Parser):
    def __init__(self, file_worker_path) -> None:
        super().__init__(file_worker_path)

    def get_vacancies(self, keyword: str) -> list:
        """
        Метод ля получения вакансий в формате JSON.
        Args:
            keyword (str): Ключевое слово для поиска вакансий.
        Returns:
            self.vacancies(list(dict): Список с вакансиями
        """

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            except requests.exceptions.RequestException as e:
                print(f"Ошибка {e}")
        return self.vacancies
