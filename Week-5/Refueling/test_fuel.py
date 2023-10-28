from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0')

def test_x_greater():
    with pytest.raises(ValueError):
        assert convert('4')

