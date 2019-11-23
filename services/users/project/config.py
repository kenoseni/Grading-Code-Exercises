"""Application configuration module"""
import sys
from os import getenv
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

class BaseConfig:
    """Base configuration"""
    FLASK_ENV = getenv('FLASK_ENV', 'development')
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass