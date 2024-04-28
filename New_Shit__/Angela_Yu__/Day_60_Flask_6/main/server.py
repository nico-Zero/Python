from flask import Flask, render_template, request
from datetime import date
import requests
import json

from email.message import EmailMessage
import smtplib
import ssl

app = Flask(__name__)


@app.route("/")
def home():
    blogs = requests.get("https://api.npoint.io/b319f78fbe9660d688d9")
    blogs.raise_for_status()
    blogs = blogs.json()
    with open("data.json", "w") as data_file:
        data_file.write(json.dumps(blogs, indent=4))

    image = "../static/assets/img/home-bg.jpg"
    year = date.today().year

    return render_template("index.html", img=image, blog_posts=blogs, current_year=year)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    image = "../static/assets/img/contact-bg.jpg"
    year = date.today().year
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = f"""
From:- {email}
Message:-{request.form['message']}"""

        my_email = "zandaxheart955@gmail.com"
        password = "slemixowrmjmezyt"
        subject = f"An Email from {name} by Blog Website."

        print(name, email, phone, message, sep="\n")

        try:
            em = EmailMessage()
            em["From"] = my_email
            em["To"] = email
            em["subject"] = subject
            em.set_content(message)
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(my_email, password)
                smtp.sendmail(my_email, my_email, em.as_string())

            print("successfully sent👌👌")
        except:
            print("Unable to send email.")

        return render_template(
            "contact.html",
            message="successful",
            img=image,
            current_year=year,
            form_=True,
        )
    else:
        return render_template("contact.html", img=image, current_year=year, form_=True)


@app.route("/about")
def about():
    image = "../static/assets/img/about-bg.jpg"
    year = date.today().year

    return render_template("about.html", img=image, current_year=year)


@app.route("/post/<int:blog_id>")
def post(blog_id: int):
    with open("data.json") as data_file:
        blog_data = json.load(data_file)
        blog = [post for post in blog_data if post["id"] == blog_id][0]

    image = "../static/assets/img/post-bg.jpg"
    year = date.today().year

    return render_template("post.html", img=image, post=blog, current_year=year)


@app.route("/page/<int:page_number>")
def page(page_number: int):
    with open("data.json") as data_file:
        blogs = json.load(data_file)

    year = date.today().year
    image = "../static/assets/img/home-bg.jpg"

    return render_template(
        "page.html",
        img=image,
        current_year=year,
        blog_posts=blogs,
        page_=page_number,
        next_page=page_number + 1,
        previous_page=page_number - 1,
    )


if __name__ == "__main__":
    app.run(debug=True)
