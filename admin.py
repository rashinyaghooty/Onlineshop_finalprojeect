from model.entity import *


class Admin(Base):
    __tablename__ = "admin_tbl"
    __table_args__ = {"extend_existing": True}
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), unique=True, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin_id = None

    @validates('username')
    def validate_username(self, key, username):
        return Validator.username_validator(username, "Invalid Username.")

    @validates('password')
    def validate_password(self, key, password):
        return Validator.password_validator(password, "Invalid Password.")

