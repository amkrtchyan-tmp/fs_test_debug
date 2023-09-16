from pathlib import Path

basedir = Path(__file__).parent.parent.absolute()


class Config:
    SECRET_KEY = 'FDOyNV0umtP0dmxe8y2sH3c8rVGfl2alPx8gDNXZ+o3xWrPgFDv/kgtXiB7/bQsV3SA9Hm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask Security and depend apps settings
    SECURITY_PASSWORD_LENGTH_MIN = 8
    SECURITY_PASSWORD_SALT = '12rhIePdXmgCPBARHd'
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True

    # Enable the TESTING flag to disable the error catching during request handling
    # so that you get better error reports when performing test requests against the application.
    TESTING = True
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

    PRESERVE_CONTEXT_ON_EXCEPTION = False

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir / "fapp_test.db"}'

    SECURITY_POST_LOGIN_VIEW = '/'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir / "fapp.db"}'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig,
}
