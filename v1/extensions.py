from v1.models.database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def app_extension(app):
    bcrypt.init_app(app)
    