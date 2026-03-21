def flatten(nested_list: list) -> list:
    if not isinstance(nested_list,list):
        raise ValueError("Input is not in correct format.")
    
    flatten_list = []
    for item in nested_list:
        if isinstance(item, list):
            temp = flatten(item)
            flatten_list.extend(temp)
        else:
            flatten_list.append(item)

    return flatten_list