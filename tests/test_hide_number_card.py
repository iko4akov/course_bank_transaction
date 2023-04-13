from utils import hide_number_card

def test_hide_number_card_valid():
    """Test case Valid number"""

    info_1 = 'Testservice 1596837868705199'
    info_2 = 'Test 75106830613657916952'
    info_3 = 'Test service 6831982476737658'

    assert hide_number_card(info_1) == 'Testservice 1596 83** **** 5199'
    assert hide_number_card(info_2) == 'Test **6952'
    assert hide_number_card(info_3) == 'Test service 6831 98** **** 7658'
