# from contextlib import contextmanager
#
#
# class Resource:
#     def __init__(self):
#         self.opened = False
#
#     def open(self, *args):
#         self.opened = True
#         print(f'Open file with argument {args}')
#
#     def close(self):
#         self.opened = False
#         print('Close file')
#
#     def __del__(self):
#         if self.opened:
#             print('Open file detected')
#
#     def action(self):
#         print('Do something')
#
#
# @contextmanager
# def open_resource(*args):
#     resource = None
#     try:
#         resource = Resource()
#         resource.open(*args)
#         yield resource
#     except:
#         raise
#     finally:
#         if resource:
#             resource.close()
#
#
# class ResourceWorker:
#     def __init__(self, *args):
#         self.args = args
#         self.resource = None
#
#     def __enter__(self):
#         self.resource = Resource()
#         self.resource.open(*self.args)
#         return self.resource
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.resource:
#             self.resource.close()


class Point:
    x, y, z = 10, 20, 30

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


class A(Point):
    def __init__(self, x=None, y=None):
        self.a = 10
        super().__init__(x, y)

    def __str__(self):
        return f'{self.x, self.y, self.a}'


class B(A, Point):
    pass


numbers = list(range(1, 100))


if __name__ == '__main__':
    # _list = [n*2 for n in numbers]
    # _set = {n*2 for n in numbers}
    # _dict = {n: n*2 for n in numbers}
    # _generator = (n*2 for n in numbers)
    # print(_list)
    # print(_list)
    # print(tuple(_generator))
    # print(tuple(_generator))
    print(B.__mro__)
    # a = A(40, 20)
    # print(a.x)
    # print(A.x)
    # with ResourceWorker(1, 2, 3) as res:
    #     res.action()


