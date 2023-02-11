from gendiff.utils.mapping_utils import map_plain


def format_plain(diff, path=''):
    def handle_unchanged(key, value):
        return ''

    def handle_changed(key, value):
        return f"Property '{key}' was updated. From {map_plain(value['old'])} to {map_plain(value['new'])}\n"

    def handle_added(key, value):
        return f"Property '{key}' was added with value: {map_plain(value['added'])}\n"

    def handle_removed(key, value):
        return f"Property '{key}' was removed\n"

    def handle_nested(key, value):
        return format_plain(value['nested'], f'{key}')

    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if 'nested' in value:
            result += handle_nested(key, value)
        elif 'old' in value:
            result += handle_changed(key, value)
        elif 'unchanged' in value:
            result += handle_unchanged(key, value)
        elif 'added' in value:
            result += handle_added(key, value)
        elif 'removed' in value:
            result += handle_removed(key, value)
    return result
