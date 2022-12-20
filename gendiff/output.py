import json
from collections import defaultdict
from gendiff.tools import map_value, map_stylish


def diff_to_dict(diff):
    def handle_changed(key, value):
        result[f'- {key}'] = value['value']['old']
        result[f'+ {key}'] = value['value']['new']

    def handle_added(key, value):
        result[f'+ {key}'] = value['value']

    def handle_removed(key, value):
        result[f'- {key}'] = value['value']

    def handle_unchanged(key, value):
        result[key] = value['value']

    def handle_nested(key, value):
        result[key] = diff_to_dict(value['value'])

    result = defaultdict(dict)
    for key, value in sorted(diff.items()):
        handler = {'changed': handle_changed,
                   'added': handle_added,
                   'removed': handle_removed,
                   'unchanged': handle_unchanged,
                   'nested': handle_nested}[value['type']]
        handler(key, value)
    return result


def format_stylish(diff):
    dict_to_print = diff_to_dict(diff)

    def stylish(dict_to_stylish, tab='    ', lvl=1):  # print any dict in stylish format
        result = '{\n'
        for key, value in dict_to_stylish.items():
            if isinstance(value, dict):
                if key.startswith('+') or key.startswith('-'):
                    result += f"{tab * lvl}{map_stylish(key)}: {stylish(value, tab, lvl + 1)}"[2:] + '\n'
                else:
                    result += f"{tab * lvl}{key}: {stylish(value, tab, lvl + 1)}\n"
            else:
                if key.startswith('+') or key.startswith('-'):
                    result += f"{tab * lvl}{map_stylish(key)}: {map_stylish(value)}"[2:] + '\n'
                else:
                    result += f'{tab * lvl}{key}: {map_stylish(value)}\n'
        result += f'{tab * (lvl - 1)}}}'
        return result

    return stylish(dict_to_print)


def format_plain(diff, path=''):
    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if value['type'] == 'nested':
            result += format_plain(value['value'], f'{key}')
        elif value['type'] == 'changed':
            result += f"Property '{key}' was updated. " \
                      f"From {map_value(value['value']['old'])} to {map_value(value['value']['new'])}\n"
        elif value['type'] == 'added':
            result += f"Property '{key}' was added with value: {map_value(value['value'])}\n"
        elif value['type'] == 'removed':
            result += f"Property '{key}' was removed\n"
    return result


def format_json(diff):
    return json.dumps(diff_to_dict(diff), indent=5)
