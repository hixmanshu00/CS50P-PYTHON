import numb3rs

def test_valid():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("10.0.0.255") == True
    assert numb3rs.validate("255.255.255.255") == True

def test_invalid():
    assert numb3rs.validate("256.0.0.0") == False
    assert numb3rs.validate("0.0.0.-1") == False
    assert numb3rs.validate("abc.def.ghi.jkl") == False
    assert numb3rs.validate("192.168.1") == False
    assert numb3rs.validate("75.456.76.65") == False




