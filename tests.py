from functions import (
    task1,
    task2,
    task3,
)


#task 1
print("\ntask 2:")

"""
1. Напишите код на python, который посчитает и выведет на экран количество единичек и их индексы в массиве:

[-1,  1, -2, -1, -2,  0,  2, -3,  2, -2,  0, -1,  1, -3,  0,  1,  2, -1, -3, -3]

"""

list = [-1,  1, -2, -1, -2,  0,  2, -3,  2, -2,  0, -1,  1, -3,  0,  1,  2, -1, -3, -3]
print(task1(list))

#task 2
print("\ntask 2:")

"""
2. Дан список (list) цен на iphone xs max 256gb у разных продавцов на hotline:  

[47.999, 42.999, 49.999, 37.245, 38.324, 37.166, 38.988, 37.720]

Средствами python, написать функцию, возвращающую tuple из min, max и mean (среднюю) и median (медианную) цену.

"""

list = [47.999, 42.999, 49.999, 37.245, 38.324, 37.166, 38.988, 37.720]
print(task2(list))

#task 3
print("\ntask 3:")

"""
3. Дан словарь продавцов и цен на iphone xs max 256gb у разных продавцов на hotline: 

{ ‘citrus’: 47.999, ‘istudio’ 42.999,
 ‘moyo’: 49.999, ‘royal-service’: 37.245,
‘buy.ua’: 38.324, ‘g-store’: 37.166, 
‘ipartner’: 38.988, ‘sota’: 37.720 }

Средствами python, написать функцию, возвращающую список имен продавцов, чьи цены попадают в диапазон (from_price, to_price). Например: 

(37.000, 38.000) -> [‘royal-service’, ‘g-store’, ‘sota’]

"""

sellers= {'citrus': 47.999,
          'istudio': 42.999,
          'moyo': 49.999,
          'royal-service': 37.245,
          'buy.ua': 38.324,
          'g-store': 37.166,
          'ipartner': 38.988,
          'sota': 37.720 }

from_price = 37.000
to_price = 38.000
print ("{} -> {}".format((from_price, to_price), task3(sellers, from_price, to_price)))

#task 4
print("\ntask 4:")
print(
"""
M =     |1, 2|      a =     |1|
        |3, 4|              |2|

S =     |1*1 + 2*2| =       |5|
        |3*1 + 4*2|         |11|
"""
)

