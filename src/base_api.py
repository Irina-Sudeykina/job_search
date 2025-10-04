from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с api
    """

    @abstractmethod
    def __load_vacancies(self):
        """
        Абстрактный приватный метод для подключения к api
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Абстрактный метод для получения вакансий
        """
        pass
