from db import db


class RoleModel(db.Model):

    __tablename__ = 'roles'
    rid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())

    skills = db.relationship('RoleSkillAssociation', back_populates='role')
    projects = db.relationship('ProjectRoleAssociation', back_populates='role')

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def json(self):
        return {'title': self.title, 'description': self.description}

    # @classmethod
    # def fine_by_title(cls, title):
    #     return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
