#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

time_halo = 0
time_enjoy = 0
time_clean = 0

for song in violator_songs_list:
    if song[0] == 'Halo':
        time_halo = song[1]
    elif song[0] == 'Enjoy the Silence':
        time_enjoy = song[1]
    elif song[0] == 'Clean':
        time_clean = song[1]

total_time_1 = time_halo + time_enjoy + time_clean
total_time_1_rounded = round(total_time_1, 2)

print('Три песни звучат', total_time_1_rounded, 'минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

time_sweetest = violator_songs_dict['Sweetest Perfection']
time_policy = violator_songs_dict['Policy of Truth']
time_blue = violator_songs_dict['Blue Dress']

total_time_2 = time_sweetest + time_policy + time_blue
total_time_2_rounded = round(total_time_2, 2)

print('А другие три песни звучат', total_time_2_rounded, 'минут')
