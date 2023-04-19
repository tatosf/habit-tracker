import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Set up database client
    mongo_uri = os.environ.get("MONGODB_URI")
    client = MongoClient(mongo_uri)
    db = client.get_default_database()

    # Register blueprints
    from routes import pages
    app.register_blueprint(pages)
    
    # Add db attribute to app object
    app.db = db

    return app