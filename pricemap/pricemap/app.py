from flask import Flask, g,render_template
import psycopg2

from pricemap.blueprints.api import api

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(api, url_prefix='/api')


@app.before_request
def before_request():
   """Before every requests, connect to database in case of any disconnection."""

   if not hasattr(app, '_request_counter'):
      app._request_counter = 0
   if not hasattr(app, 'db') or app.db.closed or app._request_counter == 10000:
      if hasattr(app, 'db'):
         app.db.close()
      app.db = psycopg2.connect(**app.config['DATABASE'])
      app._request_counter = 0
   app._request_counter += 1
   g.db = app.db


@app.route('/')
def index():
   return render_template('index.html')
