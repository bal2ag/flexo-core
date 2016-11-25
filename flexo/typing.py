from .errors import DefinitionError, ValidationError
from .utils import validate_fields

import datetime, types, json

class BaseType(object):
     """Base class for basic types or formations (complex types). This enables
     determination if a variable is a valid 'type' (basic or formation)."""
     pass

class StringType(BaseType):
    """A type representing a unicode string.

    :type minLength: int
    :param minLength: The minimum length of strings of this type. Defaults
                      to 0.

    :type maxLength: int
    :param maxLength: The maximum length of strings of this type. Defaults
                      to None (unspecified).
    """
    def __init__(self, minLength=0, maxLength=None):
        if not isinstance(minLength, types.IntType):
            raise DefinitionError("minLength "\
                    "'%s' must be an integer, but was %s" %\
                    (str(minLength), type(minLength)))

        if maxLength is not None and not isinstance(maxLength,\
                types.IntType):
            raise DefinitionError("maxLength "\
                    "'%s' must be an integer, but was %s" %\
                    (str(maxLength), type(maxLength)))

        if maxLength is not None and maxLength < minLength:
            raise DefinitionError("maxLength cannot be less than minLength")

        self.minLength = minLength
        self.maxLength = maxLength

    def validate(self, value):
        """Validates if the given value is a valid string.

        :type value: string
        :param value: The value to validate.
        """
        if not isinstance(value, types.StringTypes):
            raise ValidationError("%s: expected string but was %s" %\
                    (str(value), type(value)))
        if len(value) < self.minLength:
            raise ValidationError("length of '%s' is %s, but minimum is %s" %\
                    (value, len(value), self.minLength))
        if self.maxLength is not None and len(value) > self.maxLength:
            raise ValidationError("length of '%s' is %s, but maximum is %s" %\
                    (value, len(value), self.maxLength))

class LongType(BaseType):
    """A type representing a Long.

    :type minValue: int
    :param minValue: The minimum size of longs of this type. Defaults
                     to None (unspecified).

    :type maxValue: int
    :param maxValue: The maximum size of longs of this type. Defaults
                     to None (unspecified).
    """
    def __init__(self, minValue=None, maxValue=None):
        if minValue is not None and not isinstance(minValue,\
                types.LongType):
            raise DefinitionError("minValue "\
                    "'%s' must be a long, but was %s" %\
                    (str(minValue), type(minValue)))

        if maxValue is not None and not isinstance(maxValue,\
                types.LongType):
            raise DefinitionError("maxValue "\
                    "'%s' must be a long, but was %s" %\
                    (str(maxValue), type(maxValue)))

        if minValue is not None and maxValue is not None and\
                maxValue < minValue:
            raise DefinitionError("maxValue cannot be less than minValue")

        self.minValue = minValue
        self.maxValue = maxValue

    def validate(self, value):
        """Validates if the given value is a valid long. 

        :type value: long
        :param value: The value to validate.
        """
        if not isinstance(value, types.LongType):
            raise ValidationError("%s: expected long but was %s" %\
                    (str(value), type(value)))
        if self.minValue is not None and value < self.minValue:
            raise ValidationError("%s is less than minimum %s" %\
                    (str(value), self.minValue))
        if self.maxValue is not None and value > self.maxValue:
            raise ValidationError("%s is greater than maximum %s" %\
                    (str(value), self.maxValue))

class FloatType(BaseType):
    """A type representing a float.

    :type minValue: float
    :param minValue: The minimum size of floats of this type. Defaults
                     to None (unspecified).

    :type maxvalue: float
    :param maxValue: The maximum size of floats of this type. Defaults
                     to None (unspecified).
    """
    def __init__(self, minValue=None, maxValue=None):
        if minValue is not None and not isinstance(minValue,\
                types.FloatType):
            raise DefinitionError("minValue "\
                    "'%s' must be a float, but was %s" %\
                    (str(minValue), type(minValue)))

        if maxValue is not None and not isinstance(maxValue,\
                types.FloatType):
            raise DefinitionError("maxValue "\
                    "'%s' must be a float, but was %s" %\
                    (str(maxValue), type(maxValue)))

        if minValue is not None and maxValue is not None and\
                maxValue < minValue:
            raise DefinitionError("maxValue cannot be less than minValue")

        self.minValue = minValue
        self.maxValue = maxValue

    def validate(self, value):
        """Validates if the given value is a valid float.

        :type value: float
        :param value: The value to validate.
        """
        if not isinstance(value, types.FloatType):
            raise ValidationError("%s: expected float but was %s" %\
                    (str(value), type(value)))
        if self.minValue is not None and value < self.minValue:
            raise ValidationError("%s is less than minimum %s" %\
                    (str(value), self.minValue))
        if self.maxValue is not None and value > self.maxValue:
            raise ValidationError("%s is greater than maximum %s" %\
                    (str(value), self.maxValue))

