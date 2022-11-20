# - follow: false
# host: hexlet.io
# - proxy: 123.234
# .53
# .22
# - timeout: 50
# + timeout: 20
# + verbose: true
import json


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    result = []
    for key in file1.keys():
        if key in file2.keys():
            if file1[key] == file2[key]:
                result.append('  ' + key + ': ' + str(file1[key]))
            else:
                result.append('- ' + key + ': ' + str(file1[key]))
                result.append('+ ' + key + ': ' + str(file2[key]))
        else:
            result.append('- ' + key + ': ' + str(file1[key]))
    for key in file2.keys():
        if key not in file1.keys():
            result.append('+ ' + key + ': ' + str(file2[key]))
    return result


print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
