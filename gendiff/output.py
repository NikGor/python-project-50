import json
from collections import defaultdict
from gendiff.tools import strip_dict, map_value, map_stylish


def diff_to_dict(diff):  # convert internal diff structure to dict with '+' and '-' signs
    result = defaultdict(dict)
    for key, value in sorted(diff.items()):
        if 'new' in value and 'old' in value:
            if isinstance(value['old'], dict) and isinstance(value['new'], dict):
                result[key] = diff_to_dict(value['old'])
            elif value['old'] == value['new']:
                result_key = f'  {key}'
                result[result_key] = value['old']
            else:
                result_key = f'- {key}'
                result[result_key] = value['old']
                result_key = f'+ {key}'
                result[result_key] = value['new']
        elif 'new' in value:
            result_key = f'+ {key}'
            result[result_key] = value['new']
        elif 'old' in value:
            result_key = f'- {key}'
            result[result_key] = value['old']
    return result


def stylish(diff):
    dict_to_print = diff_to_dict(diff)

    def stylish_dict(dict_to_stylish, tab='  ', lvl=1):  # print any dict in stylish format
        result = '{\n'
        for key, value in dict_to_stylish.items():
            if isinstance(value, dict):
                result += f'  {tab * lvl}{key}: {stylish_dict(value, tab, lvl + 1)}\n'
            else:
                result += f'  {tab * lvl}{key}: {map_stylish(value)}\n'
        result += f'{tab * (lvl - 1)}}}'
        return result

    return stylish_dict(dict_to_print)
    # return json.dumps(diff_to_dict(dict_to_print), indent=2).replace('"', '').replace("'", '').replace(',', '')


def diff_to_plain(diff, path=''):  # convert diff to plain format
    result = ''
    for key, value in sorted(diff.items()):
        if 'new' in value and 'old' in value:
            if isinstance(value['old'], dict) and isinstance(value['new'], dict):
                result += diff_to_plain(value['old'], f'{path}.{key}')
            elif value['old'] == value['new']:
                pass
            else:
                result += f"Property '{path}.{key}' was updated. " \
                          f"From {map_value(value['old'])} to {map_value(value['new'])}\n"
        elif 'new' in value:
            result += f"Property '{path}.{key}' was added with value: {map_value(value['new'])}\n"
        elif 'old' in value:
            result += f"Property '{path}.{key}' was removed\n"
    return result


def diff_to_json(diff):
    return json.dumps(strip_dict(diff_to_dict(diff)), indent=5)
