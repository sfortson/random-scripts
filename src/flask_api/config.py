import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Configure the SQLAlchemy part of the app instance
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", True)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////" + os.path.join(basedir, "people.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS", False
    )
