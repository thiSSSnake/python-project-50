def gen_diff(data_1, data_2):
    keys = data_1.keys() | data_2.keys()
    result = []

    for key in sorted(keys):
        value_1 = data_1.get(key)
        value_2 = data_2.get(key)

        if key not in data_1:
            result.append({
                'key': key,
                'type': 'added',
                'value': value_2
            })
        elif key not in data_2:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': value_1
            })
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': gen_diff(value_1, value_2)
            })
        elif data_1[key] == data_2[key]:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': value_1
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': value_1,
                'new_value': value_2
            })
    return result


def make_tree(data_1, data_2):
    return {
        'type': 'root',
        'children': gen_diff(data_1, data_2)
    }
