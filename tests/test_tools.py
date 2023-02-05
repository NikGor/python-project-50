from gendiff.utils.file_utils import get_file_extension, load_file, get_file_content
from gendiff.utils.mapping_utils import map_plain


def test_get_file_extension():
    assert get_file_extension('tests/fixtures/file1.json') == '.json'


def test_load_file():
    assert load_file('tests/fixtures/test') == 'Hello Hexlet!'


def test_get_file_content():
    assert get_file_content('tests/fixtures/test.json') == {'Hello': 'World'}


def test_map_value():
    assert map_plain({'key': 'value'}) == '[complex value]'
    assert map_plain(True) == 'true'
    assert map_plain('value') == "'value'"
    assert map_plain(1) == 1
