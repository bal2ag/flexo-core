import pytest

from flexo.typing import BooleanType
from flexo.errors import ValidationError

def test_validate_not_boolean():
    with pytest.raises(ValidationError):
        BooleanType().validate("test")

def test_validate():
    BooleanType().validate(True)
