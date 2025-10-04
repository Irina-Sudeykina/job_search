import json
from typing import Any

import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с API HeadHunter
    Класс BaseAPI является родительским классом
    """

    __url: str
    __headers: dict
    __params: dict
    __vacancies: list

    def __init__(self) -> None:
        """
        Иницализация класса HeadHunterAPI
        """
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __load_vacancies(self, keyword: str) -> None:
        """
        Приватный метод получения списка вакансий
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    def get_vacancies(self, keyword: str) -> Any:
        """
        Публичный метод получения вакансий в формате JSON
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        self.__load_vacancies(keyword)
        return json.dumps(self.__vacancies, indent=4)
