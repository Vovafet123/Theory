def calc(x: int | float, y: int | float) -> int | float:
    return x + y


def prize(years: int, c: float = 1.5) -> float:
    return years * c


# Все неименованные аргументы собираются в кортеж *args
# Все именованные аргументы собираются в словарь *kwargs
def summary(*args, **kwargs) -> int | float:
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    return sum(args)


def summary(*args, **kwargs) -> int | float:
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    return args, kwargs


def dict_iteration(**kwargs):
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")


class Template:
    _balance = 0
    __slots__ = ()
    # Кортеж с названием свойств возможных для этого класса, + и - этого параметра
    ''' + Ограничивает возможные свойства для класса
        + Ускоряет работу программы
        + Уменьшение занимаемой памяти из-за отсутствия словаря __dict__
    '''

    # mro алгоритм поиска свойств и методов в унаследованных классах

    def __init__(self):
        pass

    def hello(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass

    #  Метод, который получает класс в качестве неявного первого аргумента, точно так же,
    #  как обычный метод экземпляра получает экземпляр.
    @classmethod
    def buy(cls):
        pass

    #  Используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван
    @staticmethod
    def sell():
        pass

    #  Обращение. property используют только для protected и private свойств
    @property
    def balance(self):
        return self._balance

    #  Изменение
    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._balance = value

    #  Удаление
    @balance.deleter
    def balance(self):
        del self._balance


if __name__ == '__main__':
    # print(calc(10, 20))
    # print(calc(x=10, y=20))
    print(summary(30, 40, a=10, b=20))
    # print(unpacking(30, 40, a=10, b=20))
    # dictionary = {"name": "John", "age": 25, "sex": "male", "name": "Egor"}
    # dict_iteration(**dictionary)  # Зачем мы пишем ** если в кварги попадает словарь. Тут запаковываем?
    # print(dictionary)
