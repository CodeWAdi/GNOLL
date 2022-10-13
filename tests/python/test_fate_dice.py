#!/usr/bin/env python3

import pytest
from util import Mock, roll, error_handled_by_gnoll

@pytest.mark.parametrize("FD",["df", "dF", "df.2", "dF.2"])
def test_traditional_fate(FD):
    # Assure Symbols are correct
    # TODO: Maybe it would be better to return "PLUS", "BLANK" "MINUS"?
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == "-"

@pytest.mark.parametrize("FD",["df.1", "dF.1"])
def test_large_alt_fate_low(FD):
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=3)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=4)
    assert result == 0
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=5)
    assert result == "-"

@pytest.mark.parametrize("FD",["df.3", "dF.9"])
def test_large_alt_fate_high(FD):
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=0)
    assert result == "+"
    result = roll(FD, mock_mode=Mock.RETURN_CONSTANT, mock_const=1)
    assert result == "-"

def test_multidie():
    result = roll("2dF", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == ['-', '-']


def test_fate_addition():
    # Addition = Concatination
    result = roll("df+df", mock_mode=Mock.RETURN_CONSTANT, mock_const=2)
    assert result == ['-', '-']

@pytest.mark.parametrize("r",[
    # Most of the time, using the two together doesn't make sense
    ("d10+dF"),
    ("d10-dF"),
    # Much arithmithic is ambigious with symbols
    # e.g.
    # dF * 2 could mean:
    # - roll 2 dF dice (2dF -> -+)
    # or
    # - multiply the result of dF by 2 (+ -> ++)
    # Unless there is evidence of that priority defined somewhere
    ("dF-dF"),
    ("dF*2"),
    ("dF*dF"),
    ("dF/2"),
    ("dF/dF"),
    # We could perhaps use modulo as a counter
    # or some other function.
    # But for now, its undefined behaviour
    ("dF%2"),
    ("dF%dF"),
])
def test_fate_numeral_interoperability(r):
    try:
        roll(r)
    except Exception as e:
        error_handled_by_gnoll(e)
