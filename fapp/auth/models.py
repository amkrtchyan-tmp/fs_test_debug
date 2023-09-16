from flask_security import RoleMixin, UserMixin

from fapp import db


class RolesUsers(db.Model):
    __tablename__ = 'auth_roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('auth_user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('auth_role.id'))

    def __repr__(self):
        return f'<{__class__.__name__} {self.id} {self.user_id=}, {self.role_id=}>'


class Role(db.Model, RoleMixin):
    __tablename__ = 'auth_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<{__class__.__name__} {self.id} {self.name=}>'


class User(db.Model, UserMixin):
    __tablename__ = 'auth_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='auth_roles_users', backref=db.backref('auth_user', lazy='dynamic'))

    def __repr__(self):
        return f'<{__class__.__name__} {self.id} {self.email=} {self.fs_uniquifier=}>'

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # security.datastore.add_role_to_user(self, RolesDef.USER.name)

    @property
    def token(self):
        return self.fs_uniquifier

    @staticmethod
    def get_by_token(token):
        return User.query.filter_by(fs_uniquifier=token).first_or_404()
