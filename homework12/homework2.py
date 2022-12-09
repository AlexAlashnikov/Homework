import string

class InvalidPassword(Exception):
    pass

class InvalidLogin(Exception):
    pass

class InvalidEmail(Exception):
    pass

class ValidationError(Exception):
    pass


class Validator:

    @staticmethod
    def validate(user_data: tuple) -> bool:
        try:
            Validator.validate_login(user_data[0])
            Validator.validate_password(user_data[1])
            Validator.validate_email(user_data[2])
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError
        else:
            return True

    @staticmethod
    def validate_login(login: str) -> bool:
        if len(login) >= 6:
            return True
        else:
            raise InvalidLogin

    @staticmethod
    def validate_email(email: str) -> bool:
        if '@' in email and email[-3] == '.' and email[-2:] == 'by':
            return True
        else:
            raise InvalidEmail

    @staticmethod
    def validate_password(password: str) -> bool:
        if (len(password) >= 8 and 
            len([i for i in password if i in string.ascii_lowercase]) > 0 and
            len([i for i in password if i in string.ascii_uppercase]) > 0 and
            len([i for i in password if i in string.punctuation]) > 0):
            return True
        else:
            raise InvalidPassword


user_data = ("user_login", "Some!Password", "user@email.by")
v = Validator()
v.validate(user_data)
v.validate_login("user_login")
v.validate_password("Some!Password")
v.validate_email("user@email.by")