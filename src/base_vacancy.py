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
