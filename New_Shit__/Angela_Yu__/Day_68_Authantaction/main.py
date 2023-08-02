from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(
                str(request.form.get("password")), salt_length=20
            ),
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("secrets", id=user.id))

    return render_template("register.html")


@app.route("/login", methods={"GET", "POST"})
def login():
    if request.method == "POST":
        user_data = db.session.execute(
            db.select(User).where(User.email == request.form["email"])
        ).scalar_one()

        print(user_data)

        return redirect(url_for("secrets", id=user_data.id))
    return render_template("login.html")


@app.route("/secrets/<int:id>")
def secrets(id):
    user_data = db.get_or_404(User, id)
    return render_template("secrets.html", logged_in=True, user=user_data)


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/download")
def download():
    return send_from_directory(
        "static",
        path="files/cheat_sheet.pdf",
    )


if __name__ == "__main__":
    app.run(debug=True)
