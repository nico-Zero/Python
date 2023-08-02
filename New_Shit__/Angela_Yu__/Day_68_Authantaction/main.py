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

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def user_loader(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)  # type: ignore


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        try:
            user = User(
                name=request.form.get("name"),
                email=request.form.get("email"),
                password=generate_password_hash(
                    str(request.form.get("password")), salt_length=12
                ),
            )  # type: ignore
            db.session.add(user)
            db.session.commit()
        except:
            flash("This email is already registered.")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("secrets", id=user.id))

    return render_template("register.html", logged_in=current_user.is_authenticated)  # type: ignore


@app.route("/login", methods={"GET", "POST"})
def login():
    if request.method == "POST":
        try:
            user_data = db.session.execute(
                db.select(User).where(User.email == request.form.get("email"))
            ).scalar_one()
        except:
            flash("This email does not exist in our database.")
            return redirect(url_for("register"))

        if check_password_hash(user_data.password, str(request.form.get("password"))):
            login_user(user_data)
            return redirect(url_for("secrets"))
        else:
            flash("Invalid password")
            return redirect(url_for("login"))

    return render_template("login.html", logged_in=current_user.is_authenticated)  # type: ignore


@app.route("/secrets")
@login_required
def secrets():
    user_name = current_user.name  # type: ignore
    return render_template(
        "secrets.html",
        logged_in=True,
        name=user_name,
        logged_in=current_user.is_authenticated,  # type: ignore
    )


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory(
        "static",
        path="files/cheat_sheet.pdf",
    )


if __name__ == "__main__":
    app.run(debug=True)
