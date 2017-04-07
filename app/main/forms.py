<<<<<<< HEAD
from flask_wtf import Form
=======
from flask_wtf import FlaskForm
>>>>>>> upstream/master
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


<<<<<<< HEAD
class NameForm(Form):
=======
class NameForm(FlaskForm):
>>>>>>> upstream/master
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


<<<<<<< HEAD
class EditProfileForm(Form):
=======
class EditProfileForm(FlaskForm):
>>>>>>> upstream/master
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


<<<<<<< HEAD
class EditProfileAdminForm(Form):
=======
class EditProfileAdminForm(FlaskForm):
>>>>>>> upstream/master
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


<<<<<<< HEAD
class PostForm(Form):
=======
class PostForm(FlaskForm):
>>>>>>> upstream/master
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')


<<<<<<< HEAD
class CommentForm(Form):
=======
class CommentForm(FlaskForm):
>>>>>>> upstream/master
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')
