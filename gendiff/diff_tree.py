def build_diff_tree(old_data, new_data):
    result = {}
    for key, value in old_data.items():
        if key in new_data:
            # Key is present in both dictionaries
            if isinstance(value, dict) and isinstance(new_data[key], dict):
                # Nested vertex
                descendants = build_diff_tree(value, new_data[key])
                result[key] = {'type': 'nested', 'value': descendants}
            elif value == new_data[key]:
                # Unchanged vertex
                result[key] = {'type': 'unchanged', 'value': value}
            else:
                # Changed vertex
                result[key] = {'type': 'changed', 'value': {'old': value, 'new': new_data[key]}}
        else:
            # Removed vertex
            result[key] = {'type': 'removed', 'value': value}
    for key, value in new_data.items():
        if key not in old_data:
            # Added vertex
            result[key] = {'type': 'added', 'value': value}
    return result
