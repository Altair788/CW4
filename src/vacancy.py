from abc import ABC


class Vacancy(ABC):
    """
    Представляет абстрактный класс Vacancy.
    """

    @abstractmethod
    def __init__(self):
        """
        Абстрактный метод для инициализации класса Vacancy.
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

