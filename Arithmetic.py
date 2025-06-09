class Arithmetic:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num})"

    def __add__(self, other): #сумма
        if isinstance(other, int | float):
            return Arithmetic(self.num + other)
        elif isinstance(other, Arithmetic):
            return Arithmetic(self.num + other.num)
        return NotImplemented

    def __radd__(self, other): #игнорирует порядок аргументов
        return self.__add__(other)

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

