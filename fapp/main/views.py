from flask import url_for, redirect
from flask_security import auth_required, current_user

from fapp.main import main


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('.secured'))
    return "Index view"


@main.route('/secured')
@auth_required()
def secured():
    return "Secured page"
