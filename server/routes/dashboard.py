from server import app
from server.controllers import dashboard

app.add_url_rule('/', 'index', dashboard.index)
app.add_url_rule('/other', 'other', dashboard.other)