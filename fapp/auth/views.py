from flask_security import auth_required

from . import auth
from .models import User


@auth.route('/user_profile/<token>')
@auth_required()
def user_profile(token: str):
    user = User.get_by_token(token)
    return user
