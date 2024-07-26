from marshmallow import ValidationError


def length_validate(value, max_length: int = None, min_length: int = None):
    if max_length:
        if len(value) > max_length:
            raise ValidationError(f"Length must not exceed {max_length} characters.")

    if min_length:
        if len(value) < min_length:
            raise ValidationError(f"Length must not be less than {min_length} characters.")
            