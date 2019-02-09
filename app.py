from server import app
from server.routes import dashboard

if __name__ == "__main__":
    app.run(debug=True)