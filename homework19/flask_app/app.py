from flask import Flask
from app.views import app1


def application_creation():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(app1)
    return app


if __name__ == '__main__':
    application_creation().run()