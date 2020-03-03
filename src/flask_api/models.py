from datetime import datetime

from config import db, ma
from marshmallow import post_load


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)
