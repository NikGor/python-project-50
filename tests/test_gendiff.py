import pytest
from gendiff import generate_diff
from gendiff.tools import load_file


# to test:
# 1. compare two json files, output in stylish format
# 2. compare two yaml files, output in stylish format
# 3. compare two nested json files, output in stylish format
# 4. compare two nested yaml files, output in stylish format
# ...
# repeat for all possible combinations of input files and output formats
# summary: 2 * 2 * 3 = 12 tests

@pytest.mark.parametrize("file1, file2, result, output_format", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', load_file('tests/fixtures/result.txt'), None),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', load_file('tests/fixtures/result.txt'), None),
    ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json', load_file('tests/fixtures/nested_result.txt'), None),
    ('tests/fixtures/nested1.yaml', 'tests/fixtures/nested2.yml', load_file('tests/fixtures/nested_result.txt'), None),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', load_file('tests/fixtures/plain_result.txt'), 'plain'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', load_file('tests/fixtures/plain_result.txt'), 'plain'),
    ('tests/fixtures/nested1.yaml', 'tests/fixtures/nested2.yml',
     load_file('tests/fixtures/plain_nested_result.txt'), 'plain'),
    ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json',
     load_file('tests/fixtures/plain_nested_result.txt'), 'plain'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     load_file('tests/fixtures/result.json'), 'json'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml',
     load_file('tests/fixtures/result.json'), 'json'),
    ('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json',
     load_file('tests/fixtures/nested_result.json'), 'json'),
    ('tests/fixtures/nested1.yaml', 'tests/fixtures/nested2.yml',
     load_file('tests/fixtures/nested_result.json'), 'json')

])
def test_diff(file1, file2, result, output_format):
    diff = generate_diff(file1, file2, output_format)
    assert diff == result
