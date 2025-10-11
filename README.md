# Проект "job_search" - Поиск вакансий

## Описание:
 Проект "job_search" - это проект на Python, 
 осуществляющий поиск вакансий на hh.ru
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/job_search.git
 
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
  
 ### class BaseAPI(ABC): ###
    """
    Абстрактный класс для работы с api
    """

    @abstractmethod
    def _load_vacancies(self, keyword: str) -> None:
        """
        Абстрактный приватный метод для подключения к api
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """


    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Абстрактный метод для получения вакансий
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """


 ### class BaseVacancy(ABC):###
    """
    Абстрактный класс вакансий
    """

    __slots__ = ["id_vacancy", "name", "url", "description", "salary"]

    @abstractmethod
    def __init__(self, id_vacancy: str, name: str, url: str, description: str, salary: Optional[Any]):
    
    @classmethod
    @abstractmethod
    def sorted_by_salary(cls, is_reverse=True) -> None:
        """
        Абстрактные Class метод для сортировки объектов Vacancy по зарплате
        :return: None
        """

    @classmethod
    @abstractmethod
    def top_n_salary(cls, n: int) -> list[dict]:
        """
        Абстрактный Class метод возвращает тор n вакансий по зарплате
        :param n: количество вакансий с наибольшей зарплатой
        :return: список из n словарей вакансий с наибольшими зарплатами
        """


### class BaseWorkingWithFiles(ABC):### 
    """
    Абстрактный класс для работы с файлами
    """

    def __init__(self, file_name: str) -> None:
        pass

    @abstractmethod
    def getting_data(self) -> list[dict]:
        """Метод получения данных из файла"""

    @abstractmethod
    def adding_data(self, new_data: list[dict], key_str: str):
        """Метод добавления данных в файл"""

    @abstractmethod
    def deleting_data(self):
        """Метод удаления данных из файла"""


### class HeadHunterAPI(BaseAPI):### 
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
        
    def _load_vacancies(self, keyword: str) -> None:
        """
        Приватный метод получения списка вакансий
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
    
    def get_vacancies(self, keyword: str) -> Any:
        """
        Публичный метод получения вакансий в формате JSON
        :param keyword: строка - запрос для поиска вакансий
        :return: None
        """
    
    def __load_vacancy_description(self, id_vacance: str) -> None:
        """
        Приватный метод получения полной информации по id вакансии
        :param id_vacance: строка - id вакансии
        :return: None
        """
    
    def get_vacancy_description(self, id_vacance: str) -> Any:
        """
        Публичный метод получения полной информации по id вакансии в формате JSON
        :param id_vacance: строка - id вакансии
        :return: None
        """

    
### class Vacancy(BaseVacancy):### 
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
    
    def __str__(self):
        """
        Представление объекта Vacancy в текстовом виде
        """

    def __validate_salary(self, salary):
        """
        Валидация вакансии по зарплате
        """
    
    def __validate_url(self, url):
        """
        Валидация вакансии по url
        """
    
    def __eq__(self, other):
        """
        Проверка на равенство по зарплате
        """
    
    def __ne__(self, other):
        """
        Проверка на не равенство по зарплате
        """
    
    def __lt__(self, other):
        """
        Проверка когда первый объект меньше второго по зарплате
        """
    
    def __le__(self, other):
        """
        Проверка когда первый объект меньше или равен второму по зарплате
        """
    
    def __gt__(self, other):
        """
        Проверка когда первый объект больше второго по зарплате
        """

    def __ge__(self, other):
        """
        Проверка когда первый объект больше или равен второго по зарплате
        """
    
    @classmethod
    def cast_to_object_list(cls, json_vacancies) -> None:
        """
        Class метод для преобразования набора данных из JSON в список объектов Vacancy
        :param json_vacancies: JSON с вакансиями
        :return: None
        """
    
    @classmethod
    def sorted_by_salary(cls, is_reverse=True) -> None:
        """
        Class метод для сортировки объектов Vacancy по зарплате
        :return: None
        """
    
    @classmethod
    def top_n_salary(cls, n: int) -> list[dict]:
        """
        Class метод возвращает тор n вакансий по зарплате
        :param n: количество вакансий с наибольшей зарплатой
        :return: список из n словарей вакансий с наибольшими зарплатами
        """
    
    @classmethod
    def filter_by_salary(cls, salary_from: int, salary_to: int) -> list[dict]:
        """
        Class метод для фильтрации объектов Vacancy по зарплате
        :param salary_from: нижняя граница зарплаты
        :param salary_to: верняя граница зарплаты
        :return: None
        """
    
    @classmethod
    def filter_by_words(cls, words: str) -> list[dict]:
        """
        Class метод для фильтрации объектов Vacancy по тексту в описании
        :param words: строка для фильтрации
        :return: None
        """


### class WorkingWithJsonFiles(BaseWorkingWithFiles):### 
    """
    Класс для работы с JSON-файлами
    """

    def __init__(self, file_name: str = "my_json_file.json") -> None:
        """
        Инициализация класса для работы с JSON-файлами
        """
    
    def getting_data(self) -> list[dict]:
        """
        Метод получения данных из JSON-файла
        return: список словарей
        """
    
    def adding_data(self, new_data: list[dict], key_str: str) -> None:
        """
        Метод добавления данных в JSON-файл
        :param new_data: - список словарей для добавленияв в файл
        :param key_str: - ключ словаря для определения уникальности записи
        :return: None
        """
    
    def deleting_data(self):
        """Метод удаления данных из JSON-файла"""


###Функция def merging_dictionary_lists###(data: list[dict], new_data: list[dict], key_str: str) -> list[dict]:
    """
    Функция объединения списков словарей
    :param data: первый список словарей
    :param new_data: второй список словарей
    :param key_str: ключ по которому сравниваются списки словарей
    :return: список словарей
    """


###def sort_dictionary_lists###(data: list[dict], params: list, is_reverse=True) -> list[dict]:
    """
    Функция сортировки списка словарей
    :param data: список словарей
    :param params: список ключей, для сортировки
    :return: список словарей
    """


 ## Тестирование:
Проект покрыт тестами фреймворка pytest. Для их запуска выполните команду:
```
pytest
```
Для выгрузки отчета о покрытии проекта тестами выполните команду:
```
pytest --cov=src --cov-report=html
```


 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 