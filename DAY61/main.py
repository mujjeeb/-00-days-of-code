from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')


USER_EMAIL = "admin@email.com"
USER_PASSWORD = "123456789"

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["Get", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        input_email = login_form.email.data
        input_password = login_form.password.data
        if input_email == USER_EMAIL and input_password == USER_PASSWORD:
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
