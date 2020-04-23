from flask import Flask, jsonify
from redis_ratelimit import ratelimit

app = Flask(__name__)

@app.route('/oi')
@ratelimit(rate='1/s', key='oi', redis_url='redis://192.168.56.1:6379/1')
def index_oi():
    return jsonify({'carrier': 'oi'})

@app.route('/vivo')
@ratelimit(rate='3/s', key='vivo', redis_url='redis://192.168.56.1:6379/1')
def index_vivo():
    return jsonify({'carrier': 'vivo'})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	


