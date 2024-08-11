from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

jwt = JWTManager(app)
cors = CORS(app)
client = MongoClient(app.config["MONGO_URI"])
db = client.project_management

from app import routes, auth
