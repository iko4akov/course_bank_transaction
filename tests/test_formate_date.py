from utils import format_date


def test_format_date_valid():
    """Test case 1: Valid date string"""
    date_string = '2022-11-15T12:30:45.123456'
    expected_output = '15.11.2022'

    assert format_date(date_string) == expected_output

def test_format_date_invalid():
    """Test case 2: Invalid date string"""

    date_string = '2022-53-15T12:30:45.123456'

    try:
        format_date(date_string)
        assert False, 'Expected an exception to be raised'

    except ValueError:
        pass

def test_format_date_empty():
    """Test case 3: Empty string"""

    date_string = ''
    try:
        format_date(date_string)
        assert False, 'Expected an exception to be raised'

    except ValueError:
        pass


test_format_date_valid()
test_format_date_invalid()
test_format_date_empty()
