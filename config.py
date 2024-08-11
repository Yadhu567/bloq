import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("mongodb://localhost:27017")
    JWT_SECRET_KEY = os.getenv("b5c1e0ffb2934f64917b4c78956f2e223b96f9b042d1939e73f8315e3b15d32e")
