import os
from dotenv import load_dotenv
from pathlib import Path

# Get the root directory
ROOT_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file
load_dotenv(os.path.join(ROOT_DIR, '.env'))

class Config:
    # Project paths
    ROOT_DIR = ROOT_DIR
    BACKEND_DIR = ROOT_DIR / 'backend'
    FRONTEND_DIR = ROOT_DIR / 'frontend'
    DATABASE_DIR = ROOT_DIR / 'database'
    
    # Google API
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    GOOGLE_CUSTOM_SEARCH_ENGINE_ID = os.getenv('GOOGLE_CUSTOM_SEARCH_ENGINE_ID')
    
    # Database
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv('FLASK_DEBUG') == '1'
    
    # AI keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
    
    # Database URL
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    @classmethod
    def get_path(cls, *paths):
        """Helper method to get paths relative to root directory"""
        return os.path.join(cls.ROOT_DIR, *paths) 