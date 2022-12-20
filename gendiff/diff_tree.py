def build_diff_tree(old_data, new_data):
    result = {}
    for key, value in old_data.items():
        if key in new_data:
            if isinstance(value, dict) and isinstance(new_data[key], dict):
                nodes = build_diff_tree(value, new_data[key])
                result[key] = {'type': 'nested', 'value': nodes}
            elif value == new_data[key]:
                result[key] = {'type': 'unchanged', 'value': value}
            else:
                result[key] = {'type': 'changed', 'value': {'old': value, 'new': new_data[key]}}
        else:
            result[key] = {'type': 'removed', 'value': value}
    for key, value in new_data.items():
        if key not in old_data:
            result[key] = {'type': 'added', 'value': value}
    return result
