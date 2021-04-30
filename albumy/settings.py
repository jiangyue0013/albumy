import os
import sys


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"


class BaseConfig:
    ALBUMY_ADMIN_EMAIL = os.getenv("ALBUMY_ADMIN", "admin@albumy.com")
    ALBUMY_PHOTO_PER_PAGE = 12
    ALBUMY_COMMENT_PER_PAGE = 15
    ALBUMY_NOTIFICATION_PER_PAGE = 20
    ALBUMY_USER_PER_PAGE = 20
    ALBUMY_MANAGE_PHOTO_PER_PAGE = 20
    ALBUMY_MANAGE_USER_PER_PAGE = 30
    ALBUMY_MANAGE_TAG_PER_PAGE = 50
    ALBUMY_MANAGE_COMMENT_PER_PAGE = 30
    ALBUMY_SEARCH_RESULT_PER_PAGE = 20
    ALBUMY_MAIL_SUBJECT_PREFIX = "[Albumy]"
    ALBUMY_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    ALBUMY_PHOTO_SIZE = {'small': 400,
                         'medium': 800}
    ALBUMY_PHOTO_SUFFIX = {
        ALBUMY_PHOTO_SIZE['small']: '_s',  # thumbnail
        ALBUMY_PHOTO_SIZE['medium']: '_m',  # display
    }

    SECRET_KEY = os.getenv("SECRET_KEY", "a secret string")
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024

    # bootstrap 资源设置
    BOOTSTRAP_SERVE_LOCAL = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("Albumy Admin", MAIL_USERNAME)

    # dropzone 相关设置
    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    DROPZONE_ENABLE_CSRF = True

    # flask-avatars 相关设置
    AVATARS_SAVE_PATH = os.path.join(ALBUMY_UPLOAD_PATH, "avatars")
    AVATARS_SIZE_TUPLE = (30, 100, 200)

    # flask-whooshee 设置
    WHOOSHEE_MIN_STRING_LEN = 1


class DevelopmentConfig(BaseConfig):
    DEV_MYSQL_USERNAME = os.getenv("DEV_MYSQL_USERNAME")
    DEV_MYSQL_PASSWORD = os.getenv("DEV_MYSQL_PASSWORD")
    DEV_MYSQL_DATABASE = os.getenv("DEV_MYSQL_DATABASE")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@localhost:3306/%s" \
        % (DEV_MYSQL_USERNAME, DEV_MYSQL_PASSWORD, DEV_MYSQL_DATABASE)


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = prefix + ":memory"


class ProductionConfig(BaseConfig):
    PRO_MYSQL_USERNAME = os.getenv("PRO_MYSQL_USERNAME")
    PRO_MYSQL_PASSWORD = os.getenv("PRO_MYSQL_PASSWORD")
    PRO_MYSQL_DATABASE = os.getenv("_MYSQL_DATABASE")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@localhost:3306/%s" \
        % (PRO_MYSQL_USERNAME, PRO_MYSQL_PASSWORD, PRO_MYSQL_DATABASE)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}


class Operations:
    CONFIRM = "confirm"
    RESET_PASSWORD = "rest-password"
    CHANGE_EMAIL = "change-email"
