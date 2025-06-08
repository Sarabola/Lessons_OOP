from functools import singledispatchmethod
from datetime import date
from functools import total_ordering

class Processor:
    @singledispatchmethod
    @staticmethod
    def process(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    @staticmethod
    def int_float_process(data: int | float):
        return data * 2

    @process.register(str)
    @staticmethod
    def str_process(arg):
        return arg.upper()

    @process.register(list)
    @staticmethod
    def list_process(arg):
        return sorted(arg)

    @process.register(tuple)
    @staticmethod
    def tuple_process(arg):
        return tuple(sorted(arg))

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register
    @staticmethod
    def _int_float_neg(arg: bool | int | float):
        return -1 * arg

    @neg.register(bool)
    @staticmethod
    def _int_float_neg(arg):
        return not arg

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def _int_float_format(arg: int | float):
        if isinstance(arg, int):
            print( f'Целое число: {arg}')
        else:
            print( f'Вещественное число: {arg}')

    @format.register
    @staticmethod
    def _list_tuple_format(arg: list | tuple):
        if isinstance(arg, list):
            print( f"Элементы списка: ", *arg)
        else:
            print( f"Элементы кортежа: ", *arg)

    @format.register(dict)
    @staticmethod
    def _dict_format(arg):
        print('Пары словаря: ', end='')
        print(*arg.items(), sep=', ')

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _date_init(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _iso_init(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register
    def _list_tuple_init(self, birth_date: list | tuple):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        return current_age(self.birth_date, date.today())

class Config:
    """Реализация SingleTone pattern"""
    _init = None

    def __new__(cls, *args, **kwargs):
        if cls._init is None:
            cls._init = super().__new__(cls)
            cls._init.program_name = 'GenerationPy'
            cls._init.environment = 'release'
            cls._init.loglevel = 'verbose'
            cls._init.version = '1.0.0'
            return cls._init
        return cls._init

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'{self.__class__.__name__}({self.word})'

    def __str__(self):
        return self.word.title()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        else:
            return NotImplemented

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f'{self.__class__.__name__}{self.year, self.month}'

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple | list):
            return (self.year, self.month) == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            if self.year == other.year:
                return self.month < other.month
            else:
                return self.year < other.year
        elif isinstance(other, tuple | list):
            return (self.year, self.month) < tuple(other) if len(other) == 2 else NotImplemented
        else:
            return NotImplemented

@total_ordering
class Version:
    def __init__(self, version):
        self.version = version

    def __repr__(self):
        return f'{self.__class__.__name__}({self.version!r})'

    def __str__(self):
        return f'{self.version}'

    def ver_to_list(self):
        res = [i for i in map(int, self.version.split('.'))]
        while len(res) < 3:
            res.append(0)
        return res


    def __eq__(self, other):
        if isinstance(other, Version):
            return self.ver_to_list() == other.ver_to_list()
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.ver_to_list() < other.ver_to_list()
        else:
            return NotImplemented

