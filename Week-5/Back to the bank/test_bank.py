from bank import value

def test_hello():
    assert value('Hello') == 0

def test_h():
    assert value('hey') == 20

def test_other():
    assert value('whey') == 100