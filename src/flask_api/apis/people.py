from flask import make_response, request
from flask_restplus import Namespace, Resource, fields
from marshmallow import ValidationError

from config import db
from models import Person, PersonSchema

api = Namespace('people', description='People related operations')

model = api.model('People Model', {
  'fname': fields.String(required=True, description="First name"),
  'lname': fields.String(required=True, description='Last name')
})


@api.route('/')
class AllPeople(Resource):
    # Create a handler for our read (GET) people
    @staticmethod
    def get():
        """
        This function responds to a request for /api/people with complete lists of people

        :return: sorted list of people
        """
        # Create the list of people from our data
        people = Person.query.order_by(Person.lname).all()

        # Serialize the data for the response
        person_schema = PersonSchema(many=True)
        return person_schema.dump(people)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def post(self):
        json_data = request.get_json()
        if not json_data:
            api.abort(404, 'No input data provided')

        schema = PersonSchema()

        try:
            new_person = schema.load(json_data, session=db.session)
        except ValidationError as err:
            api.abort(400, str(err))
            raise

        first_name, last_name = new_person.fname, new_person.lname

        existing_person = Person.query \
            .filter(Person.fname == first_name) \
            .filter(Person.lname == last_name) \
            .one_or_none()

        if existing_person:
            api.abort(409, 'Person {} {} already exists in the database'.format(first_name, last_name))

        db.session.add(new_person)
        db.session.commit()

        return schema.dump(new_person), 201


# noinspection PyUnresolvedReferences
@api.route('/<int:person_id>')
class OnePerson(Resource):
    @staticmethod
    def id_not_found(person_id):
        api.abort(404, "Person with ID: {person_id} not found".format(person_id=person_id))

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'person_id': 'Specify the id associated with the person'})
    def get(self, person_id):
        """
        This function responds to a request for /api/people/{person_id} with one matching person from people

        :param person_id:   id of person to find
        :return:            person matching last name
        """
        # Does the person exist in people?
        person = Person.query.filter(Person.person_id == person_id).one_or_none()

        if not person:
            api.abort(404, 'Person not found for ID: {}'.format(person_id))

        person_schema = PersonSchema()
        return person_schema.dump(person)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def put(self, person_id):
        """
        Defines a unique URL to update an existing order

        :param person_id:
        :return: person object
        """
        json_data = request.get_json()
        if not json_data:
            api.abort(404, 'No input data provided')

        schema = PersonSchema()

        try:
            new_person = schema.load(json_data, session=db.session)
        except ValidationError as err:
            api.abort(400, str(err))
            raise

        existing_person = Person.query \
            .filter(Person.person_id == person_id) \
            .one_or_none()

        if not existing_person:
            self.id_not_found(person_id)

        new_person.person_id = existing_person.person_id

        db.session.merge(new_person)
        db.session.commit()

        return schema.dump(existing_person), 201

    def delete(self, person_id):
        existing_person = Person.query \
            .filter(Person.person_id == person_id) \
            .one_or_none()

        if not existing_person:
            self.id_not_found(person_id)

        db.session.delete(existing_person)
        db.session.commit()

        return make_response('Removed ID: {}'.format(person_id), 200)
