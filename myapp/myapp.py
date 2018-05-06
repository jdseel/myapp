from flask import Flask, render_template, request
import random

app = Flask(__name__)
greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user/<string:username>')
def users(username):
    #return "<h1>Hello %s</h1>"% username
    return render_template('user.html', uname=username)

@app.route('/form')
def form():
    return render_template('form-basics.html')

@app.route('/form-demo', methods=['GET','POST'])
def form_demo():
    if request.method == 'GET':
        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True, port=4500)
