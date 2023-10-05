n = int(input('Введите количество кустов черники: '))
arr = list()
for i in range(n):
    a =int(input('Введите количество ягод на кусте: '))
    arr.append(a)

arr_count = list()
for i in range(len(arr)):
       arr_count.append(arr[i-2] + arr[i-1] + arr[i])
print(f'Наибольшее количество ягод за один заход {max(arr_count)}')