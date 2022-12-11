# the difference between the two dictionaries is stored in the result dictionary
# I use dicts to store the values of the keys: {'old': old_value, 'new': new_value}
# if item in the dictionary is a dictionary, then I call the function recursively
# the result is only for internal use, it is not displayed
# and can be used to display the result in different formats


def diff_calculator(old_data, new_data):
    result = {}
    for key, value in old_data.items():
        if key in new_data:
            if isinstance(value, dict) and isinstance(new_data[key], dict):
                result[key] = {'old': diff_calculator(value, new_data[key]),
                               'new': diff_calculator(value, new_data[key])}
            elif value == new_data[key]:
                result[key] = {'old': value, 'new': value}
            else:
                result[key] = {'old': value, 'new': new_data[key]}
        else:
            result[key] = {'old': value}
    for key, value in new_data.items():
        if key not in old_data:
            result[key] = {'new': value}
    return result
