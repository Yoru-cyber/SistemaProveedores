from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, DecimalField, validators
from wtforms.validators import DataRequired
PLACE_HOLDERS_EXAMPLE = ['Farmatodo', 'Alcohol', '300', '5.16', '12/10/2023']
STYLE_NAME = {"class": "form-control", "type": "text", "placeholder": PLACE_HOLDERS_EXAMPLE[0], "style": "max-width: fit-content;"}
STYLE_PRODUCT = {"class": "form-control", "type": "text", "placeholder": PLACE_HOLDERS_EXAMPLE[1]}
STYLE_UNITS = {"class": "form-control", "type": "number", "placeholder": PLACE_HOLDERS_EXAMPLE[2], "style": "max-width: fit-content;"}
STYLE_PRICE = {"class": "form-control", "type": "number", "placeholder": PLACE_HOLDERS_EXAMPLE[3]}
STYLE_DATE = {"class": "form-control", "type": "date", "placeholder": PLACE_HOLDERS_EXAMPLE[4]}
STYLE_SUBMIT = {"class": "btn btn-primary", "style": "margin-bottom: 10px;"}
class VentaForm(FlaskForm):
    nameProvider = StringField('nameProvider', validators=[DataRequired(), validators.Length(max=20)], render_kw=STYLE_NAME)
    nameProduct = StringField('nameProduct', validators=[DataRequired(), validators.Length(max=20)], render_kw=STYLE_PRODUCT)
    unitsProduct = IntegerField('unitsProduct', validators=[DataRequired()], render_kw=STYLE_UNITS)
    pricePerUnit = DecimalField('pricePerUnit', validators=[DataRequired()], render_kw=STYLE_PRICE)
    date = DateField('date', validators=[DataRequired()], render_kw=STYLE_DATE)
    submit = SubmitField('Submit', render_kw=STYLE_SUBMIT, validators=[DataRequired()])