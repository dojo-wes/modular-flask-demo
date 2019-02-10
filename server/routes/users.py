from server.config import app
from server.controllers import users

app.add_url_rule('/users/new', 'users:new', users.new)
app.add_url_rule('/users/create', 'users:create', users.create, methods=['POST'])