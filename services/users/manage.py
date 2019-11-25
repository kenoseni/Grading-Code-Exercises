import unittest
from flask.cli import FlaskGroup
from project import create_app, db
from database import db

cli = FlaskGroup(create_app=create_app)

# this registers a new command to the cli so that we can run it from \
# the command line
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs the test without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()