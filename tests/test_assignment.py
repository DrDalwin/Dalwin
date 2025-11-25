from assignment import square_number

def test_square_positive_numbers():
    assert square_number(5) == 25
    assert square_number(10) == 100

def test_square_zero():
    assert square_number(0) == 0

def test_square_negative_numbers():
    assert square_number(-4) == 16
    assert square_number(-1) == 1
