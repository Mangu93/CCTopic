from flask import Flask
app = Flask(__name__)
import os
default = os.environ.get('name')


@app.route('/')
def hello_world():
    return "Hello {}".format(default)
@app.route('/<name>')
def hello_name(name=default):
    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
