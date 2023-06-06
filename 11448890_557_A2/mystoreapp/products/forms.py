from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import ValidationError


def validate_image(form, field):
    allowed_extensions = ['jpg', 'png', 'gif', 'jpeg']
    if field.data:
        if not field.data.filename.lower().endswith(tuple(allowed_extensions)):
            raise ValidationError('Images only please.')
        
class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = FloatField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])

    image_1 = FileField('Image_1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])
    image_2 = FileField('Image_2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])
    image_3 = FileField('Image_3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), validate_image])
