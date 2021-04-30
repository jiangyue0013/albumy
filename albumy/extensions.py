import re
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, AnonymousUserMixin
from flask_dropzone import Dropzone
from flask_wtf import CSRFProtect
from flask_avatars import Avatars
from flask_whooshee import Whooshee


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
login_manager = LoginManager()
dropzone = Dropzone()
csrf = CSRFProtect()
avatars = Avatars()
whooshee = Whooshee()


@login_manager.user_loader
def load_user(user_id):
    from albumy.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = "auth.login"
login_manager.login_message = "请先登录"
login_manager.login_message_category = "warning"

login_manager.refresh_view = "auth.re_authenticate"
# login_manager.needs_refresh_message = 'Your custom message'
login_manager.needs_refresh_message_category = "warning"



class Guest(AnonymousUserMixin):

    def can(self, permission_name):
        return False
    
    @property
    def is_admin(self):
        return False

# 设置未登录的匿名用户为 Guest 类的实例
login_manager.anonymous_user = Guest