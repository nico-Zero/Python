from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

##CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
ckeditor = CKEditor()

db.init_app(app)
ckeditor.init_app(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


with app.app_context():
    db.create_all()


##WTForm
class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Body", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    data = list(db.session.query(BlogPost))
    posts = [i.to_dict() for i in data]
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id).to_dict()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["POST", "GET"])
def make_post():
    form = PostForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        blog = BlogPost(
            title=data["title"],
            subtitle=data["subtitle"],
            date=date.today().strftime("%B %d, %Y"),
            body=data["body"],
            author=data["author"],
            img_url=data["img_url"],
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("show_post", post_id=blog.id))

    return render_template("make_post.html", form=form, is_edit=False)


@app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)

    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body,
    )

    if form.validate_on_submit():
        post.title = form.data["title"]
        post.subtitle = form.data["subtitle"]
        post.author = form.data["author"]
        post.img_url = form.data["img_url"]
        post.body = form.data["body"]

        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))

    return render_template("make_post.html", form=form, is_edit=True)


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    db.session.delete(db.get_or_404(BlogPost, post_id))
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
