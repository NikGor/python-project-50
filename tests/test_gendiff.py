import pytest
from gendiff.logic import generate_diff
from gendiff.tools import normalize_file_name
import json


@pytest.fixture
def get_json():
    with open(normalize_file_name('//wsl$/Ubuntu-20.04/home/nikostolz/Hexlet/Python/python-project-50/tests/fixtures'
                                  '/file1.json')) as _:
        dict1 = json.load(_)
    with open(normalize_file_name('//wsl$/Ubuntu-20.04/home/nikostolz/Hexlet/Python/python-project-50/tests/fixtures'
                                  '/file2.json')) as _:
        dict2 = json.load(_)
    with open(normalize_file_name('//wsl$/Ubuntu-20.04/home/nikostolz/Hexlet/Python/python-project-50/tests/fixtures'
                                  '/result.txt')) as _:
        result = _.read()
    return dict1, dict2, result


def test_generate_diff(get_json):
    dict1, dict2, result = get_json
    assert generate_diff(dict1, dict2) == result
