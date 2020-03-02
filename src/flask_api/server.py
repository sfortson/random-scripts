from flask import render_template
from apis import blueprint as people

from config import app


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.register_blueprint(people)
    app.run(debug=True)
