from db import db


class SkillModel(db.Model):

    __tablename__ = 'skills'
    sid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    roles = db.relationship("RoleSkillAssociation", back_populates="skill")

    def __init__(self, title):
        self.title = title

    def json(self):
        return {'title': self.title}

    # @classmethod
    # def fine_by_title(cls, title):
    #     return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
