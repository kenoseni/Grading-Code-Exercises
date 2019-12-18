from project.api.models import User


def add_user(username, email):
    """Add user function"""

    user = User(
        username='parker',
        email='parker@gmail.com'
    ).save()
    return user
