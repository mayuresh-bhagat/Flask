from app import db
from flask_login import UserMixin

class Person(db.Model):
    __tablename__ = 'persons'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Person(pid={self.pid}, name={self.name}, age={self.age}, job={self.job})"
    

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)
    
    def __repr__(self):
        return f"<User:{self.username}, role:{self.role}>"
    
    def get_id(self):
        return self.uid