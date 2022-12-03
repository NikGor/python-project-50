# the difference between the two dictionaries is stored in the result dictionary
# I use lists to store the values of the keys: [old_value, new_value]
# if item in the dictionary is a dictionary, then I call the function recursively
# the result is only for internal use, it is not displayed
# and can be used to display the result in different formats


def generate_diff(data1, data2):
    result = {}
    for key, value in data1.items():
        if key in data2:
            if value == data2[key]:
                result[key] = [value, value]
            elif isinstance(value, dict) and isinstance(data2[key], dict):
                result[key] = [generate_diff(value, data2[key]), generate_diff(value, data2[key])]
            else:
                result[key] = [value, data2[key]]
        else:
            result[key] = [value, None]
    for key, value in data2.items():
        if key not in data1:
            result[key] = [None, value]
    return result
