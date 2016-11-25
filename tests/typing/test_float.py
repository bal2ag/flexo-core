import pytest

from flexo.typing import FloatType, PositiveFloatType
from flexo.errors import DefinitionError, ValidationError

def test_ctor_minvalue_not_int():
    with pytest.raises(DefinitionError):
        FloatType(minValue="test")

def test_ctor_maxvalue_not_int():
    with pytest.raises(DefinitionError):
        FloatType(maxValue="test")

def test_ctor_maxvalue_less_than_minvalue():
    with pytest.raises(DefinitionError):
        FloatType(minValue=2.0, maxValue=1.0)

def test_ctor_defaults():
    f = FloatType()

    assert f.minValue == None
    assert f.maxValue == None

def test_ctor():
    minValue = 2.0
    maxValue = 4.0
    f = FloatType(minValue=minValue, maxValue=maxValue)

    assert f.minValue == minValue
    assert f.maxValue == maxValue

def test_validate_not_float():
    with pytest.raises(ValidationError):
        FloatType().validate("test")

def test_validate_less_than_min():
    minValue = 2.0
    maxValue = 4.0
    f = FloatType(minValue=minValue, maxValue=maxValue)

    with pytest.raises(ValidationError):
        f.validate(1.0)

def test_validate_greater_than_max():
    minValue = 2.0
    maxValue = 4.0
    f = FloatType(minValue=minValue, maxValue=maxValue)

    with pytest.raises(ValidationError):
        f.validate(5.0)

def test_positive_float_type():
    f = PositiveFloatType()

    assert f.minValue == 0.0
