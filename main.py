from src.hh_api import HeadHunterAPI


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")
    print(hh_vacancies)


if __name__ == "__main__":
    user_interaction()
