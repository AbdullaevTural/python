#Дано натуральное число N. Найдите значение выражения:N + NN + NNN. N может быть любой длины.

a = int(input("Введите целое число: "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
import random 
list = [random.randint(0,9) for i in range (15)]
print (list)
checkNumber = input("Введите число: ")

strNumber = ''
for i in list:
    strNumber = strNumber + str(i)
    
print ('Да' if strNumber.count(checkNumber)> 0 else 'нет')

#Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

i = 0
j = 0
 
for j in range(2,12):
    for i in range (1,j):
        if i % j != 0:
            print(i, '/', j)
