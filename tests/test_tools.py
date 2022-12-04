import pytest
from gendiff.tools import get_file_extension, load_file, get_file_content


def test_get_file_extension():
    assert get_file_extension('tests/fixtures/file1.json') == '.json'


def test_load_file():
    assert load_file('tests/fixtures/test') == 'Hello Hexlet!'


def test_get_file_content():
    assert get_file_content('tests/fixtures/test.json') == {'Hello': 'World'}


def test_unknown_file_extension():
    with pytest.raises(ValueError):
        get_file_content('tests/fixtures/test.txt')

