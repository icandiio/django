import json

from django.db import models


class JSONField(models.Field):
    description = "JSONField"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    def db_type(self, connection):
        """call by django when create table"""
        return "json"

    def from_db_value(self, value, expression, connection, context):
        # load data from db and convert to python object
        # called in all circumstances when the data is loaded from the database
        if value is None:
            return value
        return self.to_python(value)

    def to_python(self, value):
        # called by deserialization and during the clean() method used from forms
        if isinstance(value, dict):
            return value
        if isinstance(value, list):
            return json.loads(value)
        if isinstance(value, str):
            return json.loads(value)
        if value is None:
            return value

        raise Exception("Value Type Error")

    def get_prep_value(self, value):
        # convert Python objects back to query values and prepare save data to db
        if isinstance(value, dict):  # json object
            return json.dumps(value)
        if isinstance(value, list):  # json array
            return json.dumps(value)
        if isinstance(value, str):
            return json.dumps(value)
        if value is None:
            return value
        raise Exception("Value Type Error")
