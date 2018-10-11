from db import db


class ProjectModel(db.Model):
    """docstring for ProjectModel"""

    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80))
    owner = db.Column(db.String(80))
    # roles = db.Column()

    def __init__(self, pname, owner):
        self.pname = pname
        self.owner = owner

    def json(self):
        return {'pname': self.pname, 'owner': self.owner}

    @classmethod
    def find_by_name(cls, pname):
        return cls.query.filter_by(pname=pname).first()  # SELECT * FROM items WHERE pname=pname

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
