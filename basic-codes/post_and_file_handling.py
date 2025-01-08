import os
from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import uuid

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # return "login code"
        username = request.form.get('username')
        password = request.form.get('password')

        
        if 'username' in request.form.keys() and 'password' in request.form.keys():
            if username == 'mayuresh' and password == '123456':
                return "Success"
            else :
                return "Fail"
        else :
            return "Invalid Request"
    else: 
        return render_template('post_and_file_handling.html')


@app.route('/file', methods=['POST'])
def file():
    file = request.files['file']
    file_extension = os.path.splitext(file.filename)[1]
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file_extension == '.xlsx':
        df = pd.read_excel(file)
        return df.to_html()
    
    return "file code"


@app.route('/convert_to_csv', methods=['POST'])
def convert_to_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype="text/csv",
        headers={
            'Content-Disposition': 'attachment; filename=export.csv'
        }

    )

    return response

@app.route('/convert_to_csv_two', methods=['POST'])
def convert_to_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'

    df.to_csv(os.path.join('downloads', filename))

    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='export.csv')


@app.route('/handle_post_js', methods=['POST'])
def handle_post_js():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting} {name}')

    return jsonify({'message': 'Successfully written'})



if __name__ == '__main__':
    app.run(debug=True)