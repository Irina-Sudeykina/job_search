from abc import ABC, abstractmethod


class BaseWorkingWithFiles(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    def __init__(self, file_name: str) -> None:
        pass

    @abstractmethod
    def getting_data(self) -> list[dict]:
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def adding_data(self, new_data: list[dict], key_str: str):
        """Метод добавления данных в файл"""
        pass

    @abstractmethod
    def deleting_data(self):
        """Метод удаления данных из файла"""
        pass
