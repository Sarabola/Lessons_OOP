from math import pi


class Todo:
    def __init__(self):
        self.things = []
        self.low_pr = 0
        self.max_pr = 0

    def add(self, name, pr):
        self.things.append((name, pr))
        self.low_pr = min(map(lambda x: x[1], self.things))
        self.max_pr = max(map(lambda x: x[1], self.things))

    def get_by_priority(self, n):
        return [i[0] for i in self.things if i[1] == n]

    def get_low_priority(self):
        return [i[0] for i in self.things if i[1] == self.low_pr]

    def get_high_priority(self):
        return [i[0] for i in self.things if i[1] == self.max_pr]


class Postman:

    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        pre_res = [i[1] for i in self.delivery_data if i[0] == street]
        return list({}.fromkeys(pre_res))

    def get_flats_for_house(self, street, house):
        pre_res = [i[2] for i in self.delivery_data if i[1] == house and i[0] == street]
        return list({}.fromkeys(pre_res))


class Wordplay:
    def __init__(self, words=None):
        if words == None:
            words = []
        self.words = words.copy()

    def add_word(self, w):
        if w not in self.words:
            self.words.append(w)

    def words_with_length(self, l):
        return [w for w in self.words if len(w) == l]

    def only(self, *args, **kwargs):
        return [w for w in self.words if all(map(lambda x: x in ''.join(args), w))]

    def avoid(self, *args, **kwargs):
        return [w for w in self.words if not any(map(lambda x: x in ''.join(args), w))]


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, h, v):
        x1, x2 = ord(self.horizontal) - 97, ord(h) - 97
        y1, y2 = 8 - int(self.vertical), 8 - int(v)
        difference_product = (x1 - x2) * (y1 - y2)
        return True if difference_product == 2 or difference_product == -2 else False

    def move_to(self, h, v):
        if self.can_move(h, v):
            self.horizontal = h
            self.vertical = v

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        x = ord(self.horizontal) - 97
        y = 8 - int(self.vertical)
        board[y][x] = self.get_char()

        for i in range(8):
            for j in range(8):
                if abs(y - i) * abs(x - j) == 2:
                    board[i][j] = '*'

        for row in board:
            print(*row)


class Circle:
    def __init__(self, r):
        self._radius = r
        self._diameter = r * 2
        self._area = pi * r ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        if self._balance < 0:
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account, amount):
        balance = account.get_balance()
        self.withdraw(amount)
        account.deposit(amount)


class User:

    def __init__(self, name, age):
        self._name = self.is_valid_name(name)
        self._age = self.is_valid_age(age)

    def is_valid_name(self, name):
        if isinstance(name, str) and name.isalpha():
            return name
        else:
            raise ValueError('Некорректное имя')

    def is_valid_age(self, age):
        if isinstance(age, int) and 0 <= age <= 110:
            return age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = self.is_valid_name(name)

    def set_age(self, age):
        self._age = self.is_valid_age(age)


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def set_length(self, length):
        self._length = length

    def set_width(self, width):
        self._width = width

    def get_perimeter(self):
        return self._length * 2 + self._width * 2

    def get_area(self):
        return self._width * self._length

    length = property(get_length, set_length)
    width = property(get_width, set_width)
    perimeter = property(get_perimeter)
    area = property(get_area)


class HourClock:
    def __init__(self, hours):
        if self.is_valid(hours):
            self._hours = hours

    @staticmethod
    def is_valid(h):
        if isinstance(h, int) and 0 < h < 13:
            return True
        else:
            raise ValueError('Некорректное время')

    def get_time(self):
        return self._hours

    def set_time(self, hours):
        if self.is_valid(hours):
            self._hours = hours

    hours = property(fset=set_time, fget=get_time)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self._name} {self._surname}'

    def set_fullname(self, name):
        self._name, self._surname = name.split()

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    name = property(fset=set_name, fget=get_name)
    surname = property(fset=set_surname, fget=get_surname)
    fullname = property(fget=get_fullname, fset=set_fullname, doc='Какая то документация')


class Cat2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    @name.deleter
    def del_name(self):
        del self._name


