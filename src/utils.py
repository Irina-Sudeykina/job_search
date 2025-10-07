def merging_dictionary_lists(data: list[dict], new_data: list[dict], key_str: str) -> list[dict]:
    merge_list: list[dict] = []
    for i in data:
        if len(merge_list) == 0:
            merge_list.append(i)
        else:
            for index, item in enumerate(merge_list):
                if item.get(key_str) == i.get(key_str):
                    merge_list[index] = i

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
    # Сортировка по ключу/ключам
    if len(params) == 0:
        return data
    elif len(params) == 1:
        sorted_list = sorted(data, key=lambda x: x[params[0]], reverse=is_reverse)
        return sorted_list
    elif len(params) == 2:
        sorted_list = sorted(data, key=lambda x: x[params[0]][params[1]], reverse=is_reverse)
        return sorted_list
    elif len(params) == 3:
        sorted_list = sorted(data, key=lambda x: x[params[0]][params[1]][params[2]], reverse=is_reverse)
        return sorted_list
    else:
        return data
