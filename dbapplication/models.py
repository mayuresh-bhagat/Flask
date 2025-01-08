from app import db

class Person(db.Model):
    __tablename__ = 'persons'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Person(pid={self.pid}, name={self.name}, age={self.age}, job={self.job})"
