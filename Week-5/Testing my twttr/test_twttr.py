from twttr import shorten

def test_shorten():
    assert shorten('Hello') == 'Hll'

def test_num():
    assert shorten('g500') == 'g'

def test_pun():
    assert shorten('yes,') =='ys'