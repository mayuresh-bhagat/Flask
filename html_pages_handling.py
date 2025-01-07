from flask import Flask, render_template, url_for, redirect 

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('post_and_file_handling.html')

@app.route('/page2')
def page2():
    name = "Mayuresh"
    age = 22
    mylist = [1, 2, 3, 4, 5]
    return render_template('page2.html', name=name, age=age, mylist=mylist)
    
@app.route('/page1')
def page1():
    return render_template('page1.html', name="Mayuresh")


@app.route('/redirect_')
def redirect_():
    return redirect(url_for('page1'))

@app.template_filter('repeat')
def repeat(s, times):
    return s * times

@app.template_filter('reverse')
def reverse(s):
    return s[::-1]

if __name__ == '__main__':
    app.run(debug=True)