class PositiveLongType(LongType):
    """A type representing a positive long.

    :type maxValue: int
    :param maxValue: The maximum size of longs of this type. Defaults
                     to None (unspecified).
    """
    def __init__(self, maxValue=None):
        super(PositiveLongType, self).__init__(0L, maxValue)

class NonzeroPositiveLongType(LongType):
    """A type representing a positive non-zero long. 

    :type maxValue: int
    :param maxValue: The maximum size of longs of this type. Defaults
                     to None (unspecified).
    """
    def __init__(self, maxValue=None):
        super(NonzeroPositiveLongType, self).__init__(1L, maxValue)

class PositiveFloatType(FloatType):
    """A type representing a positive float.

    :param maxValue: The maximum size of floats of this type. Defaults
    to None (unspecified)."""
    def __init__(self, maxValue=None):
        super(PositiveFloatType, self).__init__(0.0, maxValue)

class BooleanType(BaseType):
    """A type representing a boolean."""
    def __init__(self):
        pass

    def validate(self, value):
        """Validates if the given value is a valid boolean.

        :type value: bool
        :param value: The value to validate.
        """
        if not isinstance(value, types.BooleanType):
            raise ValidationError("%s: expected boolean but was %s" %\
                    (str(value), type(value)))

class ListType(BaseType):
    """A type representing a list of `:class:BaseType`s.

    :param element_type: A `:class:BaseType` shared by all elements of the
    list.
    """
    def __init__(self, elementType):
        if not isinstance(elementType, BaseType):
            raise DefinitionError("elementType must be an instance of BaseType")

        self.elementType = elementType

    def validate(self, value):
        """Validates if the given value is a valid list, and that each element
        of the list is valid with respect to the elementType.

        :type value: list
        :param value: The value to validate.
        """
        if not isinstance(value, types.ListType):
            raise ValidationError("%s: expected list but was %s" %\
                    (str(value), type(value)))

        for v in value:
            self.elementType.validate(v)

class MapType(BaseType):
    """A type representing a map of key-value pairs. Keys must be
    :class:`StringType`\s, while values can be any subclass of
    :class:`BaseType`.

    :type keyType: StringType
    :param keyType: The type to validate keys against.

    :type valueType: BaseType
    :param valueType: The type shared by values in this map.
    """
    def __init__(self, keyType, valueType):
        if not isinstance(keyType, StringType):
            raise DefinitionError("keyType must be an instance of StringType")
        if not isinstance(valueType, BaseType):
            raise DefinitionError("valueType must be a valid type")

        self.keyType = keyType
        self.valueType = valueType

    def validate(self, value):
        """Validates if the given value is a valid map, and that each key-value
        pair is valid with respect to the keyType and valueType.

        :type value: dict
        :param value: The value to validate.
        """
        if not isinstance(value, types.DictType):
            raise ValidationError("%s: expected dict but was %s" %\
                    (str(value), type(value)))

        for k,v in value.iteritems():
            self.keyType.validate(k)
            self.valueType.validate(v)

class DatetimeType(BaseType):
    """A type representing a datetime."""
    def __init__(self):
        pass

    def validate(self, value):
        """Validates if the given value is a valid datetime string according to
        the format.

        :type value: datetime
        :param value: The value to validate.
        """
        if not isinstance(value, datetime.datetime):
            raise ValidationError("%s: expected datetime but was %s" %\
                    (str(value), type(value)))

class FormationType(object):
    """Represents a complex type. Instances of this class define the fields
    for the formation along with some additional metadata about it. They can
    output values for all the constituent fields of the formation in the form
    of a dictionary of field name to field value.

    :type name: string
    :param name: The name of the formation.

    :type description: string
    :param description: A short description of the formation.

    :type fields: list
    :param fields: A list of fields that make up this formation. Duplicate
                   names are not allowed.
    """
    def __init__(self, name, description, fields):
        #: The name of the formation.
        self.name = name

        #: A description of the formation.
        self.description = description

        if len(fields) == 0:
            raise DefinitionError("fields must contain at least one field")

        #: The :class:`Field`s that make up this Formation.
        self.fields = {}
        for field in fields:
            if field.name in self.fields:
                raise DefinitionError("duplicate field: %s" % field.name)
            self.fields[field.name] = field

    def validate(self, value):
        """Validates a dictionary against this formation type.
        
        :param value: The dictionary to validate.
        """
        validate_fields(self.fields, value, self.name)

