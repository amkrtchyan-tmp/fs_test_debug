from flask import render_template
from flask_security import auth_required

from . import auth
from .models import User


@auth.route('/users')
@auth_required()
def users():
    users_list = User.query.all()
    print(users_list)
    return render_template('users.html', users_list=users_list)


@auth.route('/user_profile/<token>')
@auth_required()
def user_profile(token: str):
    user = User.get_by_token(token)
    return user.email
