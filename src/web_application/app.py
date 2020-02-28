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


@app.route("/city")
def city_list():
    # Get the unique city values from the database
    cities = School.query.with_entities(School.city).distinct().all()
    # They're in a weird list of one-element lists, though, like
    # [['Yonkers'],['Brooklyn'],['Manhattan']]
    # so we'll take them out of that
    cities = [city[0].title() for city in cities]
    # Now that they're both "New York," we can now dedupe and sort
    cities = sorted(list(set(cities)))
    return render_template("cities.html", cities=cities)


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


@app.route('/zip')
def zip_list():
    zip_codes = School.query.with_entities(School.ZIP).distinct().all()
    zip_codes = [zip_code[0] for zip_code in zip_codes]
    zip_codes = sorted(list(set(zip_codes)))
    return render_template('zip_codes.html', zip_codes=zip_codes)


if __name__ == '__main__':
    app.run(debug=True)
