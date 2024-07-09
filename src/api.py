import json
from abc import ABC, abstractmethod
from pathlib import Path

import requests


class API(ABC):
    """
    Представляет абстрактный класс API.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Абстрактный метод для инициализации класса API.
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
       Абстрактный метод для отправки запроса.

       Args:
           url_post (str): URL запроса
       """
        pass


class Parser(API):
    """
    Представляет класс для парсинга и обработки данных по вакансиям.

    Наследует функциональность от абстрактного класса API.
    Подключается к серверу, используя данные из файла settings.
    Находит вакансии по ключевому слову.
    """
    settings_path: Path

    def __init__(self, settings_path: Path):
        """
        Метод для инициализации класса API.

        Args:
            settings_path (Path): Путь к файлу с настройками соединения.
        """
        self.__settings_path = settings_path

        with open(self.__settings_path, 'r', encoding="UTF8") as file:
            settings: dict = json.load(file)
            self.__url: str = settings.get('url', 'https://api.hh.ru/vacancies')
            self.__headers: dict = settings.get('headers', {'User-Agent': 'HH-User-Agent'})
            self.__params: dict = settings.get('params', {'text': "", 'page': 0, 'per_page': 100})
            self.__vacancies: list = settings.get('vacancies', [])

    @property
    def settings_path(self):
        return self.__settings_path

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    @property
    def vacancies(self):
        return self.__vacancies

    @vacancies.setter
    def vacancies(self, new_data: list):
        self.__vacancies = new_data

    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод для получения вакансий в формате JSON.
        Args:
            keyword (str): Ключевое слово для поиска вакансий.
        Returns:
            list[dict]: Список с вакансиями
        """
        try:
            self.__params['text'] = keyword
            response = requests.get(self.__url, params=self.__params)
            response.raise_for_status()  # Проверяем статус ответа, вызывает исключение для ошибок HTTP
            vacancies = response.json()['items']
            return vacancies
        except requests.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []

    def post_data(self, url_post: str) -> None:
        """
       Метод для отправки данных на сервер.
       Args:
           url_post (str): URL для отправки данных.
       Returns:
           None
       """
        pass


class HeadHunterAPI(Parser):
    def __init__(self, settings_path: Path) -> None:
        """
        Инициализирует объект HeadHunterAPI.
        Args:
            settings_path (Path): Путь к файлу с настройками.
        """
        super().__init__(settings_path)
