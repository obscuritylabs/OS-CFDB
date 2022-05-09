import config
import psutil
import pymongo
from flask import Flask, abort, jsonify, make_response, request, url_for
from flask_apscheduler import APScheduler
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

__API_VERSION = "api/v1"

# init flask app
app = Flask(__name__)
# setup all config vars
app.config.from_object("config")
# init rates
limiter = Limiter(app, key_func=get_remote_address, default_limits=["60 per minute"])
# setup pymongo backend
client = pymongo.MongoClient(app.config["MONGODB_URL"])
db = client.api
# TODO: setup redis cron
#  scheduler = APScheduler()
#  scheduler.init_app(app)
#  scheduler.start()
# setup API view cache
cache = Cache(app)


def make_cache_key(*args, **kwargs):
    return request.url


# custom rate limit response


@app.errorhandler(429)
def ratelimit_handler(e):
    """Overide the default http 429 code error.

    Decorators:
        app.errorhandler

    Arguments:
        e {string} -- error of 429.

    Returns:
        json -- ratelimit exceeded
    """
    return make_response(jsonify(error="ratelimit exceeded %s" % e.description), 429)


@app.errorhandler(404)
def ratelimit_handler(e):
    """Overide the default http 404 code error.

    [description]

    Decorators:
        app.errorhandler

    Arguments:
        e {string} -- error of 404.

    Returns:
        json -- url_unkown
    """
    return make_response(
        jsonify(
            {
                "error": {
                    "id": "url_unkown",
                    "code": 404,
                    "details": e.description,
                }
            }
        ),
        404,
    )


@app.errorhandler(500)
def crit_error_handler(e):
    """Overide the default http 500 code error.

    Decorators:
        app.errorhandler

    Arguments:
        e {string} -- error of 500.

    Returns:
        json -- server_error
    """
    return make_response(
        jsonify(
            {
                "error": {
                    "id": "server_error",
                    "code": 500,
                    "details": e.description,
                }
            }
        ),
        500,
    )


@app.route("/%s/status/" % (__API_VERSION), methods=["GET"])
@cache.cached(timeout=5)
@limiter.limit("30/minute")
def get_status():
    """Check to make sure all services are running.

    Uses multiple resources to check the full stack.

    Decorators:
        app.route -- Flask route
        cache.cached -- Redis view cache
        limiter.limit --limt route per IP to 120 a min.

    Returns:
        json -- Status of server.
    """
    try:
        return make_response(jsonify({"status": "ok"}), 200)
    except:
        abort(500)


@app.route("/%s/load/" % (__API_VERSION), methods=["GET"])
@cache.cached(timeout=5)
@limiter.limit("60/minute")
def get_load():
    """Server CPU precent load.

    Uses psutil to check load of server, useful for front end
    user debugging.
        > curl 'http://127.0.0.1:8080/api/v1/load'

    Decorators:
        app.route -- Flask route
        cache.cached -- Redis view cache
        limiter.limit --limt route per IP to 120 a min.

    Returns:
        json --  CPU percent load.
    """
    try:
        return make_response(jsonify({"load": psutil.cpu_percent()}), 200)
    except:
        abort(500)


@app.route("/%s/retrive/finding/id/search" % (__API_VERSION), methods=["GET"])
@cache.cached(timeout=60, key_prefix=make_cache_key)
@limiter.limit("120/minute")
def search_finding_id():
    """Search regex of OS-CFDB ID's.

    Uses pymongo regex on Finding Matrix.ID for front-end
    type ahead within VUE.
    Example as follows:
        > curl 'http://127.0.0.1:8080/api/v1/retrive/finding/id/search?id=OS-CFDB'

    Decorators:
        app.route -- Flask route
        cache.cached -- Redis view cache
        limiter.limit --limt route per IP to 120 a min.

    Returns:
        json -- list of finding data.
    """
    try:
        temp = []
        f_id = "^" + str(request.args.get("id"))
        cursor = db.findings.find(
            {"finding.findingDetails.findingMatrix.id": {"$regex": f_id}},
            {"_id": True, "finding.findingDetails.findingMatrix": True},
        ).limit(10)
        for x in cursor:
            temp.append({"id": str(x["_id"]), "data": x["finding"]})
        return make_response(jsonify(temp), 200)
    except:
        abort(500)


@app.route("/%s/retrive/finding/title/search" % (__API_VERSION), methods=["GET"])
@cache.cached(timeout=60, key_prefix=make_cache_key)
@limiter.limit("120/minute")
def search_finding_title():
    """Search regex of finding title.

    Uses pymongo regex on Finding Matrix.ID for front-end
    type ahead within VUE.
    Example as follows:
        > curl 'http://127.0.0.1:8080/api/v1/retrive/finding/title/search?title=Insecure'

    Decorators:
        app.route -- Flask route
        cache.cached -- Redis view cache
        limiter.limit --limt route per IP to 120 a min.

    Returns:
        json -- list of finding data.
    """
    try:
        temp = []
        f_title = "^" + str(request.args.get("title"))
        cursor = db.findings.find(
            {"finding.findingDetails.findingMatrix.title": {"$regex": f_title}},
            {"_id": True, "finding.findingDetails.findingMatrix": True},
        ).limit(10)
        for x in cursor:
            temp.append({"id": str(x["_id"]), "data": x["finding"]})
        return make_response(jsonify(temp), 200)
    except:
        abort(500)


@app.route("/%s/retrive/finding/id" % (__API_VERSION), methods=["GET"])
@cache.cached(timeout=60, key_prefix=make_cache_key)
@limiter.limit("60/minute")
def get_finding():
    """Retrive findings by ID.

    Uses pymonogo to retrive by finding ID.
    Used for front end finding retreval.
        > curl 'http://127.0.0.1:8080/api/v1/retrive/finding/id/OS-CFDB-1000'


    Decorators:
        app.route -- Flask route
        cache.cached -- Redis view cache
        limiter.limit --limt route per IP to 60 a min.

    Arguments:
        f_id {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    try:
        f_id = str(request.args.get("id"))
        document = db.findings.find_one({"finding.findingDetails.findingMatrix.id": f_id}, {"_id": False})
        if not document:
            return make_response(jsonify({"data": {}}), 200)
        return make_response(jsonify({"data": document}), 200)
    except:
        abort(500)


if __name__ == "__main__":
    # DEBUG: builds
    app.run(host="127.0.0.1", port=8080)
