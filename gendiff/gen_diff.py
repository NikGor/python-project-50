def generate_diff(file1, file2):
    result = ''
    for key, value in file1.items():
        if key in file2:
            if value == file2[key]:
                result += f'  {key}: {value}\n'
            else:
                result += f'- {key}: {value}\n+ {key}: {file2[key]}\n'
        else:
            result += f'- {key}: {value}\n'
    for key, value in file2.items():
        if key not in file1:
            result += f'+ {key}: {value}\n'
    return result[:-1] # убираем символ переноса строки в конце
