class ChangeList:
    def __init__(self, list1):
        self.__list1 = list1

    def __enter__(self):
        self.__temp = self.__list1[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__list1[:] = self.__temp

        return False


first_list_of_number = [1, 2, 3]
second_list_of_number = [1, 3, 4]

with ChangeList(first_list_of_number) as fl:
    for i, a in enumerate(fl):
        first_list_of_number[i] += second_list_of_number[i]

print(first_list_of_number)
