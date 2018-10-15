from db import db

from models.project_role import ProjectRoleAssociation
from models.role_skill import RoleSkillAssociation


class ProjectModel(db.Model):
    """docstring for ProjectModel"""

    __tablename__ = 'projects'
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String())

    owner = db.relationship('UserModel', back_populates='owned_projects')
    members = db.relationship('UserJoinedProjectAssociation', back_populates='project')
    roles = db.relationship('ProjectRoleAssociation', back_populates='project')

    def __init__(self, pname, description, owner_id):
        self.pname = pname
        self.description = description
        self.owner_id = owner_id

    def json(self):
        return {'pname': self.pname, 'description': self.description, 'owner_id': self.owner_id}

    @classmethod
    def find_by_name(cls, pname):
        return cls.query.filter_by(pname=pname).first()  # SELECT * FROM items WHERE pname=pname

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
