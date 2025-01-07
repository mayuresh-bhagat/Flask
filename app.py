from flask import Flask, Response, request, render_template, session, make_response

app = Flask(__name__, template_folder="templates")
app.secret_key = "SECRET KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_session')
def set_session():
    session['name'] = "Mayuresh"
    session['age']  = 21

    return render_template('index.html', message="Session set successfully")


@app.route('/get_session')
def get_session():
    if 'name' in session.keys() and 'age' in session.keys():
        name = session.get('name')
        age  = session.get('age')

        return render_template('index.html', message=f"Name: {name}, Age: {age}")
    else :
        return render_template('index.html', message="No seession found")
    
@app.route('/delete_session')
def delete_session():
    session.clear()
    return render_template('index.html', message="Session deleted successfully")

@app.route('/set_cookies')
def set_cookies():
    response = make_response(render_template('index.html', message="Cookies set successfully"))
    response.set_cookie('name', 'Mayuresh')
    response.set_cookie('age', '21')
    return response

@app.route('/get_cookies')
def get_cookies():
    if 'name' in request.cookies.keys() and 'age' in request.cookies.keys():
        name = request.cookies.get('name')
        age = request.cookies.get('age')
        return render_template('index.html', message=f"Name: {name}, Age: {age}")
    else :
        return render_template('index.html', message="No cookies found")

@app.route('/delete_cookies')
def delete_cookies():
    response = make_response(render_template('index.html', message="Cookies deleted"))
    response.set_cookie('name', expires=0)
    response.set_cookie('age', expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
