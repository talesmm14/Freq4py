from flask_marshmallow import Schema
from marshmallow.fields import Str

class Trainee_Schema(Schema):
    class Meta:
        fields = [
            "name", "supervisor", "supervisor_registration"
        ]

        name, supervisor, supervisor_registration = Str()