from db import db


class ProjectRoleAssociation(db.Model):

    __tablename__ = 'project_role'
    # id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey('roles.rid'), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('projects.pid'), primary_key=True)

    role = db.relationship('RoleModel', back_populates='projects')
    project = db.relationship('ProjectModel', back_populates='roles')
