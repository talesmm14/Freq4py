from typing_extensions import Required
from api.model.lost_day import Lost_Day
from commissioned_schema import Commissioned_Schema
from trainee_schema import Trainee_Schema
from flask_marshmallow import Schema
from marshmallow.fields

class Sheet_Schema(Schema):
    class Meta:
        fields = [
            "path", 
            "save_path", 
            "year", 
            "month", 
            "key_words", 
            "not_working_days"
        ]

        path, save_path = Str(required=True)
        year, month = Number(required=True)
        key_words = {"Trainee": Trainee_Schema, "Commissioned": Commissioned_Schema}
        not_working_days = Nested(Lost_Day, many=True)