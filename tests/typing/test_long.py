import pytest

from flexo.typing import LongType, PositiveLongType, NonzeroPositiveLongType
from flexo.errors import DefinitionError, ValidationError

def test_ctor_minvalue_not_int():
    with pytest.raises(DefinitionError):
        LongType(minValue="test")

def test_ctor_maxvalue_not_int():
    with pytest.raises(DefinitionError):
        LongType(maxValue="test")

def test_ctor_maxvalue_less_than_minvalue():
    with pytest.raises(DefinitionError):
        LongType(minValue=2L, maxValue=1L)

def test_ctor_defaults():
    l = LongType()

    assert l.minValue == None
    assert l.maxValue == None

def test_ctor():
    minValue = 2L
    maxValue = 4L
    l = LongType(minValue=minValue, maxValue=maxValue)

    assert l.minValue == minValue
    assert l.maxValue == maxValue

def test_validate_not_long():
    with pytest.raises(ValidationError):
        LongType().validate("test")

def test_validate_less_than_min():
    minValue = 2L
    maxValue = 4L
    l = LongType(minValue=minValue, maxValue=maxValue)

    with pytest.raises(ValidationError):
        l.validate(1L)

def test_validate_greater_than_max():
    minValue = 2L
    maxValue = 4L
    l = LongType(minValue=minValue, maxValue=maxValue)

    with pytest.raises(ValidationError):
        l.validate(5L)

def test_positive_long_type():
    l = PositiveLongType()

    assert l.minValue == 0L

def test_nonzero_positive_long_type():
    l = NonzeroPositiveLongType()

    assert l.minValue == 1L
