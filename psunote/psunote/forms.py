from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.orm import model_form
from models import Note, Tag
from psunote import db  # หรือ import db จากไฟล์ที่มี SQLAlchemy()

BaseNoteForm = model_form(
    Note,
    base_class=FlaskForm,
    exclude=["created_date", "updated_date"],
    db_session=db.session
)

class TagForm(FlaskForm):
    name = StringField("Tag Name", validators=[DataRequired()])
    submit = SubmitField("Save")
