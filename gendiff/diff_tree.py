def build_diff_tree(old_data, new_data):
    def handle_common_key(key):
        old_value = old_data[key]
        new_value = new_data[key]
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            return {'nested': build_diff_tree(old_value, new_value)}
        elif old_value != new_value:
            return {'old': old_value, 'new': new_value}
        else:
            return {'unchanged': old_value}

    def handle_removed(key):
        return {'removed': old_data[key]}

    def handle_added(key):
        return {'added': new_data[key]}

    result = {}
    for key in set(old_data) | set(new_data):
        if key in old_data and key in new_data:
            handler = handle_common_key
        elif key in old_data:
            handler = handle_removed
        else:
            handler = handle_added
        result[key] = handler(key)
    return result
