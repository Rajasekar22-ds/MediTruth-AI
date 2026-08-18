from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, FileField
from wtforms.validators import Length
from flask_wtf.file import FileAllowed

class OriginalTextForm(FlaskForm):
    from wtforms.validators import Optional, Length

    original_text = TextAreaField(
        'Original Text',
        validators=[Optional(), Length(max=10000)],
        render_kw={'placeholder': 'Enter text OR upload image'}
    )


    image = FileField(
        'Upload Medical News Image',
        validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')]
    )

    predict = SubmitField('Predict')

