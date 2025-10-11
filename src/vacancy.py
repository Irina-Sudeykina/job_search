import json
import re
from typing import Any, Optional

from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    """
    Класс для работы с вакансиями
    """

    __slots__ = ["id_vacancy", "name", "url", "description", "salary"]

    instances: list = []

    def __init__(self, id_vacancy: str, name: str, url: str, description: str, salary: Optional[Any]) -> None:
        """
        Инициализация класса Vacancy:
        :param id_vacancy: строка - id вакансии
        :param name: строка - наименование
        :param url: строка - ссылка на вакансию
        :param description: строка - описание
        :param salary: словарь - диапазон зарплаты
        :return: None
        """
        self.id_vacancy = id_vacancy
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary

        self.__validate_url(url)
        self.__validate_salary(salary)

        Vacancy.instances.append(self)

    def __str__(self):
        """
        Представление объекта Vacancy в текстовом виде
        """
        return (
            f"id: {self.id_vacancy} {self.name} {self.salary.get('from')}-{self.salary.get('to')} руб. url: {self.url}"
        )

    def __validate_salary(self, salary):
        """
        Валидация вакансии по зарплате
        """
        if salary is None:
            salary_vacancy = {"from": 0, "to": 0}
        elif isinstance(salary, int):
            salary_vacancy = {"from": salary, "to": salary}
        elif isinstance(salary, str):
            try:
                value = int(salary)
                salary_vacancy = {"from": value, "to": value}
            except ValueError:
                salary_vacancy = {"from": 0, "to": 0}
        elif isinstance(salary, dict):
            # Получаем зарплату с дефолтом в 0, если ключ отсутствует
            salary_from = salary.get("from", 0)
            salary_to = salary.get("to", 0)

            # Приводим возможные None-значения к числу
            salary_from = salary_from or 0
            salary_to = salary_to or 0

            # Обработка границ зарплаты
            if salary_from == 0 and salary_to > 0:
                salary_from = salary_to // 2
            elif salary_to == 0 and salary_from > 0:
                salary_to = salary_from
            elif salary_from > salary_to and salary_from > 0 and salary_to > 0:
                salary_from, salary_to = salary_to, salary_from

            salary_vacancy = {"from": salary_from, "to": salary_to}
        else:
            salary_vacancy = {"from": 0, "to": 0}

        self.salary = salary_vacancy

    def __validate_url(self, url):
        """
        Валидация вакансии по url
        """
        if isinstance(url, str):
            url_pattern = re.compile(
                r"^https?://"  # Протокол (http или https)
                r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # Доменное имя
                r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # Или IP-адрес
                r"(?::\d+)?"  # Необязательный номер порта
                r"(?:/?|[/?]\S+)$",
                re.IGNORECASE,
            )  # Необязательный путь
            if re.match(url_pattern, url) is not None:
                self.url = url
            else:
                self.url = "https://hh.ru/vacancy"
        else:
            self.url = "https://hh.ru/vacancy"

    def __eq__(self, other):
        """
        Проверка на равенство по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] == other
        elif isinstance(other, Vacancy):
            return self.salary["from"] == other.salary["from"] and self.salary["to"] == other.salary["to"]
        else:
            raise TypeError("Сравнение невозможно")

    def __ne__(self, other):
        """
        Проверка на не равенство по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] != other
        elif isinstance(other, Vacancy):
            return self.salary["from"] != other.salary["from"] and self.salary["to"] != other.salary["to"]
        else:
            raise TypeError("Сравнение невозможно")

    def __lt__(self, other):
        """
        Проверка когда первый объект меньше второго по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] < other
        elif isinstance(other, Vacancy):
            return self.salary["from"] < other.salary["from"]
        else:
            raise TypeError("Сравнение невозможно")

    def __le__(self, other):
        """
        Проверка когда первый объект меньше или равен второму по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] <= other
        elif isinstance(other, Vacancy):
            return self.salary["from"] <= other.salary["from"]
        else:
            raise TypeError("Сравнение невозможно")

    def __gt__(self, other):
        """
        Проверка когда первый объект больше второго по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] > other
        elif isinstance(other, Vacancy):
            return self.salary["from"] > other.salary["from"]
        else:
            raise TypeError("Сравнение невозможно")

    def __ge__(self, other):
        """
        Проверка когда первый объект больше или равен второго по зарплате
        """
        if isinstance(other, (float, int)):
            return self.salary["from"] >= other
        elif isinstance(other, Vacancy):
            return self.salary["from"] >= other.salary["from"]
        else:
            raise TypeError("Сравнение невозможно")

    @classmethod
    def cast_to_object_list(cls, json_vacancies) -> None:
        """
        Class метод для преобразования набора данных из JSON в список объектов Vacancy
        :param json_vacancies: JSON с вакансиями
        :return: None
        """
        # Парсим строку JSON в словарь
        hh_vacancies = json.loads(json_vacancies)

        # Проверяем есть ли такие вакансии в списке, если нет, то создаем вакансию
        for vacancy in hh_vacancies:
            if not cls.instances:
                cls(
                    vacancy.get("id", ""),
                    vacancy.get("name", ""),
                    vacancy.get("alternate_url", "https://hh.ru/vacancy"),
                    vacancy.get("snippet", "").get("requirement", ""),
                    vacancy.get("salary", 0),
                )
            else:
                is_in_list = False
                for instance in cls.instances:
                    if instance.id_vacancy == vacancy.get("id", ""):
                        instance.name = vacancy.get("name", "")
                        instance.url = vacancy.get("alternate_url", "")
                        instance.description = vacancy.get("snippet", "").get("requirement", "")
                        instance.salary = vacancy.get("salary", 0)
                        is_in_list = True

                if not is_in_list:
                    cls(
                        vacancy.get("id", ""),
                        vacancy.get("name", ""),
                        vacancy.get("alternate_url", "https://hh.ru/vacancy"),
                        vacancy.get("snippet", "").get("requirement", ""),
                        vacancy.get("salary", 0),
                    )

    @classmethod
    def sorted_by_salary(cls, is_reverse=True) -> None:
        """
        Class метод для сортировки объектов Vacancy по зарплате
        :return: None
        """
        cls.instances = sorted(cls.instances, key=lambda vacancy: vacancy, reverse=is_reverse)

    @classmethod
    def top_n_salary(cls, n: int) -> list[dict]:
        """
        Class метод возвращает тор n вакансий по зарплате
        :param n: количество вакансий с наибольшей зарплатой
        :return: список из n словарей вакансий с наибольшими зарплатами
        """
        cls.sorted_by_salary()
        print("\n".join(str(i).strip() for i in cls.instances[:n]))
        return cls.instances[:n]

    @classmethod
    def filter_by_salary(cls, salary_from: int, salary_to: int) -> list[dict]:
        """
        Class метод для фильтрации объектов Vacancy по зарплате
        :param salary_from: нижняя граница зарплаты
        :param salary_to: верняя граница зарплаты
        :return: None
        """
        filtered_instances = [
            vacancy
            for vacancy in cls.instances
            if (vacancy.salary.get("from", 0) >= salary_from and vacancy.salary.get("to", 0) <= salary_to)
        ]
        cls.instances = filtered_instances
        cls.sorted_by_salary()
        print("\n".join(str(i).strip() for i in cls.instances))
        return cls.instances

    @classmethod
    def filter_by_words(cls, words: str) -> list[dict]:
        """
        Class метод для фильтрации объектов Vacancy по тексту в описании
        :param words: строка для фильтрации
        :return: None
        """
        filtered_instances = [vacancy for vacancy in cls.instances if words.lower() in vacancy.description.lower()]
        cls.instances = filtered_instances
        print("\n".join(str(i).strip() + "\n" + i.description + "\n" for i in cls.instances))
        return cls.instances
