from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # skills = db.relationship('UserSkillAssociation', back_populates='user')
    # owned_projects = db.relationship('ProjectModel', back_populates='owner')
    # joined_projects = db.relationship('UserJoinedProjectAssociation', back_populates='member')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class ProjectModel(db.Model):
    """docstring for ProjectModel"""

    __tablename__ = 'projects'
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String())

    def __init__(self, pname, description, owner_id):
        self.pname = pname
        self.description = description
        self.owner_id = owner_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


db.create_all()

user = UserModel("abc", "asdf")

something = ProjectModel("name", "description", 1)
something.save_to_db()

something = ProjectModel("name1", "description", 1)
something.save_to_db()

something = ProjectModel("name2", "description", 1)
something.save_to_db()

for item in something.query.all():
    print(item.pname)
