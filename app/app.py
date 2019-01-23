import redis
from flask import Flask
app = Flask(__name__)
import os
default = os.environ.get('name')
redis_port = 6379
redis_password = ""
try:
    r = redis.StrictRedis(host="redis", port=redis_port, password=redis_password, decode_responses=True)
except Exception as e:
    print("No Redis db found")
    r = None

@app.route('/')
def hello_world():
    if r is None:
        return "Hello {}".format(default)
    else:
        return get_times(default)
@app.route('/<name>')
def hello_name(name=default):
    if r is None:
        return "Hello {}".format(name)
    else:
        return get_times(name)

def get_times(default):
    try:
        times = r.get("times_{}".format(default))
        if times is None:
            times = 0
        else:
            times = int(times)
        r.set("times_{}".format(default), times+1)
        return "Hello {0}, you have been here {1} times".format(default, times)
    except:
        return "Hello {0}".format(default)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
