from flask import Flask, render_template
from .form import Formulario


def create_app():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "eu-amo-programar"

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = Formulario()

        if form.validate_on_submit():
             pass

        return render_template("login.html", form=form)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
