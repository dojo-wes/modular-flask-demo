from server.config import app, db
from server.routes import *
from server.models import *

if __name__ == "__main__":
    app.run(debug=True)