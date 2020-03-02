import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


# Create the application instance
app = Flask(__name__)

# Read the swagger.yml file to configure the endpoints
# blueprint = Blueprint('api', __name__, url_prefix='/api')
# api = Api(blueprint)
# ns = api.namespace('people', description='People APIs', path='/api')
# api.add_namespace(people)

# app.register_blueprint(blueprint)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
