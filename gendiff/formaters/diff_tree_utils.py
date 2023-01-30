from collections import defaultdict


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
        result[key] = convert_diff_tree_to_dict(value['old'])

    for key, value in sorted(diff.items()):
        if 'new' in value and 'old' in value:
            if isinstance(value['old'], dict) and isinstance(value['new'], dict):
                handle_dict(key, value)
            elif value['old'] == value['new']:
                handle_equal(key, value)
            else:
                handle_different(key, value)
        elif 'added' in value:
            handle_added(key, value)
        elif 'removed' in value:
            handle_removed(key, value)
    return result