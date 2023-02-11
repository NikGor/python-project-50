import json
from collections import defaultdict
from gendiff.utils.mapping_utils import map_stylish


def format_stylish(diff):
    def convert_diff_tree_to_dict(diff):
        result = defaultdict(dict)

        def handle_unchanged(key, value):
            result[key] = value['unchanged']

        def handle_changed(key, value):
            result[f'- {key}'] = value['old']
            result[f'+ {key}'] = value['new']

        def handle_added(key, value):
            result[f'+ {key}'] = value['added']

        def handle_removed(key, value):
            result[f'- {key}'] = value['removed']

        def handle_nested(key, value):
            result[key] = convert_diff_tree_to_dict(value)

        for key, value in sorted(diff.items()):
            if 'nested' in value:
                handle_nested(key, value['nested'])
            elif 'old' in value:
                handle_changed(key, value)
            elif 'unchanged' in value:
                handle_unchanged(key, value)
            elif 'added' in value:
                handle_added(key, value)
            elif 'removed' in value:
                handle_removed(key, value)
        return result

    result = json.dumps(convert_diff_tree_to_dict(diff), indent=4)
    return map_stylish(result)
