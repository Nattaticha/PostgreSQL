from flask import Flask, render_template, redirect, url_for, request
from models import db, Note, Tag
from forms import BaseNoteForm, TagForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

# 🔧 1. แก้ไข Note
@app.route("/note/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = BaseNoteForm(obj=note)
    if form.validate_on_submit():
        form.populate_obj(note)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_note.html", form=form)

# 🔧 2. แก้ไข Tag
@app.route("/tag/edit/<int:tag_id>", methods=["GET", "POST"])
def edit_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    form = TagForm(obj=tag)
    if form.validate_on_submit():
        form.populate_obj(tag)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_tag.html", form=form)

# 🗑️ 3. ลบ Note
@app.route("/note/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("index"))

# 🗑️ 4. ลบ Tag
@app.route("/tag/delete/<int:tag_id>", methods=["POST"])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect(url_for("index"))
