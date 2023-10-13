#  Итератор хранит в себе всю последовательность, а генератор возвращает значения на ходу и по одному, сохраняя
#  локальные переменные и при следующем вызове продолжает работу со значения, на котором он остановился ранее,
#  и увеличивает это значение на единицу
a = [1, 3, 5]
it = iter(a)
gen = (i for i in a)

print(next(it))
print(next(it))

print(next(gen))