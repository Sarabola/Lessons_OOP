class PASS:
    def hash_function(obj):
        obj = str(obj)
        temp1, temp2 = 0, 0
        for i in range(len(obj) // 2):
            temp1 += ord(obj[i]) * ord(obj[(-i) - 1])
        if len(obj) % 2:
            temp1 += ord(obj[len(obj) // 2])
        for i in range(len(obj)):
            temp2 += ((-1) ** i) * (ord(obj[i]) * (i + 1))
            # print(f'{i}: {i, -i - 1} | {(-1) ** i} {i + 1}')
        print(temp1, temp2)
        return (temp1 * temp2) % 123456791

    # print(hash_function(12345))


class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y, self.color}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color and self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            raise AttributeError('Установка нового атрибута невозможна')

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __delattr__(self, item):
        raise AttributeError("Удаление атрибута невозможно")

    def __repr__(self):
        formated_kwargs = []
        for k, v in self.__dict__.items():
            formated_kwargs.append(f'{k}={v!r}')
        return f"{self.__class__.__name__}({', '.join(formated_kwargs)})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__repr__() == other.__repr__()
        return NotImplemented

    def __hash__(self):
        return hash(self.__repr__())

