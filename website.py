from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('static/index.html')

@app.route('/blog')
def blog():
    return render_template('static/blog.html')

@app.route('/cryptocurrency')
def cryptocurrency():
    return render_template('static/cryptocurrency.html')

@app.route('/index2')
def index2():
    return render_template('static/index2.html')

@app.route('/index3')
def index3():
    return render_template('static/index3.html')

@app.route('/mindmap')
def mindmap():
    return render_template('static/mindmap.html')

@app.route('/pics')
def pics():
    return render_template('static/pics.html')

@app.route('/profile1')
def profile1():
    return render_template('static/profile1.html')

@app.route('/schedule')
def schedule():
    return render_template('static/schedule.html')

@app.route('/secrets')
def secrets():
    return render_template('static/secrets.html')

if __name__ == '__main__':
    app.run(debug=True)
