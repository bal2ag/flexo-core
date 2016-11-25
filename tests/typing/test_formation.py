import pytest, datetime

from flexo.typing import FormationType 
from flexo.errors import DefinitionError, ValidationError

from mock import mock, MagicMock

def test_ctor_no_fields():
    with pytest.raises(DefinitionError):
        FormationType("test", "test", [])

def test_ctor_duplicate_fields():
    field_one = MagicMock()
    field_one.name = "test"

    field_two = MagicMock()
    field_two.name = "test"

    with pytest.raises(DefinitionError):
        FormationType("test", "test", [field_one, field_two])

def test_ctor():
    field_one = MagicMock()
    field_one.name = "testOne"

    field_two = MagicMock()
    field_two.name = "testTwo"

    name = "testName"
    description = "testDescription"
    moduleName = "testModuleName"
    fields = [field_one, field_two]

    formationType = FormationType(name, description, fields)

    assert formationType.name == name
    assert formationType.description == description
    assert formationType.fields == {f.name: f for f in fields}

@mock.patch('flexo.typing.validate_fields')
def test_validate(mock_validate_fields):
    field_one = MagicMock()
    field_one.name = "testOne"

    field_two = MagicMock()
    field_two.name = "testTwo"

    name = "testName"
    description = "testDescription"
    fields = [field_one, field_two]
    expected_fields = {field_one.name: field_one, field_two.name: field_two}
    value = {"testName": "testValue"}

    formationType = FormationType(name, description, fields)
    formationType.validate(value)

    mock_validate_fields.assert_called_with(expected_fields, value, name)
