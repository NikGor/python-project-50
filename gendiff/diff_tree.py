from collections import defaultdict


def build_diff_tree(old_data, new_data):
    def handle_common_key(key):
        old_value = old_data[key]
        new_value = new_data[key]
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            return {'old': build_diff_tree(old_value, new_value),
                    'new': build_diff_tree(old_value, new_value)}
        else:
            return {'old': old_value, 'new': new_value}

    def handle_old(key):
        return {'old': old_data[key]}

    def handle_new(key):
        return {'new': new_data[key]}

    result = {}
    for key in set(old_data) | set(new_data):
        if key in old_data and key in new_data:
            handler = handle_common_key
        elif key in old_data:
            handler = handle_old
        else:
            handler = handle_new
        result[key] = handler(key)
    return result


def diff_to_dict(diff):
    result = defaultdict(dict)

    def handle_equal(key, value):
        result[key] = value['old']

    def handle_different(key, value):
        result[f'- {key}'] = value['old']
        result[f'+ {key}'] = value['new']

    def handle_new(key, value):
        result[f'+ {key}'] = value['new']

    def handle_old(key, value):
        result[f'- {key}'] = value['old']

    def handle_dict(key, value):
        result[key] = diff_to_dict(value['old'])

    for key, value in sorted(diff.items()):
        if 'new' in value and 'old' in value:
            if isinstance(value['old'], dict) and isinstance(value['new'], dict):
                handle_dict(key, value)
            elif value['old'] == value['new']:
                handle_equal(key, value)
            else:
                handle_different(key, value)
        elif 'new' in value:
            handle_new(key, value)
        elif 'old' in value:
            handle_old(key, value)
    return result
