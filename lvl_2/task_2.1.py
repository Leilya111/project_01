# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    min_value = arr [0]
    for i in arr [1:]:
        if min_value >= i:
         min_value = i
    return min_value

def maximum(arr):
    max_value = arr [0]
    for i in arr [1:]:
        if max_value <= i:
         max_value = i
    return max_value

spis_1 = [4,6,2,1,9,63,-134,566]
spis_2 = [-52, 56, 30, 29, -54, 0, -110]
spis_3 = [42, 54, 65, 87, 0]
spis_4 = [5]

print(f'max =  {maximum (spis_1)} , min =  {minimum (spis_1)} ')
print(f'max =  {maximum (spis_2)} , min =  {minimum (spis_2)} ')
print(f'max =  {maximum (spis_3)} , min =  {minimum (spis_3)} ')
print(f'max =  {maximum (spis_4)} , min =  {minimum (spis_4)} ')