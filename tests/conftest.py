import os

import pytest

from fapp import app

os.environ['APP_CONF'] = 'testing'


@pytest.fixture(scope='session')
def fapp():
    """Creating app and context"""
    # for APP to start in testing mode please set APP_CONFIG=testing environment variable
    with app.app_context():
        yield app
