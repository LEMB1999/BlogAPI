from flask import Flask
from flask_mongoengine import MongoEngine
from .Controllers import Article,Auth 
from dotenv import load_dotenv
import os 

def create_app():
    app = Flask(__name__)
    load_dotenv()  

    app.config["MONGODB_SETTINGS"] = {
        "db":"blog_db",
        "host":"localhost",
        "username":os.environ.get("DB_USER"),
        "password":os.environ.get("DB_PASSWORD")
    }

    db = MongoEngine(app)
    

    @app.get("/")
    def home():
        return "Welcome to the page"

    app.register_blueprint(Auth.main,url_prefix="/auth")
    app.register_blueprint(Article.main,url_prefix="/articles")
    return app

