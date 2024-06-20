import re
from datetime import datetime, date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def date_validator(cls, date_tuple, message):
        if isinstance(date_tuple, date):
            return date_tuple
        try:
            return datetime(*date_tuple).date()
        except:
            raise ValueError(message)

    @classmethod
    def amount_validator(cls, amount, message):
        if isinstance(amount, int) and amount > 0:
            return amount
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, number, message):
        if re.match(r"^(09|\+989)\d{9}$", number):
            return number
        else:
            raise ValueError(message)

    @classmethod
    def price_validator(cls, price, message):
        if isinstance(price, int) and price > 0:
            return price
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def address_validator(cls, address, message):
        if re.match("^[a-zA-Z0-9,/s]{2,30}$", address):
            return address
        else:
            raise ValueError(message)

