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
    with pytest.raises(AttributeError):
        last_operations(config_obj.test_file)
