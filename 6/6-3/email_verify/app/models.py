from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# time import will give us time since 1/1/1970
from time import time
#  jwt is JSON WEB TOKEN, gives us an ability to have encoded links
import jwt

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # creates a token for us to send, expires after ten minutes
    def get_reset_password_token(self, expires_in=600):
        # encode with shaw 256, use decode to return back a string variable
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            algorithms=['HS256']).decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
        # trying to decode token, if successful retrieving self.id from reset_password key set above
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            # return nothing if failed attempt
            return
            # if token verified, return user from database using id
        return User.query.get(id)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
