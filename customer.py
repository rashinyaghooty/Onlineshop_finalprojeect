from model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"
    __table_args__ = {"extend_existing": True}
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), unique=True, nullable=False)
    phone_number = Column(String(11), unique=True, nullable=False)
    address = Column(String(255), nullable=False)

    # relation
    order = relationship("Order", back_populates="customer")

    def to_dict(self):
        return {'customer_id': self.customer_id,
                'name': self.name,
                'last_name': self.last_name,
                'username': self.username,
                'password': self.password,
                'phone_number': self.phone_number,
                'address': self.address}

    def __init__(self, name, last_name, username, password, phone_number, address):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.customer_id = None

    @validates("name")
    def validate_name(self, key, name):
        return Validator.name_validator(name, "Invalid name.")

    @validates("last_name")
    def validate_last_name(self, key, last_name):
        return Validator.name_validator(last_name, "Invalid Password.")

    @validates('username')
    def validate_username(self, key, username):
        return Validator.username_validator(username, "Invalid Username.")

    @validates('password')
    def validate_password(self, key, password):
        return Validator.password_validator(password, "Invalid Password.")

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        return Validator.phone_number_validator(phone_number, "Invalid Phone Number.")

    @validates("address")
    def validate_address(self, key, address):
        return Validator.address_validator(address, "Invalid Address.")

