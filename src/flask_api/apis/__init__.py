from flask import Blueprint
from flask_restplus import Api

from .people import api as people

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    blueprint,
    title='People',
    version='1.0',
    description='Get People Information'
)

api.add_namespace(people)
