from flask_api.config import Config
from flask import render_template
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)

    register_routes(app)

    return app


def register_routes(app):
    @app.route('/')
    def home():
        return render_template("home.html")

    from flask_api.apis import blueprint as people
    app.register_blueprint(people)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
