from marshmallow import validate

from marshmallow_jsonapi import fields, Schema

not_blank = validate.Length(min=1, error='Field connect be blank')


class MomentSchema(Schema):
    id = fields.Str(dump_only=True)
    event_date = fields.Date(required=True)
    details = fields.Str(required=True, validate=not_blank)
    created_on = fields.DateTime(dump_only=True)
    updated_on = fields.DateTime(dump_only=True)
    active = fields.Boolean(dump_only=True)

    class Meta:
        type_ = 'moment'
        self_url = '/moment/{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/moments/'
