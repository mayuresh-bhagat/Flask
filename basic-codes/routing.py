from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')                              ## url path
def index():
    return 'Hello World'


@app.route('/hello')
def hello():                
    return "Hello world page 2"


@app.route('/with_status_code')             ## url path with output status code
def with_status_code():
    return "This is with status code", 200

@app.route('/greed/<name>')                 ## url path with variable
def greed(name):
    return f"Hello, {name}"

@app.route('/add/<int:number1>/<int:number2>')            ## url path with int variable
def add(number1, number2):
    return f"Sum of {number1} and {number2} is {number1 + number2}"


@app.route('/handle_post', methods=['POST'])            ## url path with post method
def handle_post():
    return "hello this is post method request"


@app.route('/handle_both_request', methods=['GET', 'POST'])            ## url path with both get and post method
def handle_both_request():
    if request.method == 'GET':
        return "This is get request"
    elif request.method == 'POST':
        return "This is post request"

@app.route('/handle_get_url')                        ## url path with get method request
def handle_get_url():
    if request.args.get('uname') and request.args.get('greed'):
        name = request.args.get('uname')
        greed = request.args['greed']
        return f"{greed}, {name}"
    else :
        return "Please provide name and greed"

@app.route('/custom_response')                        ## rotue with custom response
def custom_response():
    response = make_response('This is custom response')
    response.status_code = 200
    response.headers['content-type'] = 'application/json'
    return response



if __name__ == "__main__":
    app.run(debug=True)


