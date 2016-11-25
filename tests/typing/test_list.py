import pytest, json

from flexo.typing import ListType, BaseType
from flexo.errors import DefinitionError, ValidationError

from mock import MagicMock, call

class MockType(BaseType):
    def __init__(self):
        self.validate = MagicMock()

def test_ctor_not_basetype():
    with pytest.raises(DefinitionError):
        ListType(elementType="test")

def test_ctor():
    elementType = MockType()

    assert ListType(elementType=elementType).elementType == elementType

def test_validate_not_list():
    elementType = MockType()

    with pytest.raises(ValidationError):
        ListType(elementType=elementType).validate("test")

def test_validate():
    elementType = MockType()
    values = ["test1", "test2", "test3"]

    ListType(elementType=elementType).validate(values)
    elementType.validate.assert_has_calls([call(x) for x in values])
