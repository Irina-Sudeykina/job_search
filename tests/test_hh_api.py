import json
from unittest.mock import Mock, patch

from src.hh_api import HeadHunterAPI


def test_hh_api_init(head_hunter_api) -> None:
    """
    Проверка инициации экземпляра сласса HeadHunterAPI
    :param head_hunter_api: фикстура экземпляра класса HeadHunterAPI
    :return: Ничего не возвращает
    """

    assert head_hunter_api.url == "https://api.hh.ru/vacancies"
    assert head_hunter_api.headers == {"User-Agent": "HH-User-Agent"}
    assert head_hunter_api.params == {"text": "", "page": 0, "per_page": 100}
    assert head_hunter_api.vacancies == []


def test_load_vacancies() -> None:
    """
    Проверка метода _load_vacancies сласса HeadHunterAPI
    :return: Ничего не возвращает
    """

    with patch("requests.get") as mock_get:
        hh_api = HeadHunterAPI()

        # Фиктивный ответ сервера
        fake_response = {
            "items": [
                {"name": "Python Developer", "salary": {"from": 80000}},
                {"name": "Data Scientist", "salary": {"from": 100000}},
            ]
        }

        # Настройка поведения mock-запросов
        mock_response = Mock()
        mock_response.json.return_value = fake_response
        mock_get.return_value = mock_response

        # Загрузка вакансий
        hh_api._load_vacancies("Developer")

        # Проверка первого вызова (первоначальные параметры)
        expected_params_first_call = {"text": "Developer", "page": 20, "per_page": 100}
        first_call_args = mock_get.call_args_list[0][1]["params"]
        assert first_call_args == expected_params_first_call

        # Количество вызовов должно соответствовать числу выполненных попыток
        num_calls = len(mock_get.call_args_list)
        assert num_calls >= 1  # Должен быть минимум один вызов

        # Последняя попытка (после обновления страницы)
        final_expected_params = {"text": "Developer", "page": 20, "per_page": 100}
        last_call_args = mock_get.call_args_list[-1][1]["params"]
        assert last_call_args == final_expected_params

        # Проверка наличия загруженных вакансий
        assert len(hh_api.vacancies) == 40


@patch("requests.get")
def test_get_vacancies(mock_get) -> None:
    """
    Проверка метода get_vacancies сласса HeadHunterAPI
    :return: Ничего не возвращает
    """

    hh_api = HeadHunterAPI()

    # Установка значения списка вакансий вручную
    hh_api._HeadHunterAPI__vacancies = [{"name": "Python Developer"}, {"name": "JavaScript Developer"}]  # type: ignore

    # Получение вакансий
    result = hh_api.get_vacancies("Developer")

    # Преобразование результата обратно в объект Python
    parsed_result = json.loads(result)

    # Проверка формата и содержания результата
    assert isinstance(parsed_result, list)
    assert len(parsed_result) == 2
    assert {"name": "Python Developer"} in parsed_result
    assert {"name": "JavaScript Developer"} in parsed_result
