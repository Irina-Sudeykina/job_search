from src.vacancy import Vacancy


def test_vacancy_init(
    vacancy1, vacancy2, vacancy3, vacancy4, vacancy5, vacancy6, vacancy7, vacancy8, vacancy9, vacancy10, vacancy11
) -> None:
    """
    Проверка инициации экземпляра класса Vacancy
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :param vacancy3: фикстура экземпляра класса Vacancy - 3 Зарплата передается как текст
    :param vacancy4: фикстура экземпляра класса Vacancy - 4 Зарплата отсутствует
    :param vacancy5: фикстура экземпляра класса Vacancy - 5 Присутствуют только верхняя граница по зарплате
    :param vacancy6: фикстура экземпляра класса Vacancy - 6 Присутствуют только нижняя граница по зарплате
    :param vacancy7: фикстура экземпляра класса Vacancy - 7 Нижняя граница по зарплате больше верхней
    :param vacancy8: фикстура экземпляра класса Vacancy - 8 Зарплата передается как текст, но в тексте не число
    :param vacancy9: фикстура экземпляра класса Vacancy - 9 Зарплата не корректного типа
    :param vacancy10: фикстура экземпляра класса Vacancy - 10 Некорректный тект url
    :param vacancy11: фикстура экземпляра класса Vacancy - 11 Некорректный url - не тект
    :return: Ничего не возвращает
    """
    assert vacancy1.id_vacancy == "12345"
    assert vacancy1.name == "Developer"
    assert vacancy1.url == "https://hh.ru/vacancy/12345"
    assert vacancy1.description == "description"
    assert vacancy1.salary == {"from": 120000, "to": 150000}

    assert vacancy2.id_vacancy == "123456"
    assert vacancy2.name == "PHP Developer"
    assert vacancy2.url == "https://hh.ru/vacancy/123456"
    assert vacancy2.description == "description"
    assert vacancy2.salary == {"from": 140000, "to": 140000}

    assert vacancy3.salary == {"from": 130000, "to": 130000}
    assert vacancy4.salary == {"from": 0, "to": 0}
    assert vacancy5.salary == {"from": 75000, "to": 150000}
    assert vacancy6.salary == {"from": 150000, "to": 150000}
    assert vacancy7.salary == {"from": 130000, "to": 150000}
    assert vacancy8.salary == {"from": 0, "to": 0}
    assert vacancy9.salary == {"from": 0, "to": 0}

    assert vacancy10.url == "https://hh.ru/vacancy"
    assert vacancy11.url == "https://hh.ru/vacancy"


def test_vacancy_str(vacancy1) -> None:
    """
    Проверка текстового представлени класса Vacancy
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :return: Ничего не возвращает
    """
    assert str(vacancy1) == "id: 12345 Developer 120000-150000 руб. url: https://hh.ru/vacancy/12345"


def test_vacancy_eq(vacancy1, vacancy10) -> None:
    """
    Проверка на равенство по зарплате класса Vacancy
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy10: фикстура экземпляра класса Vacancy - 10 Некорректный тект url
    :return: Ничего не возвращает
    """
    assert vacancy1 == vacancy10
    assert vacancy1 == 120000

    try:
        assert vacancy1 == "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_vacancy_ne(vacancy1, vacancy2) -> None:
    """
    Проверка на не равенство по зарплате класса Vacancy
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :return: Ничего не возвращает
    """
    assert vacancy1 != vacancy2
    assert vacancy1 != 1

    try:
        assert vacancy1 != "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_vacancy_lt(vacancy1, vacancy2) -> None:
    """
    Проверка когда первый экземпляр класса Vacancy меньше второго по зарплате
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :return: Ничего не возвращает
    """
    assert vacancy1 < vacancy2
    assert vacancy1 < 160000

    try:
        assert vacancy1 < "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_vacancy_le(vacancy1, vacancy2) -> None:
    """
    Проверка когда первый экземпляр класса Vacancy меньше или равен второму по зарплате
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :return: Ничего не возвращает
    """
    assert vacancy1 <= vacancy2
    assert vacancy1 <= 160000
    assert vacancy1 <= 120000

    try:
        assert vacancy1 <= "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_vacancy_gt(vacancy1, vacancy2) -> None:
    """
    Проверка когда первый экземпляр класса Vacancy больше второго по зарплате
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :return: Ничего не возвращает
    """
    assert vacancy2 > vacancy1
    assert vacancy2 > 1

    try:
        assert vacancy1 > "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_vacancy_ge(vacancy1, vacancy2) -> None:
    """
    Проверка когда первый экземпляр класса Vacancy больше или равен второму по зарплате
    :param vacancy1: фикстура экземпляра класса Vacancy - 1 Присутствуют обе границы по зарплате
    :param vacancy2: фикстура экземпляра класса Vacancy - 2 Зарплата передается как число
    :return: Ничего не возвращает
    """
    assert vacancy2 >= vacancy1
    assert vacancy2 >= 1
    assert vacancy2 >= 140000

    try:
        assert vacancy1 >= "test"
    except TypeError as e:
        assert str(e) == "Сравнение невозможно"


def test_cast_to_object_list(json_vacancies1, json_vacancies2) -> None:
    """
    Проверка преобразования набора данных из JSON в список объектов Vacancy
    :param json_vacancies1: Фикстура списка вакансий в JSON формате - 1
    :param json_vacancies2: Фикстура списка вакансий в JSON формате - 2
    :return: Ничего не возвращает
    """
    del Vacancy.instances[:]
    assert len(Vacancy.instances) == 0

    Vacancy.cast_to_object_list(json_vacancies1)

    assert len(Vacancy.instances) == 2

    Vacancy.cast_to_object_list(json_vacancies2)

    assert len(Vacancy.instances) == 4
