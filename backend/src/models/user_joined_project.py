from db import db


class UserJoinedProjectAssociation(db.Model):

    __tablename__ = 'user_joined_project'
    # id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('projects.pid'), primary_key=True)

    member = db.relationship('UserModel', back_populates='joined_projects')
    project = db.relationship('ProjectModel', back_populates='members')
