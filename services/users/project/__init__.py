import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from database import db
from project.api.users import users_blueprint
from project.api.auth.auth import auth_blueprint

# instantiate extention
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):
    
    sentry_sdk.init(
    dsn="https://e5c909cdd76348008b176ad5945be634@sentry.io/1885551",
    integrations=[FlaskIntegration()]
)

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # initialize db by binding app
    db.init_app(app)

    # set up extention
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)

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
