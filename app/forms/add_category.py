from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddCategoryForm(FlaskForm):
    name = StringField(label='أسم القائمة', validators=[DataRequired()])
    submit = SubmitField(label='Add Category')