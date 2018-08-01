from flask import Flask
from flask import url_for
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request
from flask import render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

import psutil
import pymongo

import config

# init flask app
app = Flask(__name__)
# setup all config vars
app.config.from_object('config')
# init rates
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["60 per minute"]
)
# setup pymongo backend
client = pymongo.MongoClient(app.config['MONGODB_URL'])
db = client.api
# TODO: setup redis cron
#  scheduler = APScheduler()
#  scheduler.init_app(app)
#  scheduler.start()
# setup API view cache
cache = Cache(app)


def make_cache_key(*args, **kwargs): return request.url

@app.route('/')
def index():
    return render_template('index.html', active='index')

@app.route('/search/', methods=['GET'])
def search():
    return render_template('search.html', active='search')

@app.route('/search/results', methods=['GET','POST'])
def search_console():
    q_str = '^' + request.form.get('string')
    cur = db.findings.find({"finding.findingDetails.findingMatrix.title": { "$regex": q_str, "$options" : 'i'}}, {"_id": False, "finding": True}).limit(10)
    docs = [document for document in cur]
    print(docs)
    return render_template('search_results.html', active='search', docs=docs)

@app.route('/search/query', methods=['GET'])
def search_query():
    q_str = '^' + request.args.get('string')
    cur = db.findings.find({"finding.findingDetails.findingMatrix.title": { "$regex": q_str, "$options" : 'i'}}, {"_id": False, "finding.findingDetails.findingMatrix": True}).limit(10)
    docs = [document for document in cur]
    return make_response(jsonify(docs), 200)

@app.route('/findings', methods=['GET'])
def findings():
    cur = db.findings.find({}, {"_id": False})
    docs = [document for document in cur]
    return render_template('findings.html', active='findings', docs=docs)

@app.route('/findings/<string:f_id>', methods=['GET'])
def finding_id(f_id):
    cur = db.findings.find_one({"finding.findingDetails.findingMatrix.id": f_id}, {"_id": False})
    return render_template('finding.html', active='findings', doc=cur)

@app.route('/docs', methods=['GET'])
def docs():
    return render_template('index.html', active='docs')

if __name__ == '__main__':
    # DEBUG: builds
    app.run(host="127.0.0.1", port=8081)