'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.
'''

n = int(input('Enter number: '))
k = 0
temp = 0

for i in range (n):
    temp = 2 ** k 
    i += 1
    k += 1
    print (temp, end = ' ')