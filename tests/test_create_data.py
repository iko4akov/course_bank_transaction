import json

from src.utils import create_data
from config.config import config_obj

def test_create_data_valid():
    """Test Valid JSON file"""

    filename = config_obj.test_file_invalid
    expected_output = [
        {"test1": 1, "test2": 2, "test3": 3},
        {"test4": 4, "test5": 5, "test6": 6}
                       ]

    with open(filename, 'w') as f:
        json.dump(expected_output, f)

    assert create_data(filename) == expected_output
    assert type(create_data(filename)) == type(expected_output)

def test_create_data_invalid():
    """Test Invalid JSON file"""


    with open(config_obj.test_write_file, 'w') as f:
        f.write('invalid json')

    try:
        create_data(config_obj.test_write_file)

        assert False, 'Expected an exception to be raised'

    except json.JSONDecodeError:
        pass

def test_create_data_non():
    """Test Non-existent file"""

    try:
        create_data('non_existent.json')

        assert False, 'Expected an exception to be raised'

    except FileNotFoundError:
        pass
