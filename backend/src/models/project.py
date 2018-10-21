from db import db

from models.role import RoleModel
from models.project_role import ProjectRoleAssociation


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

    def __init__(self, pname, description, owner_id, roles=[]):
        self.pname = pname
        self.description = description
        self.owner_id = owner_id
        # print((roles)

        self.roleList = []
        for role in roles:
            # print(type(eval(role)))
            role = eval(role)
            r = RoleModel(role['title'], role['description'], role['skills'])
            self.roleList += [r]
            # self.roles.append(r)

    def json(self):
        return {
            'pid': self.pid,
            'pname': self.pname,
            'description': self.description,
            'owner_id': self.owner_id,
            # 'roles': self.roles.json()
        }

    @classmethod
    def find_by_name(cls, pname, owner_id):
        return cls.query.filter_by(pname=pname, owner_id=owner_id).first()

    def save_to_db(self):
        for role in self.roleList:
            a = ProjectRoleAssociation()
            a.role = role
            self.roles.append(a)

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
