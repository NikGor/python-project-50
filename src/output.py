import json


def diff_to_dict(diff):  # convert diff to dict with '+' and '-' signs
    result = {}
    for key, value in sorted(diff.items()):
        if isinstance(value[0], dict) and isinstance(value[1], dict):
            result[key] = diff_to_dict(value[0])
        elif value[0] is None:
            result_key = f'+ {key}'
            result[result_key] = value[1]
        elif value[1] is None:
            result_key = f'- {key}'
            result[result_key] = value[0]
        elif value[0] == value[1]:
            result_key = f'  {key}'
            result[result_key] = value[0]
        else:
            result_key = f'- {key}'
            result[result_key] = value[0]
            result_key = f'+ {key}'
            result[result_key] = value[1]
    return result


def stylish(dict_to_print):  # print any dict in stylish format
    return json.dumps(diff_to_dict(dict_to_print), indent=4).replace('"', '').replace("'", '')


# пока затрудняюсь сделать вывод полного пути к свойству
def diff_to_plain(diff):  # convert diff to plain format
    result = []
    for key, value in sorted(diff.items()):
        if isinstance(value[0], dict) and isinstance(value[1], dict):
            result.append(diff_to_plain(value[0]))
        elif value[0] is None:
            if isinstance(value[1], dict):
                result.append(f"Property '{key}' was added with value: [complex value]")
            else:
                result.append(f"Property '{key}' was added with value: {value[1]}")
        elif value[1] is None:
            result.append(f"Property '{key}' was removed")
        elif value[0] == value[1]:
            result.append(f'Property \'{key}\' was unchanged')
        else:
            if isinstance(value[0], dict):
                result.append(f"Property '{key}' was updated. From [complex value] to {value[1]}")
            else:
                result.append(f"Property '{key}' was updated. From {value[0]} to {value[1]}")
    return '\n'.join(result)


def diff_to_json(diff):  # convert diff to json format
    return json.dumps(diff_to_dict(diff), indent=4)
