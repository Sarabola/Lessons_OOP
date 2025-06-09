class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    def hash_function(self, password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9
    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = self.hash_function(password)


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        return cls(*map(float, string.split()))


class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def r(self):
        return int(self._hexcode[:2], 16)

    @property
    def g(self):
        return int(self._hexcode[2:4], 16)

    @property
    def b(self):
        return int(self._hexcode[4:], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode


class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.favorite_things = []

    def about(self):
        return f'Имя: {self.name}, возраст: {self.age}'

    def loves(self, thing):
        self.favorite_things.append(thing)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)


class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.num_of_pets() > 0 else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.num_of_pets() > 0 else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


class StrExtension:

    @staticmethod
    def remove_vowels(string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
        for letter in string:
            if letter in vowels:
                string = string.replace(letter, '')
        return string

    @staticmethod
    def leave_alpha(string):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in string:
            if letter.lower() not in alphabet:
                string = string.replace(letter, '')
        return string

    @staticmethod
    def replace_all(string, chars, char):
        for letter in string:
            if letter in chars:
                string = string.replace(letter, char)
        return string


class CaseHelper:

    @staticmethod
    def is_snake(string):
        return string.islower() and ' ' not in string

    @staticmethod
    def is_upper_camel(string):
        if string[0].isupper():
            for letter in string:
                if not letter.isalpha():
                    return False
            return True
        else:
            return False

    @staticmethod
    def to_snake(camel_string):
        if CaseHelper.is_snake(camel_string):
            return camel_string
        else:
            result = ''
            for char in camel_string:
                if char.isupper():
                    result += '_' + char.lower()
                else:
                    result += char
            return result[1:]

    @staticmethod
    def to_upper_camel(snake_string):
        if CaseHelper.is_upper_camel(snake_string):
            return snake_string
        else:
            return snake_string.title() if '_' not in snake_string else ''.join(map(lambda word: word.title(), snake_string.split('_')))

