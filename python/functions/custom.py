def calc(x: int | float, y: int | float) -> int | float:
    return x + y


def prize(years: int, c: float = 1.5) -> float:
    return years * c


# Все неименованные аругемны собираются в кортеж *args
# Все именованные аругемны собираются в словарь *kwargs
def summary(*args, **kwargs) -> int | float:
    print(type(args))
    print(args)
    print(kwargs)
    return sum(args)


if __name__ == '__main__':
    print(calc(10, 20))
    print(calc(x=10, y=20))
    print(summary(30, 40, a=10, b=20))
