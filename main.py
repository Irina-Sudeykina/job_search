import json

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    # hh_vacancies_json = hh_api.get_vacancies("Python")

    # Парсим строку JSON в словарь
    # hh_vacancies = json.loads(hh_vacancies_json)

    # Распечатываем первую вакансию
    # print(hh_vacancies[0])

    # Берём ID первой вакансии
    # id_vacancy = hh_vacancies[0].get("id")

    # Получаем полную информацию по вакансии
    hh_vacancy_description = hh_api.get_vacancy_description("125598563")
    print(type(hh_vacancy_description))
    print(hh_vacancy_description)

    vacancy1 = Vacancy(
        "12345", "Developer", "https://hh.ru/vacancy/12345", "description", {"from": 120000, "to": 150000}
    )
    print(vacancy1.name)

    vacancy2 = Vacancy("123456", "PHP Developer", "https://hh.ru/vacancy/123456", "description", 0)
    print(vacancy2.name)

    print(len(Vacancy.instances))

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
    print(type(json_vacancies_str))
    json_vacancies = json.dumps(json_vacancies_str)
    print(type(json_vacancies))

    Vacancy.cast_to_object_list(json_vacancies)
    print(len(Vacancy.instances))
    print(Vacancy.instances[0])


if __name__ == "__main__":
    user_interaction()
