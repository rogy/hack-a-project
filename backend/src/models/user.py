from db import db
from models.skill import SkillModel
from models.user_skill import UserSkillAssociation
from models.user_joined_project import UserJoinedProjectAssociation


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    skills = db.relationship('UserSkillAssociation', back_populates='user')
    owned_projects = db.relationship('ProjectModel', back_populates='owner')
    joined_projects = db.relationship('UserJoinedProjectAssociation', back_populates='member')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
