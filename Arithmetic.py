class Arithmetic:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num})"

    def __add__(self, other):                       #все виды заначи операторов сложения  iadd (+=)   add (x + y)  radd (y + x)
        if isinstance(other, int | float):
            return Arithmetic(self.num + other)
        elif isinstance(other, Arithmetic):
            return Arithmetic(self.num + other.num)
        return NotImplemented

    def __radd__(self, other): #игнорирует порядок аргументов
        return self.__add__(other)

    def __iadd__(self, other):                  #создается автоматически при создании add
        self.num += other                       #но каждый раз вовращает новый объект в памяти даже если объект изменяемый класс
        return self


    def __sub__(self, other):
        if isinstance(other, int | float):
            return Arithmetic(self.num - other)
        elif isinstance(other, Arithmetic):
            return Arithmetic(self.num - other.num)
        return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __itruediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __imod__(self, other):
        pass


class FoodInfo:
    """Класс попроводящий операции над БЖУ"""
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{self.__class__.__name__}{self.proteins, self.fats, self.carbohydrates}"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return self.__class__(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.__class__(
                self.proteins * other,
                self.fats * other,
                self.carbohydrates * other
            )
        return NotImplemented

    def __rmul__(self, other):
        return self.__add__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return self.__class__(
                self.proteins / other,
                self.fats / other,
                self.carbohydrates / other
            )
        return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if isinstance(other, int | float):
            return self.__class__(
                self.proteins // other,
                self.fats // other,
                self.carbohydrates // other
            )
        return NotImplemented

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float) and other != 0:
            return self.__class__(self.x / other, self.y / other)
        return NotImplemented

    def  __rtruediv__(self, other):
        return self.__truediv__(other)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.__class__(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)


class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            m = len(self.string) // other
            return self.__class__(self.string[:m])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.__class__(self.string)
            return self.__class__(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):

            return self.__class__(self.string[other:])
        return NotImplemented


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24 + minutes // 60
        self.minutes = minutes % 60

    def __repr__(self):
        return f'{self.__class__.__name__}{self.hours, self.minutes}'

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            minutes = self.minutes + other.minutes
            hours = (self.hours + other.hours + minutes // 60) % 24
            return self.__class__(hours, minutes % 60)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.minutes += other.minutes
            self.hours = (self.hours + other.hours + self.minutes // 60) % 24
            self.minutes %= 60
            return self
        return NotImplemented


class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def add(self, *args):
        self.args.extend(list(args))

    def pop(self):
        if len(self.args) == 0:
            return None
        return self.args.pop(0)

    def __str__(self):
        result = ' -> '.join(map(str, self.args))
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.args == other.args
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            new = self.args + other.args
            return self.__class__(*new)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.args.extend(other.args)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int) and other >= 0:
            list_args = self.args[other:]
            return self.__class__(*list_args)
        return NotImplemented

