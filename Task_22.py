print('Введите количество элементов первого и второго наборов, соответственно "a" и "b" через запятую')
a, b = map(int, input().split(','))
print('Введите первый массив чисел через запятую  равный "a"')
list_1 = set(map(int, input().split(',')))
print('Введите второй массив чисел через запятую  равный "b"')
list_2 = set(map(int, input().split(',')))
print("Массив совпадающих чисел")
print(sorted(list_1 & list_2))