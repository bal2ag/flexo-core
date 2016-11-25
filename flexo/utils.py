from .errors import ValidationError

def validate_fields(fields, to_validate, context_message=None):
    """Validate that the given dictionary is valid with respect to the given
    field definitions (dictionary of field name to :class:`flexo.model.Field`)
    by ensuring that there are no keys which are not fields, that all required
    fields are present, and that each present field is valid w.r.t. that
    field's base type.

    :param fields: Dictionary of field name to :class:`flexo.model.Field`.
    :param to_validate: The dictionary to validate against the field
    definitions.
    :param context_message: An optional message to prepend to validation
    errors.
    """
    context_message = "" if context_message is None else\
            "%s: " % context_message

    for k,v in to_validate.iteritems():
        if k not in fields:
            raise ValidationError("%sinvalid field %s" %\
                    (context_message, k))
        fields[k].validate(v)

    required_fields = set([f.name for f in fields.values() if f.required])
    missing = required_fields - set(to_validate.keys())
    if len(missing) > 0:
        raise ValidationError("%smissing required fields: %s" %\
                (', '.join(missing)))
