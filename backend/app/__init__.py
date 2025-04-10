from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Add this import
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Add this line to enable CORS for all routes
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
