import pytest

from demo01.div import div


@pytest.mark.level_critial
def test_div_int():
    assert div(10, 2) == 5
    assert div(8, 4) == 2
    assert div(10000, 50) == 200
    assert div(div(12, 2), 3) == 2


@pytest.mark.level_media
def test_div_float():
    assert type(div(7, 5)) == float
    assert type(7, 5) == 1.4
    assert div(8, 9) == 0.88


@pytest.mark.level_exception
def test_div_exception():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

    assert div('100', 8)
    assert div(9, '12')


int_data = [(10, 2, 5), (2, 1, 2), (3, 2, 1.5), (6, 4, 1.58)]
@pytest.mark.level_critial
@pytest.mark.parametrize("number1,number2,expectResult", int_data)
def test_div_int_param(number1, number2, expectResult):
    assert div(number1, number2) == expectResult


@pytest.mark.level_critial
@pytest.mark.parametrize("number1,number2,expectResult", [
    (1.0, 2.0, 0.5),
    (1.2, 2, 0.6),
    (10001.2, 4, 2500.3),
    (10, 3, 3.33),
    (-0.8, 0.4, 2)
])
def test_div_float_param(number1, number2, expectResult):
    assert div(number1, number2) == expectResult


except_data = [(3, 0, ZeroDivisionError), ('100', 9, TypeError), (99, '99', TypeError),('',9,ZeroDivisionError)]
@pytest.mark.level_exception
@pytest.mark.parametrize("number1, number2, exceptResult", except_data)
def test_div_exception_param(number1, number2, exceptResult):
    with pytest.raises(exceptResult):
        div(number1, number2)
