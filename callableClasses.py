import types
from collections import defaultdict
from random import choice #for Dice
from datetime import date
class Calculator:
    def __init__(self):
        pass

    def __call__(self, a, b, operation):
        if operation in ('+','*','-','/'):
            try:
                return eval(f"{a} {operation} {b}")
            except ZeroDivisionError:
                raise ValueError('Деление на ноль невоможно')


class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.sides_items = list(range(1, sides+1))
    def __call__(self):
        return choice(self.sides_items)


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)


class Filter:
    def __init__(self, predicate=None):
        self.predicate = predicate

    def __call__(self, iterable):
        if self.predicate is None:
            return [i for i in iterable if bool(i)]
        return [i for i in iterable if self.predicate(i)]


class DateFormatter:

    def __init__(self, country_code: str):
        self.country_code = country_code
        self.coutry_formats = {
            "ru": "%d.%m.%Y",
            'us': '%m-%d-%Y',
            'ca':  '%Y-%m-%d',
            'br': '%d/%m/%Y',
            'fr': '%d.%m.%Y',
            'pt':  '%d-%m-%Y',
        }

    def __call__(self, d: date):
        return d.strftime(self.coutry_formats[self.country_code])


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (*args, *kwargs)
        result = self.cache.get(key)
        if result is None:
            self.cache[key] = self.func(*args, **kwargs)
        return self.cache[key]


class SortKey:
    def __init__(self, *args):
        self.attrs = args
    def __call__(self, obj):
        return tuple(getattr(obj, attr) for attr in self.attrs)

