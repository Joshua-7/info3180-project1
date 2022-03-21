from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField,TextAreaField,DecimalField,IntegerField,SelectField
from wtforms.validators import InputRequired


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired()])
    bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    proptypes=["House","Appartment","Open Lot","Commercial"]
    proptype = SelectField('Proptype', validators=[InputRequired()], choices=proptypes)
    description = TextAreaField('Description', validators=[InputRequired()])
    img =FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
