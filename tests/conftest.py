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


@pytest.fixture
def top_2_vacansies():
    """
    Фикстура топ 2 вакансии сс самыми высокими зарплатами
    """
    return """id: 12345 Python Developer 120000-150000 руб. url: https://hh.ru/vacancy/12345
id: 92752367 Менеджер по продажам недвижимости 50000-60000 руб. url: https://hh.ru/vacancy/92752367"""


@pytest.fixture
def list_vacansies_obj1():
    """
    Фикстура со списком экземпляров класса Vacancy - 1
    """
    return [
        Vacancy(
            "122493254",
            "Senior Python разработчик",
            "https://hh.ru/vacancy/122493254",
            "Опыт коммерческой разработки на Python от 3-х лет.",
            {"from": 150000, "to": 240000},
        ),
        Vacancy(
            "125456182",
            "Middle Python разработчик",
            "https://hh.ru/vacancy/125456182",
            "Писать back-end и API. Linux (настройка окружения)",
            {"from": 200000, "to": 200000},
        ),
        Vacancy(
            "126176500",
            "Middle Python разработчик",
            "https://hh.ru/vacancy/126176500",
            "Уверенное знание Python. Фундаментальные знания в области информационных технологий.",
            {"from": 0, "to": 0},
        ),
        Vacancy(
            "125538232",
            "Middle Backed Python разработчик",
            "https://hh.ru/vacancy/125538232",
            "Опыт разработки на Python от 2–3 лет, уверенное знание языка и его экосистемы.",
            {"from": 0, "to": 0},
        ),
        Vacancy(
            "125962759",
            "MPython разработчик Middle+",
            "https://hh.ru/vacancy/125962759",
            "Опыт разработки на Python 3.10+ в production-разработке.",
            {"from": 150000, "to": 200000},
        ),
        Vacancy(
            "125799412",
            "Python разработчик",
            "https://hh.ru/vacancy/125799412",
            "Опыт работы с MLFlow (или любым другим open source решением, где бук на python)",
            {"from": 0, "to": 0},
        ),
    ]


@pytest.fixture
def list_vacansies_obj2():
    """
    Фикстура со списком экземпляров класса Vacancy - 2
    """
    return [
        Vacancy(
            "126071783",
            "Ведущий python разработчик",
            "https://hh.ru/vacancy/126071783",
            "Хорошие знания и навыки в написании сервисов на Python.",
            {"from": 0, "to": 0},
        ),
        Vacancy(
            "125962759",
            "MPython разработчик Middle+",
            "https://hh.ru/vacancy/125962759",
            "Опыт разработки на Python 3.10+ в production-разработке.",
            {"from": 150000, "to": 200000},
        ),
    ]


@pytest.fixture
def list_dict_vacansies1():
    """
    Фикстура со списком словарей с вакансиями - 1
    """
    return [
        {
            "id": "122493254",
            "name": "Senior Python разработчик",
            "url": "https://hh.ru/vacancy/122493254",
            "description": "Опыт коммерческой разработки на Python от 3-х лет.",
            "salary": {"from": 150000, "to": 240000},
        },
        {
            "id": "125456182",
            "name": "Middle Python разработчик",
            "url": "https://hh.ru/vacancy/125456182",
            "description": "Писать back-end и API. Linux (настройка окружения)",
            "salary": {"from": 200000, "to": 200000},
        },
        {
            "id": "126176500",
            "name": "Python разработчик",
            "url": "https://hh.ru/vacancy/126176500",
            "description": "Уверенное знание Python. Фундаментальные знания в области информационных технологий.",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125538232",
            "name": "Middle Backed Python разработчик",
            "url": "https://hh.ru/vacancy/125538232",
            "description": "Опыт разработки на Python от 2–3 лет, уверенное знание языка и его экосистемы.",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125962759",
            "name": "Python разработчик Middle+",
            "url": "https://hh.ru/vacancy/125962759",
            "description": "Опыт разработки на Python 3.10+ в production-разработке.",
            "salary": {"from": 150000, "to": 200000},
        },
        {
            "id": "125799412",
            "name": "Python разработчик",
            "url": "https://hh.ru/vacancy/125799412",
            "description": "Опыт работы с MLFlow (или любым другим open source решением, где бук на python)",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125799412",
            "name": "Python разработчик",
            "url": "https://hh.ru/vacancy/125799412",
            "description": "Опыт работы с MLFlow (или любым другим open source решением, где бук на python)",
            "salary": {"from": 0, "to": 0},
        },
    ]


