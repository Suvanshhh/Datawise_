from marshmallow import Schema, fields

class DatasetSchema(Schema):
    name = fields.Str(required=True)
    owner = fields.Str(required=True)
    description = fields.Str()
    tags = fields.List(fields.Str())
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_deleted = fields.Bool(dump_only=True)
