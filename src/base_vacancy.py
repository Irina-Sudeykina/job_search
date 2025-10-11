from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseVacancy(ABC):
    """
    Абстрактный класс вакансий
    """

    __slots__ = ["id_vacancy", "name", "url", "description", "salary"]

    @abstractmethod
    def __init__(self, id_vacancy: str, name: str, url: str, description: str, salary: Optional[Any]):
        pass

    @classmethod
    @abstractmethod
    def sorted_by_salary(cls, is_reverse=True) -> None:
        """
        Абстрактные Class метод для сортировки объектов Vacancy по зарплате
        :return: None
        """
        pass

    @classmethod
    @abstractmethod
    def top_n_salary(cls, n: int) -> list[dict]:
        """
        Абстрактный Class метод возвращает тор n вакансий по зарплате
        :param n: количество вакансий с наибольшей зарплатой
        :return: список из n словарей вакансий с наибольшими зарплатами
        """
        pass
