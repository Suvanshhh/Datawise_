from marshmallow import Schema, fields

class QualityLogSchema(Schema):
    status = fields.Str(required=True, validate=lambda x: x in ['PASS', 'FAIL'])
    details = fields.Str()
    timestamp = fields.DateTime(dump_only=True)
    dataset_id = fields.Str(required=True)
