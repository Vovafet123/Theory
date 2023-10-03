from time import time, sleep
from random import randint

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         return self.stack.pop()
#
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.pop()
# print(s.stack)


'''Декораторы'''


def dec_timeout(delay: int = 5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time()
            response = func(*args, **kwargs)
            end = time() - start
            if end >= delay:
                print(f'Запрос длилися {end} секунд')
        return wrapper
    return decorator


@dec_timeout(delay=7)
def request():
    sleep(randint(5, 10))


def dec_1(func):
    def wrapper(*args, **kwargs):
        print('Before')
        func(*args, **kwargs)
    return wrapper


def dec_2(func):
    def wrapper(*args, **kwargs):
        print('After')
        func(*args, **kwargs)
    return wrapper


@dec_1
@dec_2
def test_func(title, tag, lag):
     print (f'Напечатать функцию {title}, {lag}, {tag}')


# test_func('Олени', 'h1', 'test')
#
#
# dec_1(dec_2(test_func('Олени', 'h1', 'test')))


if __name__ == '__main__':
    request()