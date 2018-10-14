from db import db


class UserSkillAssociation(db.Model):

    __tablename__ = 'user_skill'
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'), primary_key=True)
    sid = db.Column(db.Integer, db.ForeignKey('skills.sid'), primary_key=True)

    user = db.relationship('UserModel', back_populates='skills')
    skill = db.relationship('SkillModel', back_populates='users')
