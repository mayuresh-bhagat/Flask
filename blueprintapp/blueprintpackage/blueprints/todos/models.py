from blueprintpackage.app import db

class Todo(db.Model):
    __tablename__ = 'todo'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Todo {self.title}, Done: {self.done}>"
    
    def get_id(self):
        return self.tid
