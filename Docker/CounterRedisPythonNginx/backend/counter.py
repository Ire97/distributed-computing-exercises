from flask import Flask
import redis
from fix_nginx import ReverseProxied
import os

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

redis = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'))

@app.route("/")
def count():
    redis.incr('counter')
    return "Count is %s" % redis.get('counter').decode("utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

