from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello Shreya!!')


@app.route('/index.html')
def index():
    return render_template('/index.html')



