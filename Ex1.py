'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток,  которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.
'''
from random import randint
n = int(input('Count: '))
count_max = 0
count_min = 1
temp = 0

for i in range(n):
    temp = randint (0,1)
    print(temp, end = ' ')
    if temp == 0: count_min += 1
    elif temp == 1: count_max += 1
    i+=1

if count_max < count_min:
    print(f'\n{count_max}')
else: print (f'\n{count_min}')