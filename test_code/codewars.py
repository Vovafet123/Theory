def find_outlier(array: list) -> int:
    if len(array) % 2 == 0 and sum(array) % 2 != 0:
        for i in array:
            if i % 2 != 0:
                return i
    else:
        return [i for i in array if i % 2 != 0]


if __name__ == '__main__':
    mass = [2, 4, 3]
    mass = [2, 4, 3, 6]

    mass = [1, 3, 2]
    mass = [1, 3, 2, 5]

    print(find_outlier(mass))
