from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с api
    """

    @abstractmethod
    def _load_vacancies(self, keyword: str) -> None:
        """
        Абстрактный приватный метод для подключения к api
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Абстрактный метод для получения вакансий
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        pass
