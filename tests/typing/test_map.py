import pytest, json

from flexo.typing import MapType, StringType, BaseType
from flexo.errors import DefinitionError, ValidationError

from mock import MagicMock, call

class MockKeyType(StringType):
    def __init__(self):
        self.validate = MagicMock()

class MockValueType(BaseType):
    def __init__(self):
        self.validate = MagicMock()

def test_ctor_keytype_not_string():
    with pytest.raises(DefinitionError):
        MapType(keyType="test", valueType="test")

def test_ctor_valuetype_not_basetype():
    with pytest.raises(DefinitionError):
        MapType(keyType=MockKeyType(), valueType="test")

def test_ctor():
    keyType = MockKeyType()
    valueType = MockValueType()

    m = MapType(keyType=keyType, valueType=valueType)
    assert m.keyType == keyType
    assert m.valueType == valueType

def test_validate_not_dict():
    keyType = MockKeyType()
    valueType = MockValueType()

    with pytest.raises(ValidationError):
        MapType(keyType=keyType, valueType=valueType).validate("test")
        
def test_validate():
    keyType = MockKeyType()
    valueType = MockValueType()
    values = {"testKey1": "testValue1", "testKey2": "testValue2"}

    MapType(keyType=keyType, valueType=valueType).validate(values)
    keyType.validate.assert_has_calls([call(v) for v in values.keys()])
    valueType.validate.assert_has_calls([call(v) for v in values.values()])
