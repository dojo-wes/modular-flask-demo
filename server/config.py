import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

TEMPLATES_DIR = os.path.join(os.pardir, 'client', 'templates')
STATIC_DIR = os.path.join(os.pardir, 'client', 'static')
MIGRATIONS_DIR = os.path.join('server', 'models', 'migrations')

# setup app
app = Flask(__name__)
app.secret_key = "asdfalkjsd;flakjsdf;alskdjfasdf"
app.template_folder = TEMPLATES_DIR
app.static_folder = STATIC_DIR
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

# setup database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATIONS_DIR)