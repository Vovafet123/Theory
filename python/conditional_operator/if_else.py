x = 50

if x:
    print(x)

if x > 20:
    print("x > 20")
if x > 40:
    print("x > 40")
else:
    print("default")

# Срабатывает только первое условие, а дальше проверка не идет
if x > 20:
    print("x > 20")
elif x > 40:
    print("x > 40")
else:
    print("default")


if __name__ == '__main__':
    pass