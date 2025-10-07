import builtins
import os

from src.working_with_json_files import WorkingWithJsonFiles


def test_getting_data():
    # Тестируем успешное считывание данных
    wjf = WorkingWithJsonFiles("existing_file.json")
    existing_data = wjf.getting_data()
    assert type(existing_data) == list
    assert len(existing_data) > 0, "Файл не содержит данных"

    # Тестируем попытку прочитать несуществующий файл
    non_existing_wjf = WorkingWithJsonFiles("nonexistent_file.json")
    empty_data = non_existing_wjf.getting_data()
    assert empty_data == []


def test_adding_data():
    # Данные для тестирования
    new_data = [{"id": "new_id", "name": "New Name"}, {"id": "another_new_id", "name": "Another New Name"}]

    # Инстанцируем класс
    wjf = WorkingWithJsonFiles("test_file.json")

    # Сначала очистим файл
    wjf.deleting_data()

    # Добавляем данные
    wjf.adding_data(new_data, "id")

    # Чтение обновленных данных
    updated_data = wjf.getting_data()

    # Проверка наличия новых записей
    assert any(item["id"] == "new_id" for item in updated_data), "Новая запись не была добавлена"
    assert any(item["id"] == "another_new_id" for item in updated_data), "Вторая новая запись не была добавлена"

    # Удаляем созданный временный файл
    os.remove(wjf._WorkingWithJsonFiles__file_name)


def test_deleting_data():
    # Инстанцируем класс
    wjf = WorkingWithJsonFiles("delete_test_file.json")

    # Сначала заполним файл какими-нибудь данными
    initial_data = [{"id": "initial_id", "name": "Initial Name"}]
    wjf.adding_data(initial_data, "id")

    # Проверяем наличие данных
    before_delete = wjf.getting_data()
    assert len(before_delete) > 0

    # Очищаем файл
    wjf.deleting_data()

    # Читаем файл заново
    after_delete = wjf.getting_data()
    assert after_delete == []

    # Удаляем созданный временный файл
    os.remove(wjf._WorkingWithJsonFiles__file_name)


def test_getting_data_exception(monkeypatch, capsys):
    """
    Тестирует реакцию метода getting_data на общее исключение при доступе к файлу
    """
    # Монкипатчим функцию open(), заставляя её выдавать произвольное исключение
    monkeypatch.setattr(
        builtins, "open", lambda *args, **kwargs: (_ for _ in ()).throw(Exception("Искусственный сбой"))
    )

    # Инстанцируем класс
    wjf = WorkingWithJsonFiles("fake_file.json")

    # Получаем данные и смотрим результат
    result = wjf.getting_data()

    # Проверяем, что сообщение об ошибке появилось в консоли
    captured_output = capsys.readouterr().out
    assert "Произошла ошибка при чтении файла:" in captured_output, "Сообщение об ошибке не найдено"

    # Проверяем, что результат - пустой список
    assert result == [], "Возвращаемый результат должен быть пустым списком"
