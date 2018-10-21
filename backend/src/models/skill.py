from db import db


class SkillModel(db.Model):

    __tablename__ = 'skills'
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)

    roles = db.relationship("RoleSkillAssociation", back_populates="skill")
    users = db.relationship("UserSkillAssociation", back_populates="skill")

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name}

    # @classmethod
    # def fine_by_title(cls, title):
    #     return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
