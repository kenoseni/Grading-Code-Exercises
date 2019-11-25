"""Database setup module"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# custom constraint naming convention
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "pk_%(table_name)s",
    "idx": "idx_%(table_name)s_%(constraint_name)s"
}

# creates a metadata using the naming convention event
metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
