import re

class Validator:
    """Валидация login, password, email, через регулярные выражения"""
    @staticmethod
    def validate(user_data: tuple):
        if (Validator.validate_login(user_data[0]) and
            Validator.validate_password(user_data[1]) and
            Validator.validate_email(user_data[2])):
            return True
        else:
            return False

    @staticmethod
    def validate_login(login: str):
        return re.match(r'[a-zA-Z\d]{6,10}', login)

    @staticmethod
    def validate_password(password: str):
        return re.match(r'[\w+!*-/%]{8,}', password)

    @staticmethod
    def validate_email(email: str):
        return re.match(r'[\w]+@{1,1}[a-zA-Z]+\.[by]', email)


user_data = ('2alex22','pas!s12word', 'email@gmail.by' )
val = Validator()
print(val.validate(user_data))