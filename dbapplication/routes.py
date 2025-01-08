from flask import render_template, request, redirect, url_for
from models import Person, User
from flask_login import login_user, logout_user, current_user, login_required

def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            if 'username' in request.form.keys() and 'password' in request.form.keys():
                username = request.form.get('username')
                password = request.form.get('password')

                hashed_password = bcrypt.generate_password_hash(password)

                user = User(username=username, password=hashed_password)

                db.session.add(user)
                db.session.commit()
                # session['message'] == 'User Created Successfully'
                return redirect(url_for('index'))
            else :
                return redirect(url_for('signup'))
            

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            if 'username' in request.form.keys() and 'password' in request.form.keys():
                username = request.form.get('username')
                password = request.form.get('password')
                
                user = User.query.filter(User.username == username).first()
                if user == None:
                    return render_template('login.html', message='User not found')
                else :
                    if bcrypt.check_password_hash(user.password, password):
                        login_user(user)
                        return redirect(url_for('index'))
                    else:
                        return 'Failed'
            
            else :
                return redirect(url_for('login'))
    
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/secret')
    @login_required
    def secret():
        return 'Secret Page'



    
    # for DB Application
    @app.route('/create_user', methods=['GET', 'POST'])
    def create_user():
        if request.method == 'GET':
            persons = Person.query.all()
            return render_template('index.html', Persons=persons)
        
        elif request.method == 'POST':
            name = request.form['name']
            age = int(request.form['age'])
            job = request.form['job']

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            persons = Person.query.all()
            return render_template('index.html', Persons=persons)
        

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()

        db.session.commit()

        persons = Person.query.all()
        return render_template('index.html', Persons=persons)
    
    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()

        return render_template('details.html', person=person)
    