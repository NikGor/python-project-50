# the difference between the two dictionaries is stored in the result dictionary
# I use lists to store the values of the keys: {'old': old_value, 'new': new_value}
# if item in the dictionary is a dictionary, then I call the function recursively
# the result is only for internal use, it is not displayed
# and can be used to display the result in different formats


def diff_calculator(data1, data2):
    result = {}
    for key, value in data1.items():
        if key in data2:
            if isinstance(value, dict) and isinstance(data2[key], dict):
                result[key] = {'old': diff_calculator(value, data2[key]), 'new': diff_calculator(value, data2[key])}
            elif value == data2[key]:
                result[key] = {'old': value, 'new': value}
            else:
                result[key] = {'old': value, 'new': data2[key]}
        else:
            result[key] = {'old': value}
    for key, value in data2.items():
        if key not in data1:
            result[key] = {'new': value}
    return result
