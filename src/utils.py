def merging_dictionary_lists(data: list[dict], new_data: list[dict], key_str: str) -> list[dict]:
    """
    Функция объединения списков словарей
    :param data: первый список словарей
    :param new_data: второй список словарей
    :param key_str: ключ по которому сравниваются списки словарей
    :return: список словарей
    """
    merge_list: list[dict] = []
    for i in data:
        if len(merge_list) == 0:
            merge_list.append(i)
        else:
            is_in_list = False
            for index, item in enumerate(merge_list):
                if item.get(key_str) == i.get(key_str):
                    merge_list[index] = i
                    is_in_list = True

            if not is_in_list:
                merge_list.append(i)

    for i in new_data:
        if len(merge_list) == 0:
            merge_list.append(i)
        else:
            is_in_list = False
            for index, item in enumerate(merge_list):
                if item.get(key_str) == i.get(key_str):
                    merge_list[index] = i
                    is_in_list = True

            if not is_in_list:
                merge_list.append(i)

    return merge_list


def sort_dictionary_lists(data: list[dict], params: list, is_reverse=True) -> list[dict]:
    """
    Функция сортировки списка словарей
    :param data: список словарей
    :param params: список ключей, для сортировки
    :return: список словарей
    """
    # Сортировка по ключу/ключам
    if len(params) == 0:
        return data
    elif len(params) == 1:
        sorted_list = sorted(data, key=lambda x: x.get(params[0], None), reverse=is_reverse)  # type: ignore
        return sorted_list
    elif len(params) == 2:
        sorted_list = sorted(
            data, key=lambda x: x.get(params[0], None).get(params[1], None), reverse=is_reverse  # type: ignore
        )
        return sorted_list
    elif len(params) == 3:
        sorted_list = sorted(
            data,
            key=lambda x: x.get(params[0], None).get(params[1], None).get(params[2], None),  # type: ignore
            reverse=is_reverse,  # type: ignore
        )
        return sorted_list
    else:
        return data
