import math_func
import pytest

@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result

@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
    assert isinstance(result,str)

@pytest.mark.parametrize('arg1,arg2,result',
                         [
                             (7,3,10),
                             ('Hello',' World',"Hello World"),
                             (10.5,25.5,36)
                         ])
def test_add_p(arg1,arg2,result):
    assert math_func.add(arg1, arg2) == result
