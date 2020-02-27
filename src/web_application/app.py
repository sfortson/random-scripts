# app.py
import os

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('schema', 'schools.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


db.Model.metadata.reflect(db.engine)


class School(db.Model):
    __tablename__ = 'schools_geocoded'
    __table_args__ = {'extend_existing': True}
    LOC_CODE = db.Column(db.String(50), primary_key=True)


@app.route("/")
def index():
    school_count = School.query.count()
    zip_schools = School.query.all()
    return render_template("list.html", count=school_count, schools=zip_schools, location='New York City')


@app.route("/shoelaces")
def shoelaces():
    return "This works now!"


@app.route("/about")
def about():
    return "All about my website!"


@app.route('/city/<city_name>')
def city(city_name):
    city_name = city_name.replace("-", " ")
    schools = School.query.filter_by(city=city_name.upper()).all()
    return render_template("list.html", schools=schools, count=len(schools), location=city_name)


@app.route('/schools/<slug>')
def detail(slug):
    school = School.query.filter_by(LOC_CODE=slug).first()
    return render_template("detail.html", school=school)


@app.route('/zip/<zipcode>')
def zip(zipcode):
    schools = School.query.filter_by(ZIP=zipcode).all()
    return render_template("list.html", schools=schools, count=len(schools), location=zipcode)


if __name__ == '__main__':
    app.run(debug=True)
