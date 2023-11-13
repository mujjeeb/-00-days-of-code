
from flask import Flask, render_template, request
import requests
import datetime

x = datetime.datetime.now()

BIN_URL = 'https://api.jsonbin.io/v3/b'
BIN_ID = "634d8c840e6a79321e2bb4a6"

posts = requests.get(f"{BIN_URL}/{BIN_ID}").json()['record']

string_year = f"{(x.strftime(' %B'))} {x.strftime('%d')}, {x.strftime('%Y')}"

app = Flask(__name__)


@app.route('/')
def get_posts():
    return render_template('index.html', all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            requested_post_image = f"/static/assets/img/{index}.jpg"
            print(requested_post_image)
    return render_template('post.html', post=requested_post, image_url=requested_post_image)





@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
