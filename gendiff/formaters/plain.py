from gendiff.utils.mapping_utils import map_value


def format_plain(diff, path=''):
    def handle_equal(key, value):
        return ''

    def handle_different(key, value):
        return f"Property '{key}' was updated. From {map_value(value['old'])} to {map_value(value['new'])}\n"

    def handle_new(key, value):
        return f"Property '{key}' was added with value: {map_value(value['added'])}\n"

    def handle_old(key, value):
        return f"Property '{key}' was removed\n"

    def handle_dict(key, value):
        return format_plain(value['old'], f'{key}')

    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if 'new' in value and 'old' in value:
            if isinstance(value['old'], dict) and isinstance(value['new'], dict):
                result += handle_dict(key, value)
            elif value['old'] == value['new']:
                result += handle_equal(key, value)
            else:
                result += handle_different(key, value)
        elif 'added' in value:
            result += handle_new(key, value)
        elif 'removed' in value:
            result += handle_old(key, value)
    return result