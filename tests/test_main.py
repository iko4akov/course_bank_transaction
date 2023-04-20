import json

import pytest

from config.config import config_obj
from src.main import last_operations


def test_get_file_not_found():
    """Test case 1: File not found error"""
    with pytest.raises(FileNotFoundError):
        last_operations('qerty')


def test_file_type_error():
    """Test case 2: File type error"""
    with pytest.raises(json.JSONDecodeError):
        last_operations(True)

def test_none_key():
    with pytest.raises(KeyError):
        last_operations(config_obj.test_file_invalid)


def test_last_operations():

    assert last_operations(config_obj.test_data_json) == print('26.08.2019 Перевод организации\n' \
                                                         'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                                                         '31957.58 руб.')