@pytest.fixture
def list_dict_vacansies2():
    """
    Фикстура со списком словарей с вакансиями - 2
    """
    return [
        {
            "id": "126071783",
            "name": "Ведущий python разработчик",
            "url": "https://hh.ru/vacancy/126071783",
            "description": "Хорошие знания и навыки в написании сервисов на Python.",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125962759",
            "name": "Python разработчик Middle+",
            "url": "https://hh.ru/vacancy/125962759",
            "description": "Опыт разработки на Python 3.10+ в production-разработке. Опыт работы с БД.",
            "salary": {"from": 170000, "to": 200000},
        },
    ]


@pytest.fixture
def list_dict_vacansies3():
    """
    Фикстура со списком словарей с вакансиями - 3
    """
    return [
        {
            "id": "122493254",
            "name": "Senior Python разработчик",
            "url": "https://hh.ru/vacancy/122493254",
            "description": "Опыт коммерческой разработки на Python от 3-х лет.",
            "salary": {"from": 150000, "to": 240000},
        },
        {
            "id": "125456182",
            "name": "Middle Python разработчик",
            "url": "https://hh.ru/vacancy/125456182",
            "description": "Писать back-end и API. Linux (настройка окружения)",
            "salary": {"from": 200000, "to": 200000},
        },
        {
            "id": "126176500",
            "name": "Python разработчик",
            "url": "https://hh.ru/vacancy/126176500",
            "description": "Уверенное знание Python. Фундаментальные знания в области информационных технологий.",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125538232",
            "name": "Middle Backed Python разработчик",
            "url": "https://hh.ru/vacancy/125538232",
            "description": "Опыт разработки на Python от 2–3 лет, уверенное знание языка и его экосистемы.",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "125962759",
            "name": "Python разработчик Middle+",
            "url": "https://hh.ru/vacancy/125962759",
            "description": "Опыт разработки на Python 3.10+ в production-разработке.",
            "salary": {"from": 150000, "to": 200000},
        },
        {
            "id": "125799412",
            "name": "Python разработчик",
            "url": "https://hh.ru/vacancy/125799412",
            "description": "Опыт работы с MLFlow (или любым другим open source решением, где бук на python).",
            "salary": {"from": 0, "to": 0},
        },
        {
            "id": "126071783",
            "name": "Ведущий python разработчик",
            "url": "https://hh.ru/vacancy/126071783",
            "description": "Хорошие знания и навыки в написании сервисов на Python.",
            "salary": {"from": 0, "to": 0},
        },
    ]


@pytest.fixture
def list_dict_vacansies4():
    """
    Фикстура со списком словарей с вакансиями - 4
    """
    return [
        {
            "id": "126071783",
            "name": "Ведущий python разработчик",
            "url": "https://hh.ru/vacancy/126071783",
            "description": "Хорошие знания и навыки в написании сервисов на Python.",
            "salary": {"from": 0, "to": 0},
            "test": {"1": {"1": 1}},
        },
        {
            "id": "125962759",
            "name": "Python разработчик Middle+",
            "url": "https://hh.ru/vacancy/125962759",
            "description": "Опыт разработки на Python 3.10+ в production-разработке. Опыт работы с БД.",
            "salary": {"from": 170000, "to": 200000},
            "test": {"1": {"1": 9}},
        },
    ]
