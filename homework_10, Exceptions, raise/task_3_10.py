"""
In this script you can see 2 classes. First class is class with exceptions to second class.
Second class check valid email.
"""

class InvalidEmail(Exception):
    def __init__(self, email, message):
        self.message = message
        self.email = email

    def __str__(self):
        return f'{self.email} is invalid: {self.message}'


class Invalid_AT(InvalidEmail):
    """This exception will calling, if email doesn't have @"""

    def __init__(self, email):
        super().__init__(email, message='Invalid email, email should have @')


class InvalidLength(InvalidEmail):
    """This exception will calling, if email too short"""

    def __init__(self, email):
        super().__init__(email, message="Your email is too short")


class InvalidSymbols(InvalidEmail):

    """This exception will calling, if email syntax not support"""
    def __init__(self, email):
        super().__init__(email, message="Your email is not support local-part syntax")


class Email:
    def __init__(self, email):
        self.email = email

    def is_valid(self):
        try:
            self.characters()
            self.check_point()
            self.length_email()
        except InvalidEmail as e:
            print(f'error: {e}')
            return False
        print("Valid email")
        return True

    def check_point(self):
        self.start_domen = self.email.index("@")
        self.domen = self.email[self.start_domen+1:]
        if self.email.index(".") == 0 or self.email.index(".") == self.start_domen - 1:
            raise InvalidSymbols(self.email)
        if self.domen[0] == "." or self.domen[-1] == ".":
            raise InvalidSymbols(self.email)

    def characters(self):
        special_characters = "#!%$‘&+*–/=?^_`{|}~"
        error_special = [i for i in self.email if i in special_characters]

        if error_special:
            raise InvalidSymbols(self.email)

        if "@" not in self.email:
            raise Invalid_AT(self.email)

    def length_email(self):
        if self.start_domen < 2:
            raise InvalidLength(self.email)
        if len(self.domen) < 2:
            raise InvalidLength(self.email)

object_1 = Email("akim5159@gmail.com")
print(object_1.is_valid())






