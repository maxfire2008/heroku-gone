import flask
import urllib
import os

app = flask.Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path="/"):
    netloc = urllib.parse.urlparse(flask.request.url).netloc
    if netloc in ("redirect.maxstuff.net", "localhost:5000"):
        return flask.render_template('index.html')
    if netloc+".html" in os.listdir(app.template_folder):
        return flask.render_template(netloc+".html", path=flask.request.url, netloc=netloc), 410
    return flask.render_template('wb_machine.html', path=flask.request.url, netloc=netloc), 410

if __name__ == "__main__":
    app.run(debug=True)
