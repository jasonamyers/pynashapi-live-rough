import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Config:
    SECRET_KEY = 'cookies'

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ENVIRONMENT = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'data-dev.sqlite')

    def init_app(cls, app):
        app = Config.init_app(app)


config = {'development': DevelopmentConfig, 'default': DevelopmentConfig}
