class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return super().__getattribute__('price') * super().__getattribute__('quantity')
        elif name == 'name':
            return super().__getattribute__(name).title()
        else:
            return super().__getattribute__(name)

class Logger:
    def __setattr__(self, attr, value):
        print(f'Изменение значения атрибута {attr} на {value}')
        self.__dict__[attr] = value

    def __delattr__(self, item):
        print(f"Удаление атрибута {item}")
        #del self.__dict__[item]
        object.__delattr__(self, item)


class Ord:
    def __getattr__(self, item):
        return ord(item)


class DefaultObject:
    # def __init__(self, default=None, **kwargs):
    #     self.default = default
    #     for kwarg in kwargs.items():
    #         self.__setattr__(*kwarg)
    #
    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value
    #
    # def __getattr__(self, item):
    #     return super().__getattribute__('default')

    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return self.default


class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        if isinstance(value, int | float) and value < 0:
            value = -value
        self.__dict__[key] = value


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def attrs_num(self):
        return len(self.__dict__) + 1


class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        self.__dict__[key] = value

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')


class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    def __getattribute__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return super().__getattribute__(item)
    
    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        super().__setattr__(self, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        super().__delattr__(item)

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)