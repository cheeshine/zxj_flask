import os
class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{id}?api_key=11de15b832e0eba51c3619d5d805e30d'
    MOVIE_API_KEY = os.environ.get('11de15b832e0eba51c3619d5d805e30d')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # Email Configurations
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('371972484@qq.com')
    MAIL_PASSWORD = os.environ.get('niqkxwvfjtvhbjdf')
    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:class2east@localhost/watchlist'


class TestConfig(Config):
    '''
    Test  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:class2east@localhost/watchlist_test'
    

config_options = {  
    # A to help us access different configuration option classes.
    'development': DevConfig,
    'production' : ProdConfig,
    'test':TestConfig
}
