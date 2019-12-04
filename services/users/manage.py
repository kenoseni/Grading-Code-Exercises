import unittest, coverage
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

from database import db

# coverage report configuration

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py'
    ]
)
COV.start()

app = create_app()

cli = FlaskGroup(create_app=create_app)

# this registers a new command to the cli so that we can run it from \
# the command line

@cli.command()
def testcov():
    """Runs the unit tests with coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

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

@cli.command()
def seed_db():
    """Seeds the database"""
    User(username='olusola', email='olusola@gmail.com').save()
    User(username='ezekiel', email='ezekiel@gmail.com').save()


if __name__ == "__main__":
    cli()
    