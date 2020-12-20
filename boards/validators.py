from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

class CreateBoardSchema(Inputs):
   json = [JsonSchema(schema={
   'type': 'object',
   'properties': {
       'title': {
           'type': 'string'
       }
   },
   'required': ['title']
})]