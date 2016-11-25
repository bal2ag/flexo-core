import pytest, datetime

from flexo.typing import DatetimeType
from flexo.errors import DefinitionError, ValidationError

def test_validate_not_datetime():
    with pytest.raises(ValidationError):
        DatetimeType().validate(10)

def test_validate():
    d = datetime.datetime.utcnow()
    DatetimeType().validate(d)
