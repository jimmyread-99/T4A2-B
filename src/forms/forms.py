from flask_wtf import FlaskForm

from wtforms.fields.html5 import DateField
from wtforms import validators, SubmitField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    name = StringField('Name', [Length(min=4, max=25)])
    email = StringField('Email Address', [Length(min=6, max=35)])
    password = PasswordField('New Password', [DataRequired(), Length(min=6)])


class PasswordRest(FlaskForm):
    name = StringField('Name', [Length(min=4, max=25)])
    email = StringField('Email Address', [Length(min=6, max=35)])
    password = PasswordField('New Password', [DataRequired(), Length(min=6)])


class InfoForm(FlaskForm):
    date = DateField("Start Date", format='%Y-%m-%d',
                     validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')


class UserUpdateForm(FlaskForm):
    email = StringField("email")
    name = StringField("name")
    membership = StringField("membership")
    valid = StringField("valid")
    valid_till = StringField("valid_till")
    submit = SubmitField('edit')
