from plates import is_valid

def test_valid1():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False
    assert is_valid("cs50") == True

def test_valid2():
    assert is_valid("23") == False

def test_valid3():
    assert is_valid("cs.,32") == False
    assert is_valid("cs32") == True

def test_valid4():
    assert is_valid("cs05") == False
    assert is_valid("cs50") == True
    assert is_valid("cs50p") == False