from db import db

from models.skill import SkillModel
from models.role_skill import RoleSkillAssociation


class RoleModel(db.Model):

    __tablename__ = 'roles'
    rid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())

    skills = db.relationship('RoleSkillAssociation', back_populates='role')
    projects = db.relationship('ProjectRoleAssociation', back_populates='role')

    def __init__(self, title, description, skills=[]):
        self.title = title
        self.description = description
        self.skillList = []
        for skill in skills:
            s = SkillModel(skill['name'])
            self.skillList.append(s)

    def json(self):
        return {
            'rid': self.rid,
            'title': self.title,
            'description': self.description,
            'skills': self.skills
        }

    # @classmethod
    # def fine_by_title(cls, title):
    #     return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        for skill in self.skillList:
            a = RoleSkillAssociation()
            a.skill = skill
            self.skills.append(a)

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
