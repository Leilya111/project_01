# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
#Вариант 1

random_my_favorite_songs_1 = []
random_my_favorite_songs_1.append(my_favorite_songs[2])
random_my_favorite_songs_1.append(my_favorite_songs[7])
random_my_favorite_songs_1.append(my_favorite_songs[8])

total_time_1 = 0.0

for i in random_my_favorite_songs_1:
  total_time_1 += i[1]

int_time_1 = int(total_time_1)

seconds_time_1 = total_time_1-int_time_1

if seconds_time_1 > 0.59:
  all_time_1 = int_time_1 + 1 + seconds_time_1-0.6
 
else:
  all_time_1 = total_time_1

print(f'Три песни звучат {round(all_time_1, 2)} минут')  

#Вариант 2
random_my_favorite_songs = random.choices(my_favorite_songs, k=3)

total_time = random_my_favorite_songs[0][1]+random_my_favorite_songs[1][1]+random_my_favorite_songs[2][1]

int_time = int(total_time)

seconds_time = total_time-int_time

if seconds_time > 0.59:
  all_time = int_time + 1 + seconds_time-0.6
 
else:
  all_time = total_time

print(f'Три песни звучат {round(all_time, 2)} минут')  


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_my_favorite_songs_dict = random.choices(list(my_favorite_songs_dict.values()), k=3)


songs_time = 0.0

for i in random_my_favorite_songs_dict:

    songs_time = songs_time + round (i, 2)

int_time = int(songs_time)

seconds_time = songs_time-int_time

if seconds_time > 0.59:
  
  all_time = int_time + 1 + seconds_time-0.6
 
else:
  all_time = songs_time

print(f'Три песни звучат {round(all_time, 2)} минут')  





# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 