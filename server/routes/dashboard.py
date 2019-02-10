from server.config import app
from server.controllers import dashboard

app.add_url_rule('/', 'dashboard:index', dashboard.index)