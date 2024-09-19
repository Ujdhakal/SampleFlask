class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'AS*CSAC*&AS(C^AS&^CA(S&^FA)(SF^)&C^AS)'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'