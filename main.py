from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.working_with_json_files import WorkingWithJsonFiles


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем
    """
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    print("Добро пожаловать!")
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies_json = hh_api.get_vacancies(search_query)

    # Конвертирование JSON-вакансий в объекты Vacancy
    Vacancy.cast_to_object_list(hh_vacancies_json)

    # Запрашиваем фильтры по зарплате
    salary_from = int(input("Введите нижнюю границу для фильтрации по зарплате:"))
    salary_to = int(input("Введите верхнюю границу для фильтрации по зарплате:"))
    filtered_by_salary = Vacancy.filter_by_salary(salary_from, salary_to)
    print("Отобрано вакансий:", len(filtered_by_salary))

    # Фильтрация по описанию
    words = input("\nВведите текст для фильтрации по описанию: ")
    filtered_by_words = Vacancy.filter_by_words(words)
    print("Отобрано вакансий:", len(filtered_by_words))

    # Отбираем топ-N вакансий по зарплате
    top_n = int(input("\nВведите количество вакансий для вывода в топ N: "))
    top_vacancy = Vacancy.top_n_salary(top_n)
    print("Отобрано вакансий:", len(top_vacancy))

    # Сохранение результатов в файл
    is_save = input("\nСохранить выбранные вакансии в файл? (y/n): ")
    if is_save == "y":
        # Формирование списка объектов Vacancy в виде словарей
        saved_vacancies = [
            {
                "id": vacancy.id_vacancy,  # type: ignore
                "name": vacancy.name,  # type: ignore
                "url": vacancy.url,  # type: ignore
                "description": vacancy.description,  # type: ignore
                "salary": vacancy.salary,  # type: ignore
            }
            for vacancy in top_vacancy
        ]

        # Сохраняем данные в JSON-файл
        saved = WorkingWithJsonFiles(f"vacancy_hh_{search_query}.json")
        saved.adding_data(saved_vacancies, "id")
        print("Данные сохранены.")


if __name__ == "__main__":
    user_interaction()
