# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('datafordisplay_merge.html')

@app.route('/data/<int:a>')
def data(a):
	return str(a)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9990, debug = True)
