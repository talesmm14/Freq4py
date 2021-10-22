from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model import commissioned, sheet, trainee
from api.schema import commissioned_schema, sheet_schema, trainee_schema

sheet_api = Blueprint('api', __name__)

@sheet_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Preencha sua folha',
            'schema': sheet_schema.Sheet_Schema
        }
    }
})

def sheet():
    result = sheet.Sheet()
    return sheet_schema.Sheet_Schema().dump(result), 200