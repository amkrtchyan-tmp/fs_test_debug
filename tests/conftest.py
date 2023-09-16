import pytest

from fapp import app


@pytest.fixture(scope='session')
def fapp():
    """Creating app and context"""
    with app.app_context():
        yield app
