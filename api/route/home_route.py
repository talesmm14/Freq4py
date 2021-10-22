from http import HTTPStatus
from flask import Blueprint
from api.schema.home_schema import Home_Schema
from flasgger import swag_from
from api.model import commissioned, sheet, trainee
from api.schema import commissioned_schema, sheet_schema, trainee_schema
home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Bem vindo ao gerador de folha de frequências',
            'schema': Home_Schema
        }
    }
})

def home():
    result = Home_Schema()
    return Home_Schema().dump(result), 200