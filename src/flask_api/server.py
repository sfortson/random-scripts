from datetime import datetime

from flask import Flask, request, render_template, Blueprint
from flask_restplus import Api, Resource, fields

# Create the application instance
app = Flask(__name__)

# Read the swagger.yml file to configure the endpoints
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
ns = api.namespace('people', description='People APIs', path='/')

app.register_blueprint(blueprint)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrel",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


model = api.model('People Model', {
  'fname': fields.String(required=True, description="First name"),
  'lname': fields.String(required=True, description='Last name')
})


@app.route('/')
def home():
    return render_template("home.html")


@ns.route('/people')
class AllPeople(Resource):
    # Create a handler for our read (GET) people
    @staticmethod
    def get():
        """
        This function responds to a request for /api/people with complete lists of people

        :return: sorted list of people
        """
        # Create the list of people from our data
        return [PEOPLE[key] for key in sorted(PEOPLE.keys())], 200

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def post(self):
        first_name = request.json['fname']
        last_name = request.json['lname']

        new_person = {}

        try:
            new_person = {
                last_name: {
                    'fname': first_name,
                    'lname': last_name,
                    'timestamp': get_timestamp()
                }
            }

            PEOPLE.update(new_person)

        except Exception as e:
            ns.abort(400, e.__doc__, status='Could not add person')

        return {
            'status': 'Person added',
            'person': new_person
        }, 200


# noinspection PyUnresolvedReferences
@ns.route('/people/<string:lname>')
class OnePerson(Resource):
    @staticmethod
    def lname_not_found(lname):
        ns.abort(404, "Person with last name {lname} not found".format(lname=lname))

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'lname': 'Specify the last name associated with the person'})
    def get(self, lname):
        """
        This function responds to a request for /api/people/{lname} with one matching person from people

        :param lname:   last name of person to find
        :return:        person matching last name
        """
        # Does the person exist in people?
        if lname in PEOPLE:
            person = PEOPLE.get(lname)

            return person, 200

        # otherwise, nope, not found
        else:
            self.lname_not_found(lname)

        return

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def put(self, lname):
        """
        Defines a unique URL to update an existing order

        :param lname:
        :return: person object
        """
        first_name = request.json['fname']

        print(lname, first_name)

        if lname in PEOPLE:
            new_person = {'fname': first_name, 'lname': lname, 'timestamp': get_timestamp()}
            PEOPLE[lname].update(new_person)

            return {
                'status': 'Person updated',
                'person': new_person
            }, 200

        self.lname_not_found(lname)

    def delete(self, lname):
        last_name = lname

        if last_name not in PEOPLE:
            self.lname_not_found(last_name)

        person = PEOPLE[last_name]

        del(PEOPLE[last_name])

        return {'status': 'Removed {}'.format(last_name),
                'person_removed': person}, 200


if __name__ == '__main__':
    app.run(debug=True)
