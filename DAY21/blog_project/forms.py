from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

# -------------------------
# Registration Form
# -------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")]
    )

    role = SelectField(
        "Role",
        choices=[
            ("user", "User"),
            ("author", "Author"),
            ("admin","Admin")
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Register")

# -------------------------
# Login Form
# -------------------------
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


# -------------------------
# Create Post Form
# -------------------------
class PostForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(max=200)]
    )

    content = TextAreaField(
        "Content",
        validators=[DataRequired()]
    )

    image = FileField("Post Image", validators=[
    FileAllowed(["jpg", "png", "jpeg"], "Images only!")
    ])

    submit = SubmitField("Publish") 