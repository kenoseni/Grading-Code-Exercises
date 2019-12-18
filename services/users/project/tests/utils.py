from project.api.models import User


def add_user(username, email, password):
    """Add user function"""

    user = User(
        username=username,
        email=email,
        password=password
    ).save()
    return user
