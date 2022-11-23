from gendiff.gen_diff import generate_diff
from gendiff.tools import normalize_file_name
import json


def test_generate_diff():
    with open(normalize_file_name('tests/fixtures/file1.json')) as _:
        dict1 = json.load(_)
    _.close()
    with open(normalize_file_name('tests/fixtures/file2.json')) as _:
        dict2 = json.load(_)
    _.close()
    with open(normalize_file_name('tests/fixtures/result.txt')) as _:
        assert generate_diff(dict1, dict2) == _.read()
    _.close()
