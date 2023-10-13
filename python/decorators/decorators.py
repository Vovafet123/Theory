def decorator_middle(func):
    def wrapper(*args, **kwargs):
        print("Начало")
        func(*args, **kwargs)
        print("Конец")
    return wrapper


def decorator_data_type(func):
    def wrapper(*args, **kwargs):
        print(type(args), type(kwargs))
        func(*args, **kwargs)
        print(type(args), type(kwargs))
    return wrapper


@decorator_middle
@decorator_data_type
def print_data(*args, **kwargs):
    print(args, kwargs)


print_data(3, "привет", data=True)


decorator_middle(decorator_data_type(print_data(3, "привет", data=True)))


def decorator_before_after(func):
    def wrapper(*args, **kwargs):
        print('до')
        result = func(*args, **kwargs)
        print('после')

        return result
    return wrapper


@decorator_before_after
@decorator_before_after
def test1():
    print('функция выполняется')


decorator_before_after(decorator_before_after(test1()))
