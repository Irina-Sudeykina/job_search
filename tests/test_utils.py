import src.utils as utils


def test_merging_dictionary_lists(list_dict_vacansies1, list_dict_vacansies2, list_dict_vacansies3) -> None:
    """
    Тестирование метода getting_data класса WorkingWithJsonFiles
    :param list_dict_vacansies1: - Фикстура со списком словарей с вакансиями - 1
    :param list_dict_vacansies2: - Фикстура со списком словарей с вакансиями - 2
    :param list_dict_vacansies3: - Фикстура со списком словарей с вакансиями - 3
    :return: None
    """
    result = utils.merging_dictionary_lists(list_dict_vacansies1, list_dict_vacansies2, "id")

    assert len(result) == len(list_dict_vacansies3)


def test_sort_dictionary_lists(list_dict_vacansies1, list_dict_vacansies4) -> None:
    """
    Тестирование метода sort_dictionary_lists класса WorkingWithJsonFiles
    :param list_dict_vacansies1: - Фикстура со списком словарей с вакансиями - 1
    :param list_dict_vacansies4: - Фикстура со списком словарей с вакансиями - 4
    :return: None
    """
    assert list_dict_vacansies1[0]["id"] != "125456182"

    sorted_list = utils.sort_dictionary_lists(list_dict_vacansies1, [])
    assert sorted_list[0]["id"] == "122493254"

    sorted_list = utils.sort_dictionary_lists(list_dict_vacansies1, ["test", "1", "1", "1"])
    assert sorted_list[0]["id"] == "122493254"

    sorted_list = utils.sort_dictionary_lists(list_dict_vacansies1, ["description"])
    assert sorted_list[0]["id"] == "126176500"

    sorted_list = utils.sort_dictionary_lists(list_dict_vacansies1, ["salary", "from"])
    assert sorted_list[0]["id"] == "125456182"

    assert list_dict_vacansies4[0]["id"] != "125962759"
    sorted_list = utils.sort_dictionary_lists(list_dict_vacansies4, ["test", "1", "1"])
    assert sorted_list[0]["id"] == "125962759"
