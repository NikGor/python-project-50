import json
from collections import defaultdict


def format_stylish(diff):
    def convert_diff_tree_to_dict(diff):
        result = defaultdict(dict)

        def handle_equal(key, value):
            result[key] = value['old']

        def handle_different(key, value):
            result[f'- {key}'] = value['old']
            result[f'+ {key}'] = value['new']

        def handle_added(key, value):
            result[f'+ {key}'] = value['added']

        def handle_removed(key, value):
            result[f'- {key}'] = value['removed']

        def handle_dict(key, value):
            result[key] = convert_diff_tree_to_dict(value)

        def handle_nested(key, value):
            result[key] = convert_diff_tree_to_dict(value)

        for key, value in sorted(diff.items()):
            if 'new' in value and 'old' in value:
                if 'nested' in value:
                    handle_nested(key, value)
                elif value['old'] == value['new']:
                    handle_equal(key, value)
                else:
                    handle_different(key, value)
            elif 'added' in value:
                handle_added(key, value)
            elif 'removed' in value:
                handle_removed(key, value)
            elif 'nested' in value:
                handle_dict(key, value['nested'])
        return result

    result = json.dumps(convert_diff_tree_to_dict(diff), indent=4)
    replace = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"true"': 'true',
        '"false"': 'false',
        '"null"': 'null',
    }
    for key, value in replace.items():
        result = result.replace(key, value)
    return result
