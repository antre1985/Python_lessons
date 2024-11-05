from pickle import FALSE

import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_res", [
    ('vodopad', 'Vodopad'),
    ('ребус', 'Ребус'),
    ('aRIA', 'Aria'),
    ('BROTHER', 'Brother')
    ])

def test_capitilize_positiv(input_str, expected_res):
    assert utils.capitilize(input_str) == expected_res

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_res", [
    ('', ''),  # пустая строка
    ('    ', '    '),  # строка с пробелами
    ('123', '123'),  # строка с цифрами
    ('!@#$%^&*()', '!@#$%^&*()')  # строка с символами
    ])
def test_capitilize_negative(input_str, expected_res):
    assert utils.capitilize(input_str) == expected_res


# 2.....................................................................................

@pytest.mark.positive
@pytest.mark.parametrize("with_space, result", [
    (" Hello", "Hello"),                # пробел в начале
    ('  Hello World', 'Hello World'),  # пробелы в начале
    ('HelloWorld', 'HelloWorld'),    # без пробелов
    ])
def test_trim_positive(with_space, result):
    assert utils.trim(with_space) == result

@pytest.mark.negative
@pytest.mark.parametrize("with_space, result", [
    ('', ''),                     # пустая строка
    ('    ', ''),                # строка с пробелами
    ('NoLeadingSpaces', 'NoLeadingSpaces'),  # без пробелов
    ('   123', '123'),          # пробелы перед цифрами
    ('   !@#$%', '!@#$%'),      # пробелы перед символами
])
def test_trim_negative(with_space, result):
    # Проверяем, что строка обрабатывается корректно
    assert utils.trim(with_space) == result

#3....................................................................................
@pytest.mark.positive
@pytest.mark.parametrize("input_text, result",[
    ('w,e,l,l', ['w', 'e', 'l', 'l']),
    (",,,", ["", "", "", ""])
])
def test_to_list_positive(input_text, result):
    assert utils.to_list(input_text) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_text, result",[
    ("", []),
    ("  ", [  ])
])
def test_to_list_negative(input_text, result):
    assert utils.to_list(input_text) == result


#4..................................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", True),
    ("SkyPro", "o", True)
 ])
def test_contains_positive(input_str, symbol, result):
    assert utils.contains(input_str, symbol) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "К", False),
    ("SkyPro", "3", False),
    ("SkyPro", "%", False)
])
def test_contains_negative(input_str, symbol, result):
    assert utils.contains(input_str, symbol) == result

#5............................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_del, result", [
    ("SkyPro", "k", True),
    ("SkyPro", "P", True)
])
def test_contains_del_positive(input_str, symbol_del, result):
    assert utils.contains(input_str, symbol_del) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_del, result", [
    ("SkyPro", "z", False),
    ("SkyPro", "7", False),
    ("SkyPro"," ", False )
])
def test_contains_del_negative(input_str, symbol_del, result):
    assert utils.contains(input_str, symbol_del) == result

#6...............................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "S", True)
])
def test_starts_positive(input_str, symbol, result):
    assert utils.starts_with(input_str, symbol) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "P", False),
    ("SkyPro", " ", False)
])
def test_starts_negative(input_str, symbol, result):
    assert utils.starts_with(input_str, symbol) == result

#7.............................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "o", True)
])
def test_starts_positive(input_str, symbol, result):
    assert utils.end_with(input_str, symbol) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, result", [
    ("SkyPro", "P", False),
    ("SkyPro", " ", False)
])
def test_starts_negative(input_str, symbol, result):
    assert utils.end_with(input_str, symbol) == result

#8..............................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, result", [
    (" ", True),
    ("", True),
    ("  ", True),
    ("  ", True)
])
def test_empty_positive(input_str, result):
    assert utils.is_empty(input_str) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, result", [
    ("SkyPro", False),
    ("66", False),
    ("%^^&", False)
])
def test_starts_negative(input_str, result):
    assert utils.is_empty(input_str) == result

#9............................................................................

@pytest.mark.positive
@pytest.mark.parametrize("input_str, element, result", [
    (["Sky", "Pro"], ",", "Sky,Pro"),
    ([1, 2, 3, 4], ",", "1,2,3,4"),
    (["Sky", "Pro"], "-", "Sky-Pro")
])
def test_joiner_positive(input_str, element, result):
    assert utils.list_to_string(input_str, element) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_str, element", [
    (123, ","),        # Ожидается ошибка, так как это не список
    (None, ","),      # Ожидается ошибка, так как это не список
])
def test_joiner_negative(input_str, element):
    with pytest.raises(TypeError):  # Ожидаем ошибку при передаче некорректного типа
        utils.list_to_string(input_str, element)












