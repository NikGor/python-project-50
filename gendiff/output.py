import json
from gendiff.tools import map_value, strip_dict


def diff_to_dict(diff):  # convert internal diff structure to dict with '+' and '-' signs
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
    return json.dumps(diff_to_dict(dict_to_print), indent=4).replace('"', '').replace("'", '').replace(',', '')


# пока затрудняюсь сделать вывод полного пути к свойству
def diff_to_plain(diff, path=''):  # convert diff to plain format
    result = ''
    for key, value in sorted(diff.items()):
        if path:
            key = f'{path}.{key}'
        if value[0] is None:
            if isinstance(value[1], dict):
                result += f'Property \'{key}\' was added with value: {map_value(value[1])}\n'
            else:
                result += f'Property \'{key}\' was added with value: {map_value(value[1])}\n'
        elif value[1] is None:
            result += f'Property \'{key}\' was removed\n'
        elif isinstance(value[0], dict) and isinstance(value[1], dict):
            result += diff_to_plain(value[0], key)
        elif value[0] == value[1]:
            pass
        else:
            result += f'Property \'{key}\' was updated. From {map_value(value[0])} to {map_value(value[1])}\n'
    return result


# return json without leading and trailing spaces in values
def diff_to_json(diff):
    return json.dumps(strip_dict(diff_to_dict(diff)), indent=5)
