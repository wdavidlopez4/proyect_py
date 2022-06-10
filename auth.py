from flask_login import LoginManager
from src.BLL.entities.User import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)