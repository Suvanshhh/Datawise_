from marshmallow import ValidationError

def validate_schema(schema, data):
    try:
        return schema.load(data)
    except ValidationError as err:
        return None, err.messages
