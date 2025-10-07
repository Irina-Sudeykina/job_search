import json

import pytest

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def head_hunter_api():
    return HeadHunterAPI()


@pytest.fixture
def vacancy1():
    """
    Фикстура экземпляра класса Vacancy - 1
    Присутствуют обе границы по зарплате
    """
    return Vacancy("12345", "Developer", "https://hh.ru/vacancy/12345", "description", {"from": 120000, "to": 150000})


@pytest.fixture
def vacancy2():
    """
    Фикстура экземпляра класса Vacancy - 2
    Зарплата передается как число
    """
    return Vacancy("123456", "PHP Developer", "https://hh.ru/vacancy/123456", "description", 140000)


@pytest.fixture
def vacancy3():
    """
    Фикстура экземпляра класса Vacancy - 3
    Зарплата передается как текст
    """
    return Vacancy("1234567", "Python Developer", "https://hh.ru/vacancy/1234567", "description", "130000")


@pytest.fixture
def vacancy4():
    """
    Фикстура экземпляра класса Vacancy - 4
    Зарплата отсутствует
    """
    return Vacancy("12345678", "PL/SQL Developer", "https://hh.ru/vacancy/12345678", "description", None)


@pytest.fixture
def vacancy5():
    """
    Фикстура экземпляра класса Vacancy - 5
    Присутствуют только верхняя граница по зарплате
    """
    return Vacancy(
        "123456789", "PL/SQL Developer", "https://hh.ru/vacancy/123456789", "description", {"from": None, "to": 150000}
    )


@pytest.fixture
def vacancy6():
    """
    Фикстура экземпляра класса Vacancy - 6
    Присутствуют только нижняя граница по зарплате
    """
    return Vacancy(
        "1234567890",
        "PL/SQL Developer",
        "https://hh.ru/vacancy/1234567890",
        "description",
        {"from": 150000, "to": None},
    )


@pytest.fixture
def vacancy7():
    """
    Фикстура экземпляра класса Vacancy - 7
    Нижняя граница по зарплате больше верхней
    """
    return Vacancy(
        "12345678901",
        "PL/SQL Developer",
        "https://hh.ru/vacancy/12345678901",
        "description",
        {"from": 150000, "to": 130000},
    )


@pytest.fixture
def vacancy8():
    """
    Фикстура экземпляра класса Vacancy - 8
    Зарплата передается как текст, но в тексте не число
    """
    return Vacancy("12345789012", "Developer", "https://hh.ru/vacancy/12345678901", "description", "test")


@pytest.fixture
def vacancy9():
    """
    Фикстура экземпляра класса Vacancy - 9
    Зарплата не корректного типа
    """
    return Vacancy("123457890123", "Developer", "https://hh.ru/vacancy/123457890123", "description", [])


@pytest.fixture
def vacancy10():
    """
    Фикстура экземпляра класса Vacancy - 10
    Некорректный тект url
    """
    return Vacancy("1234578901234", "Developer", "test", "description", {"from": 120000, "to": 150000})


@pytest.fixture
def vacancy11():
    """
    Фикстура экземпляра класса Vacancy - 11
    Некорректный url - не тект
    """
    return Vacancy("1234578901234", "Developer", 123, "description", {"from": 120000, "to": 150000})


@pytest.fixture
def json_vacancies1():
    """
    Фикстура списка вакансий в JSON формате - 1
    """
    data_vacancies = """
        [
            {
                "id": "12345",
                "name": "Developer",
                "alternate_url": "https://hh.ru/vacancy/12345",
                "description": "Python Developer",
                "salary": {"from": 120000, "to": 150000}
            },
            {
                "id": "123456",
                "name": "PHP Developer",
                "alternate_url": "https://hh.ru/vacancy/123456",
                "description": "Python Developer",
                "salary": 130000
            }
        ]
    """
    json_vacancies_str = json.loads(data_vacancies)
    return json.dumps(json_vacancies_str)


@pytest.fixture
def json_vacancies2():
    """
    Фикстура списка вакансий в JSON формате - 2
    """
    data_vacancies = """
        [
            {
                "id": "125598563",
                "name": "Бизнес-аналитик",
                "alternate_url": "https://hh.ru/vacancy/125598563",
                "description": "Ищем джуниор-специалистов, которые помогут нам создавать продукты и сервисы",
                "salary": null
            },
            {
                "id": "92752367",
                "name": "Менеджер по продажам недвижимости",
                "alternate_url": "https://hh.ru/vacancy/92752367",
                "description": "Анализ рынка и объектов недвижимости. Предварительная оценка недвижимости.",
                "salary": {"from": 50000, "to": 60000}
            },
            {
                "id": "12345",
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/12345",
                "description": "Python Developer",
                "salary": {"from": 120000, "to": 150000}
            }
        ]
    """
    json_vacancies_str = json.loads(data_vacancies)
    return json.dumps(json_vacancies_str)
