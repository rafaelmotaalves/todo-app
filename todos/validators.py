from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from wtforms.validators import DataRequired

class CreateTodoSchema(Inputs):
    rule = {
        'board_id': [DataRequired()]
    }
    json = [JsonSchema(schema={
        'type': 'object',
        'properties': {
            'title': {
               'type': 'string'
            },
            'description': {
                'type': 'string'
            }
        },
        'required': ['title']
})]

class UpdateTodoSchema(Inputs):
    rule = {
        'id': [DataRequired()]
    }
    json = [JsonSchema(schema={
        'type': 'object',
        'properties': {
            'title': {
                'type': 'string'
            },
            'description': {
                'type': 'string'
            },
            'status': {
                'type': 'string',
                'enum': ['TODO', 'DOING', 'DONE']
            }
        },
        'required': []
    })]
