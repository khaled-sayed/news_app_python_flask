from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired

class AddArticalForm(FlaskForm):
    title = StringField(label='أسم المقال', validators=[DataRequired()])
    body = TextAreaField(label='محتوي المقال', validators=[DataRequired()])
    img = FileField(label='صورة المقال', validators=[DataRequired()])
    category = SelectField(label='قائمة المقال',choices=[], validators=[DataRequired()])
    submit = SubmitField(label='إضافة المقال')