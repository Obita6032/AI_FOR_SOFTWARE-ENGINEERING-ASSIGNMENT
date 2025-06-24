def sort_dicts_by_key_manual(data, key):
    sorted_list = []
    for item in data:
        inserted = False
        for i, sorted_item in enumerate(sorted_list):
            if item[key] < sorted_item[key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list
