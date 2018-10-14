from db import db


class RoleSkillAssociation(db.Model):

    __tablename__ = 'role_skill'
    # id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey('roles.rid'), primary_key=True)
    sid = db.Column(db.Integer, db.ForeignKey('skills.sid'), primary_key=True)

    role = db.relationship('RoleModel', back_populates='skills')
    skill = db.relationship('SkillModel', back_populates='roles')
