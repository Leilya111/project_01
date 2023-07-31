# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться. 

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
#print(my_favorite_songs)

#Вариант 1

print(my_favorite_songs[0:14])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[51:-15])

#Вариант 2

i = my_favorite_songs.find(', ')

first_track = my_favorite_songs[: i]
print(first_track)

j = my_favorite_songs.rfind(', ')

last_track = my_favorite_songs [j+2 :]
print(last_track)

my_favorite_songs_copy = my_favorite_songs[i+2 : j]
i = my_favorite_songs_copy.find(', ')

first_track = my_favorite_songs_copy[: i]
print(first_track)

j = my_favorite_songs_copy.rfind(', ')

last_track = my_favorite_songs_copy [j+2 :]
print(last_track)