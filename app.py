import flask
import urllib

app = flask.Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path="/"):
    print(flask.template_folder)
    netloc = urllib.parse.urlparse(flask.request.url).netloc
    if netloc in ("redirect.maxstuff.net", "localhost:5000"):
        return flask.render_template('index.html')
    return flask.render_template('catch_all.html', path=flask.request.url, netloc=netloc), 410
