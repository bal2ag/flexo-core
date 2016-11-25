import pytest

from flexo.typing import StringType
from flexo.errors import DefinitionError, ValidationError

def test_ctor_minlength_not_int():
    with pytest.raises(DefinitionError):
        StringType(minLength="test")

def test_ctor_maxlength_not_int():
    with pytest.raises(DefinitionError):
        StringType(maxLength="test")

def test_ctor_maxlength_less_than_minlength():
    with pytest.raises(DefinitionError):
        StringType(minLength=3, maxLength=2)

def test_ctor_defaults():
    s = StringType()

    assert s.minLength == 0
    assert s.maxLength == None

def test_ctor():
    minLength = 2
    maxLength = 4
    s = StringType(minLength=minLength, maxLength=maxLength)

    assert s.minLength == minLength
    assert s.maxLength == maxLength

def test_validate_not_string():
    with pytest.raises(ValidationError):
        StringType().validate(10)

def test_validate_length_less_than_min():
    minLength = 2
    maxLength = 4
    s = StringType(minLength=minLength, maxLength=maxLength)

    with pytest.raises(ValidationError):
        s.validate("a")

def test_validate_length_greater_than_max():
    minLength = 2
    maxLength = 4
    s = StringType(minLength=minLength, maxLength=maxLength)

    with pytest.raises(ValidationError):
        s.validate("aaaaa")
