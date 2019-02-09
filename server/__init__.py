import os
from flask import Flask
app = Flask(__name__, template_folder=os.path.join(os.pardir, 'client/templates'))