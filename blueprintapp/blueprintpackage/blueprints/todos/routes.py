from flask import request, render_template, redirect, url_for, Blueprint
from blueprintpackage.app import db
from blueprintpackage.blueprints.todos.models import Todo

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
    todos = Todo.query.all()
    return render_template('todos/index.html', Todos=todos)

@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('todos/create.html')
    
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description') if 'description' in request.form.keys() else None
        done = True if 'done' in request.form.keys() else False

        todo = Todo(title=title, description=description, done=done)
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todos.index'))