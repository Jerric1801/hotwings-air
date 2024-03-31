from flask import Flask
from backend.services.activity_log.routes import activity_blueprint

app = Flask(__name__)
app.register_blueprint(activity_blueprint)

if __name__ == '__main__':
    app.run(debug=True)