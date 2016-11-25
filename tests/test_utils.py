import pytest

import flexo.utils
from flexo.errors import ValidationError

from mock import MagicMock

def test_validate_fields_invalid_field():
    fields = {"testOne": "testOne"}

    with pytest.raises(ValidationError):
        flexo.utils.validate_fields(fields, {"test": "test"})

def test_validate_missing_required():
    field_one = MagicMock()
    field_one.name = "fieldOne"
    field_one.validate = MagicMock()
    field_one.required = True

    field_two = MagicMock()
    field_two.name = "fieldTwo"
    field_two.validate = MagicMock()
    field_two.required = True

    fields = {field_one.name: field_one, field_two.name: field_two}

    to_validate = {"fieldOne": "valueOne"}

    with pytest.raises(ValidationError):
        flexo.utils.validate_fields(fields, to_validate)

    field_one.validate.assert_called_with("valueOne")

def test_validate():
    field_one = MagicMock()
    field_one.name = "fieldOne"
    field_one.validate = MagicMock()
    field_one.required = True

    field_two = MagicMock()
    field_two.name = "fieldTwo"
    field_two.validate = MagicMock()
    field_two.required = True

    fields = {field_one.name: field_one, field_two.name: field_two}

    to_validate = {field_one.name: "valueOne", field_two.name: "valueTwo"}

    flexo.utils.validate_fields(fields, to_validate)
    for field in fields.values():
        field.validate.assert_called_with(to_validate[field.name])
