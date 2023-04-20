import pytest

from src.utils import format_date


def test_format_date_valid():
    """Test case 1: Valid date string"""
    date_string = '2022-11-15T12:30:45.123456'
    expected_output = '15.11.2022'

    assert format_date(date_string) == expected_output

def test_format_date_invalid():
    """Test case 2: Invalid date string"""

    with pytest.raises(ValueError):
        format_date('2022-53-15T12:30:45.123456')


def test_format_date_empty():
    """Test case 3: Empty string"""

with pytest.raises(ValueError):
    format_date('')
