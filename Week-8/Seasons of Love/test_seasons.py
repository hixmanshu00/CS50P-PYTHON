from seasons import convert


def test_date():
    assert convert(7830) == "Eleven million, two hundred seventy-five thousand, two hundred minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"