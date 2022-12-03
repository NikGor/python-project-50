import pytest

from src.gendiff import generate_diff
from src.tools import load_file, get_file_content
from src.output import stylish, diff_to_plain, diff_to_json


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


@pytest.fixture
def plain_output_fixture():
    dict1 = get_file_content('tests/fixtures/file1.json')
    dict2 = get_file_content('tests/fixtures/file2.json')
    result = load_file('tests/fixtures/plain_result.txt')
    return dict1, dict2, result


@pytest.fixture
def plain_output_nested_fixture():
    dict1 = get_file_content('tests/fixtures/nested1.json')
    dict2 = get_file_content('tests/fixtures/nested2.json')
    result = load_file('tests/fixtures/plain_nested_result.txt')
    return dict1, dict2, result


@pytest.fixture
def json_output_fixture():
    dict1 = get_file_content('tests/fixtures/nested1.json')
    dict2 = get_file_content('tests/fixtures/nested2.json')
    result = load_file('tests/fixtures/result_nested.json')
    return dict1, dict2, result


def test_json(json_fixture):
    dict1, dict2, result = json_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff) == result


def test_yaml(yaml_fixture):
    dict1, dict2, result = yaml_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff) == result


def test_nested(nested_json_fixture):
    dict1, dict2, result = nested_json_fixture
    diff = generate_diff(dict1, dict2)
    assert stylish(diff) == result


def test_plain_output(plain_output_fixture):
    dict1, dict2, result = plain_output_fixture
    diff = diff_to_plain(generate_diff(dict1, dict2))
    assert diff == result


def test_plain_output_nested(plain_output_nested_fixture):
    dict1, dict2, result = plain_output_nested_fixture
    diff = generate_diff(dict1, dict2)
    assert diff_to_plain(diff) == result


def test_json_output(json_output_fixture):
    dict1, dict2, result = json_output_fixture
    diff = generate_diff(dict1, dict2)
    assert diff_to_json(diff) == result
