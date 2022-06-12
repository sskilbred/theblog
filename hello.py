import newrelic.agent
newrelic.agent.initialize('/Users/stigskilbred/2 Work/apps/python/flask_blog/newrelic.ini')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')