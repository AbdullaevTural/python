# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
def getNumber1 ():
    N = 0
    while True:
        getNumber = input('Введите число: ')  # Ввод числа
        if getNumber.isdigit() : 
            N = int(getNumber)
            return N
def Fact(n):
    fact = 1
    facts = []
    for i in range(1, n+1):
        fact *=i
        facts.append(fact)
    return facts

print (Fact(getNumber1 ()))
# 2 вариант с подключением
from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))

#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
print('x y z f')
for x in range(2):
  for y in range(2):
    for z in range(2):
        if not(x and y) or z==1:
            f = 1
        else:
            f = 0
        print(x, y, z, f)

#Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
s1 = "one"
s2 = "onetwonine"

def get_text():
    count = {}
    for s1 in s2:
        if s1 in count:
            count[s1] += 1
        else:
            count[s1] = 1
    return count
def get_count(count):
    for key in count:
        if count[key] > 1:
            print (key, count[key])

get_count(get_text())

#Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо. 



## 1 Вариант
N = int(input('Введите число: '))
count = []
coun = []
def get_numb(n):
    for s in range(-n,n+1):
        count.append(s)
        coun.append(s)
    for s in range(-n,n+1):
        coun[s] = count[s-2]
    print('Изначальный список:', count)
    print('Измененный список на 2 позиции вправо:', coun)   
get_numb(N)

## 2 Вариант

def main():
    task = []
    number = int(input('Введите число: '))
    for s in range(-number,number+1):
        task.append(s)
    print('Изначальный список:', task)
    shift = int(input('Сдвиг: '))
    task = task[-shift:] + task[:-shift]
    print('Сдвинутый список:', task)
main()