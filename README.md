# Отчёт

## Задание 0. Расстояния между городами

**Описание задачи**:  
Составить словарь словарей расстояний между тремя городами.

**Код**:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for city1, coord1 in sites.items():
    distances[city1] = {}
    for city2, coord2 in sites.items():
        if city1 != city2:
            x1, y1 = coord1
            x2, y2 = coord2
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = distance

print(distances)
```

**Скриншот**:  
![Задание 0 - расстояния между городами](img/00.png)

## Задание 1. Площадь круга и принадлежность точки

**Описание задачи**:  
- Вычислить площадь круга радиусом 42 с точностью до 4 знаков после запятой
- Проверить, лежат ли точки `(23, 34)` и `(30, 30)` внутри круга с центром в начале координат.

**Код**:
```python
radius = 42
pi = 3.1415926
area = pi * radius ** 2
print(round(area, 4))

point_1 = (23, 34)
print(point_1[0] ** 2 + point_1[1] ** 2 <= radius ** 2)

point_2 = (30, 30)
print(point_2[0] ** 2 + point_2[1] ** 2 <= radius ** 2)
```
**Скриншот**:  
![Задание 1 - круг и точки](img/01.png)

## Задание 2. Арифметическое выражение

**Описание задачи**:  
Расставить знаки операций (`+`, `-`, `*`) и скобки между числами `1 2 3 4 5`, чтобы получить результат **25**.

**Код**:
```python
result = 1 * (2 + 3) * 4 + 5
print(result)
```

**Скриншот**:  
![Задание 2 - выражение = 25](img/02.png)

## Задание 3. Индексация строки фильмов

**Описание задачи**:  
Из строки `'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'` вывести:
- первый фильм,
- последний,
- второй,
- второй с конца.

**Код**:
```python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

print(my_favorite_movies[0:11])
print(my_favorite_movies[44:])
print(my_favorite_movies[13:26])
print(my_favorite_movies[36:42])
```

**Скриншот**:  
![Задание 3 - фильмы через срезы](img/03.png)

## Задание 4. Семья и рост

**Описание задачи**:  
Создать список членов семьи и список их роста. Вывести:
- рост отца,
- общий рост всей семьи.

**Код**:
```python
my_family = ['Отец', 'Мать', 'Я']
my_family_height = [
    ['Отец', 180],
    ['Мать', 165],
    ['Я', 175],
]

print('Рост отца -', my_family_height[0][1], 'см')
total_height = sum(person[1] for person in my_family_height)
print('Общий рост моей семьи -', total_height, 'см')
```

**Скриншот**:  
![Задание 4 - рост семьи](img/04.png)

## Задание 5. Зоопарк

**Описание задачи**:  
Работа со списком животных:
- добавить медведя между львом и кенгуру,
- добавить птиц в конец,
- убрать слона,
- найти номера клеток льва и жаворонка.

**Код**:
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1
print('Лев сидит в', lion_index, 'клетке')
print('Жаворонок сидит в', lark_index, 'клетке')
```

**Скриншот**:  
![Задание 5 - зоопарк](img/05.png)

## Задание 6. Песни Depeche Mode

**Описание задачи**:  
- Из списка песен найти общую длительность трёх указанных композиций.
- Из словаря - суммарную длительность других трёх.

**Код**:
```python
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

time_halo = time_enjoy = time_clean = 0
for song in violator_songs_list:
    if song[0] == 'Halo':
        time_halo = song[1]
    elif song[0] == 'Enjoy the Silence':
        time_enjoy = song[1]
    elif song[0] == 'Clean':
        time_clean = song[1]

total_time_1 = round(time_halo + time_enjoy + time_clean, 2)
print('Три песни звучат', total_time_1, 'минут')

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

total_time_2 = round(
    violator_songs_dict['Sweetest Perfection'] +
    violator_songs_dict['Policy of Truth'] +
    violator_songs_dict['Blue Dress'],
    2
)
print('А другие три песни звучат', total_time_2, 'минут')
```

**Скриншот**:  
![Задание 6 - длительность песен](img/06.png)

## Задание 7. Расшифровка сообщения

**Описание задачи**:  
Расшифровать фразу из 5 строк, применяя разные правила срезов к каждой строке.

**Код**:
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

word1 = secret_message[0][3]
word2 = secret_message[1][9:13]
word3 = secret_message[2][5:15:2]
word4 = secret_message[3][12:6:-1]
word5 = secret_message[4][20:15:-1]

print(word1, word2, word3, word4, word5)
```
**Скриншот**:  
![Задание 7 - расшифровка](img/07.png)

## Задание 8. Цветы в саду и на лугу

**Описание задачи**:  
Преобразовать кортежи цветов в множества и вывести:
- все виды цветов,
- пересечение (растут и там, и там),
- разность (только в саду / только на лугу).

**Код**:
```python
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set | meadow_set)
print(garden_set & meadow_set)
print(garden_set - meadow_set)
print(meadow_set - garden_set)
```

## Задание 9. Сравнение цен в магазинах

**Описание задачи**:  
Для каждой сладости найти два магазина с минимальными ценами и оформить словарь `sweets`.

**Код**:
```python
# Данные уже заданы в условии, здесь только результат
sweets = {
    'печенье': [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
```

**Скриншот**:  
![Задание 9 - словарь sweets](img/09.png)

## Задание 10. Стоимость товаров на складе

**Описание задачи**:  
Без циклов рассчитать общее количество и стоимость каждого товара на складе.

**Код**:
```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
    '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
    '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
}

lamp_code = goods['Лампа']
lamp_qty = store[lamp_code][0]['quantity']
lamp_cost = store[lamp_code][0]['quantity'] * store[lamp_code][0]['price']
print('Лампа -', lamp_qty, 'шт, стоимость', lamp_cost, 'руб')

table_code = goods['Стол']
t1q, t1p = store[table_code][0]['quantity'], store[table_code][0]['price']
t2q, t2p = store[table_code][1]['quantity'], store[table_code][1]['price']
print('Стол -', t1q + t2q, 'шт, стоимость', t1q*t1p + t2q*t2p, 'руб')

sofa_code = goods['Диван']
s1q, s1p = store[sofa_code][0]['quantity'], store[sofa_code][0]['price']
s2q, s2p = store[sofa_code][1]['quantity'], store[sofa_code][1]['price']
print('Диван -', s1q + s2q, 'шт, стоимость', s1q*s1p + s2q*s2p, 'руб')

chair_code = goods['Стул']
c1q, c1p = store[chair_code][0]['quantity'], store[chair_code][0]['price']
c2q, c2p = store[chair_code][1]['quantity'], store[chair_code][1]['price']
c3q, c3p = store[chair_code][2]['quantity'], store[chair_code][2]['price']
total_chair_qty = c1q + c2q + c3q
total_chair_cost = c1q*c1p + c2q*c2p + c3q*c3p
print('Стул -', total_chair_qty, 'шт, стоимость', total_chair_cost, 'руб')
```

**Скриншот**:  
![Задание 10 - склад](img/10.png)


