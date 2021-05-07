import random
import string

import pytest

from application import db, app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["ENCRYPTION_KEY"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    app.config["ENCRYPTION_IV"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    with app.app_context():
        db.create_all()
    return app.test_client()