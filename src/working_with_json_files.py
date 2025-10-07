import json
import os

import src.utils as utils
from src.base_working_with_files import BaseWorkingWithFiles


class WorkingWithJsonFiles(BaseWorkingWithFiles):
    """
    Класс для работы с JSON-файлами
    """

    def __init__(self, file_name: str = "my_json_file.json") -> None:
        """
        Инициализация класса для работы с JSON-файлами
        """
        # Получаем путь к директории, где находится main.py
        current_dir = os.path.dirname(__file__)

        # Создаем путь к папке data, которая находится на том же уровне, что и src
        # os.path.join() безопаснее для работы с разными операционными системами
        data_dir = os.path.join(current_dir, "..", "data")

        # Полный путь к файлу
        config_file_path = os.path.join(data_dir, file_name)
        self.__file_name = config_file_path

    def getting_data(self) -> list[dict]:
        """
        Метод получения данных из JSON-файла
        return: список словарей
        """
        try:
            # Открываем файл для чтения
            with open(self.__file_name, "r", encoding="utf-8") as file:
                # Загружаем данные из файла в виде списка словарей
                return json.load(file)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден по пути {self.__file_name}")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка: Некорректный формат JSON в файле {self.__file_name}")
            return []
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return []

    def adding_data(self, new_data: list[dict], key_str: str) -> None:
        """
        Метод добавления данных в JSON-файл
        :param new_data: - список словарей для добавленияв в файл
        :param key_str: - ключ словаря для определения уникальности записи
        :return: None
        """
        # Загружаем существующие данные из файла
        data = self.getting_data()
        print(data)

        # Добавляем новые данные
        merge_list = utils.merging_dictionary_lists(data, new_data, key_str)

        # Записываем обновленные данные обратно в файл
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(merge_list, file, ensure_ascii=False, indent=4)

    def deleting_data(self):
        """Метод удаления данных из JSON-файла"""
        with open(self.__file_name, "w", encoding="utf-8") as file:
            file.truncate(0)  # Обрезает файл до нулевого размера, очищая его содержимое
