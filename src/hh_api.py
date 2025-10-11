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

    def _load_vacancies(self, keyword: str) -> None:
        """
        Приватный метод получения списка вакансий
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)

            if response.status_code != 200:
                print(f"Ошибка при получении данных: {response.status_code}")

            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    def get_vacancies(self, keyword: str) -> Any:
        """
        Публичный метод получения вакансий в формате JSON
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
        self._load_vacancies(keyword)
        return json.dumps(self.__vacancies, indent=4)

    def __load_vacancy_description(self, id_vacance: str) -> None:
        """
        Приватный метод получения полной информации по id вакансии
        :param id_vacance: строка - id вакансии
        :return: None
        """

        url = f"{self.url}/{id_vacance}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Ошибка при получении полных данных о вакансии с id {id_vacance}: {response.status_code}")

        data = response.json()
        self.__vacancies = []
        self.__vacancies.append(data)

    def get_vacancy_description(self, id_vacance: str) -> Any:
        """
        Публичный метод получения полной информации по id вакансии в формате JSON
        :param id_vacance: строка - id вакансии
        :return: None
        """
        try:
            self.__load_vacancy_description(id_vacance)
            return json.dumps(self.__vacancies, indent=4)
        except Exception as e:
            return json.dumps({"description": "Not Found", "error": str(e)}, indent=4)
