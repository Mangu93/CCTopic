import redis
from flask import Flask
app = Flask(__name__)
import os
default = os.environ.get('name')
redis_host = "localhost"
redis_ip = 6379
redis_password = ""
try:
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
except:
    print("No Redis db found")
    r = None

@app.route('/')
def hello_world():
    if r is None:
        return "Hello {}".format(default)
    else:
        times = r.get("times")
        r.set("times", times+1)
        return "Hello {0}, you have been here {1} times".format(default, times)
@app.route('/<name>')
def hello_name(name=default):
    if r is None:
        return "Hello {}".format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
