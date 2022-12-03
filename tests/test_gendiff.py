import pytest
from src.gendiff import generate_diff
from src.tools import get_file_extension, load_file, get_file_content
from src.output import diff_to_dict, stylish


@pytest.fixture
def json_fixture():
    dict1 = get_file_content('tests/fixtures/file1.json')
    dict2 = get_file_content('tests/fixtures/file2.json')
    result = load_file('tests/fixtures/result.txt')
    return dict1, dict2, result


@pytest.fixture
def yaml_fixture():
    dict1 = get_file_content('tests/fixtures/file1.yml')
    dict2 = get_file_content('tests/fixtures/file2.yml')
    result = load_file('tests/fixtures/result.txt')
    return dict1, dict2, result


@pytest.fixture
def nested_json_fixture():
    dict1 = get_file_content('tests/fixtures/nested1.json')
    dict2 = get_file_content('tests/fixtures/nested2.json')
    result = load_file('tests/fixtures/nested_result')
    return dict1, dict2, result


@pytest.fixture
def nested_yaml_fixture():
    dict1 = get_file_content('tests/fixtures/nested1.yaml')
    dict2 = get_file_content('tests/fixtures/nested2.yml')
    result = load_file('tests/fixtures/nested_result')
    return dict1, dict2, result


def test_json(json_fixture):
    dict1, dict2, result = json_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff_to_dict(diff)) == result


def test_yaml(yaml_fixture):
    dict1, dict2, result = yaml_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff_to_dict(diff)) == result


def test_tree(nested_json_fixture):
    dict1, dict2, result = nested_json_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff_to_dict(diff)) == result


def test_get_file_extension():
    assert get_file_extension('tests/fixtures/file1.json') == '.json'


def test_load_file():
    assert load_file('tests/fixtures/test') == 'Hello Hexlet!'


def test_get_file_content():
    assert get_file_content('tests/fixtures/test.json') == {'Hello': 'World'}
    assert get_file_content('tests/fixtures/test.yaml') == {'Hello': 'World'}
