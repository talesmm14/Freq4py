from flask_marshmallow import Schema
from marshmallow.fields import Nested, Str, Number

class Commissioned_Schema(Schema):
    class Meta:
        fields = ["name",
        "capacity",
        "effective_position",
        "commissioned_position",
        "registration",
        "immediate_boss",
        "mediate_boss"]

    name, capacity, effective_position, commissioned_position, registration, immediate_boss, mediate_boss = Str()
