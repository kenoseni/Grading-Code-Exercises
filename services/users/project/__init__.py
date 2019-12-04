import os
from flask import Flask

from database import db
from project.api.users import users_blueprint


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # initialize db by binding app
    db.init_app(app)

    # register blueprints
    app.register_blueprint(users_blueprint)

    from project.api import models
    from project.api import views

    # shell context for flask cli(used to register app and db to the shell)
    # now you can work with the application context and database without having
    # to import them directly into the shell
    app.shell_context_processor({
        'app': app,
        'db': db
    })
    return app
