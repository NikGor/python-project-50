import pytest
from src.gendiff import generate_diff
from src.tools import get_file_extension, load_file, get_file_content
from src.output import diff_to_str


@pytest.fixture
def get_json():
    dict1 = get_file_content('tests/fixtures/file1.json')
    dict2 = get_file_content('tests/fixtures/file2.json')
    result = load_file('tests/fixtures/result.txt')
    return dict1, dict2, result


@pytest.fixture
def get_yaml():
    dict1 = get_file_content('tests/fixtures/file1.yml')
    dict2 = get_file_content('tests/fixtures/file2.yml')
    result = load_file('tests/fixtures/result.txt')
    return dict1, dict2, result


@pytest.fixture
def get_tree():
    dict1 = get_file_content('tests/fixtures/tree1.json')
    dict2 = get_file_content('tests/fixtures/tree2.json')
    result = load_file('tests/fixtures/tree_diff.txt')
    return dict1, dict2, result


# def test_tree(get_tree):
#     dict1, dict2, result = get_tree
#     diff = generate_diff(dict1, dict2)
#     assert diff_to_str(diff) == result


def test_json(get_json):
    dict1, dict2, result = get_json
    diff = generate_diff(dict1, dict2)
    assert diff_to_str(diff) == result


def test_yaml(get_yaml):
    dict1, dict2, result = get_yaml
    diff = generate_diff(dict1, dict2)
    assert diff_to_str(diff) == result


def test_get_file_extension():
    assert get_file_extension('tests/fixtures/file1.json') == '.json'


def test_load_file():
    assert load_file('tests/fixtures/test') == 'Hello Hexlet!'


def test_get_file_content():
    assert get_file_content('tests/fixtures/test.json') == {'Hello': 'World'}
    assert get_file_content('tests/fixtures/test.yaml') == {'Hello': 'World'}
