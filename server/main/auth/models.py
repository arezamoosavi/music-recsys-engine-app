from flask_login import UserMixin
from db import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)
    password_hash = db.Column(db.String())
    is_admin = db.Column(db.Boolean, default=False)

    tokens = db.relationship("TokenModel", lazy="dynamic")

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                                        server_onupdate=db.func.now())
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def create_admin(cls, username: str, password: str) -> "UserModel":
        u = cls(username=username, is_admin=True)
        u.set_password(password)
        u.save_to_db()
        return u

    @classmethod
    def create_user(cls, username: str, password: str) -> "UserModel":
        u = cls(username=username)
        u.set_password(password)
        u.save_to_db()
        return u
    
    @classmethod
    def get_or_create(cls, username: str, password: str) -> "UserModel":
        instance = cls.find_by_username(username=username)
        if instance:
            return instance
        else:
            instance = cls.create_user(username=username, password=password)
            return instance
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()


class TokenModel(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String())
    duration = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                                        server_onupdate=db.func.now())
    
    @classmethod
    def create_token(cls, token: str, duration: int, id: int) -> None:
        u = cls(token=token, duration=duration, user_id=id)
        u.save_to_db()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()