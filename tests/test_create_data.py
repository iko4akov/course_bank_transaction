import json

from src.utils import create_data


def test_create_data_valid():
    """Test Valid JSON file"""

    filename = 'test_data.json'
    expected_output = {'name': 'John', 'age': 30, 'city': 'New York'}

    with open(filename, 'w') as f:
        json.dump(expected_output, f)

    assert create_data(filename) == expected_output
    assert type(create_data(filename)) == type(expected_output)

def test_create_data_invalid():
    """Test Invalid JSON file"""

    filename = 'invalid_data.json'

    with open(filename, 'w') as f:
        f.write('invalid json')

    try:
        create_data(filename)

        assert False, 'Expected an exception to be raised'

    except json.JSONDecodeError:
        pass

def test_create_data_non():
    """Test Non-existent file"""

    filename = 'non_existent.json'

    try:
        create_data(filename)

        assert False, 'Expected an exception to be raised'

    except FileNotFoundError:
        pass
