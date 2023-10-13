'''
    mutable - list, dict, set
    immutable - str, int, float, None, tuple, bool
'''

# example 1
# mutable objects in functions


def summary(n):
    n += [4]


a = [1, 2, 3]
summary(a)

print(a)

# example 2
# how to avoid changing mutable objects in functions


def summary(n):
    # n = []
    # n.append(4)
    n = n[:]
    n += [4]


a = [1, 2, 3]
summary(a)

print(a)

# example 3
# immutable objects in functions


def summary(n):
    n += 1


a = 5
summary(a)

print(a)
