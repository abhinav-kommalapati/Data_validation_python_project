from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from app.models.validation import User, db

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(username=username).first():
            return False, "Username already exists"
        if User.query.filter_by(email=email).first():
            return False, "Email already registered"
        
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return True, "User registered successfully"

    @staticmethod
    def login_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return True, user
        return False, "Invalid username or password"

    @staticmethod
    def get_user_history(user_id):
        return ValidationHistory.query.filter_by(user_id=user_id).order_by(ValidationHistory.created_at.desc()).all() 