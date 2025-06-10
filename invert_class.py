"""convert class to INT, FLOAT, COMPLEX and BOOl"""
from functools import total_ordering


class Sample:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value != 0 #True if self.value != 0 else False

    """ Если в классе нет методов bool и len все экземпляры будут ИСТИННЫМИ ! !  ! ! ! ! !"""


    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __complex__(self):
        return complex(self.value)

    """Если методы __int__(), __float__() и __complex__() не определены, соответствующие функции будут обращаться к методу __index__(), 
    который указывает на то, что объект имеет целочисленный тип. 
    Этот метод должен возвращать целое число, которое и будет передаваться в эти функции. 
    Наличие этого метода у класса так же позволяет применять к экземпляру этого класса функции преобразования в 
    другую систему счисления, такие как bin(), oct() и hex()."""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def module_vector(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __int__(self):
        return int(self.module_vector())

    def __float__(self):
        return float(self.module_vector())

    def __complex__(self):
        return complex(real=self.x, imag=self.y)


class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls((5 / 9) * (temperature - 32))

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

@total_ordering
class RomanNumeral:
    def __init__(self, number: str):
        self.number = number
        self.arab_number = self.romanToInt(number)

    def __str__(self):
        return f'{self.number}'

    def arab_to_rom(self):
        pass

    @staticmethod
    def romanToInt(numeral):
        rlist = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                             (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        index = 0
        intResult = 0
        for integer, romanNumeral in rlist:
            while numeral[index: index + len(romanNumeral)] == romanNumeral:
                intResult += integer
                index += len(romanNumeral)

        return intResult

    @staticmethod
    def intToRoman(integer):
        rlist = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                             (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        romanResult = ""
        for wholeNumber in rlist:
            while integer >= wholeNumber[0]:
                integer -= wholeNumber[0]
                romanResult += wholeNumber[1]
        return romanResult

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.romanToInt(self.number) == self.romanToInt(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.romanToInt(self.number) < self.romanToInt(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.number = self.intToRoman(self.romanToInt(self.number) + self.romanToInt(other.number))
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            self.number = self.intToRoman(self.romanToInt(self.number) - self.romanToInt(other.number))
            return self
        return NotImplemented

    def __int__(self):
        return self.romanToInt(self.number)

