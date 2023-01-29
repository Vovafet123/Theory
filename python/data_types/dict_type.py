dictionary = {
    1: "Hello",
    2: "my",
    3: "world",
}

# dictionary.keys() -> (1, 2, 3)
# dictionary.values() -> ("Hello", "my", "world")
# dictionary.items() -> ((1, "Hello"), (2, "my"), (3, "world"))

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(key, value)

# Добавление и изменение значений
dictionary[4] = "new"

value = dictionary[2]

# возвращает значение ключа, либо None (безопасная проверка наличия ключа в словаре)
value = dictionary.get(5)

# Удаление элемента по ключю (если такого ключа нет, то будет ошибка)
dictionary.pop(3)

dictionary1 = {10: "hi", **dictionary}


if __name__ == '__main__':
    print(dictionary1)