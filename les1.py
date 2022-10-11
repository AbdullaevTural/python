#Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# def getNumber01 ():
#     s = 0
#     while True:
#         getNumber = input('Введите целое положительное число: ')  # Ввод числа
#         if getNumber.isdigit() : 
#             s = int(getNumber)
#             return s

# def print_day(a):
#     if a in range (1,10):
#         match a:
#             case 1:
#                 print("Понедельник")
#             case 2:
#                 print("Вторник")
#             case 3:
#                 print("Среда")
#             case 4:
#                 print("Четверг")
#             case 5:
#                 print("Пятница")
#             case 6:
#                 print("Суббота")   
#             case 7:
#                 print("Воскресенье")
#     else:
#        print("Нет такого дня")
    
# print_day(getNumber01 ())

# #Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# import math

# X1 = float(input('Введите число x: '))
# Y1 = float(input('Введите число y: '))
# X2 = float(input('Введите число x1: '))
# Y2 = float(input('Введите число y1: '))


# def Method(X1, X2, Y1, Y2 ):
#   sb = math.sqrt(math.pow((X2-X1),2)+ math.pow((Y2-Y1),2))
#   return  sb
# def truncate(n, decimals=2):
#     multiplier = 10 ** decimals
#     return int(n * multiplier) / multiplier
# print(truncate(Method(X1, X2, Y1, Y2 )))

# #Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


# def getNumber01 ():
#     s = 0
#     while True:
#         getNumber = input('Введите номер четверти: ')  # Ввод числа
#         if getNumber.isdigit() : 
#             s = int(getNumber)
#             return s
# def print_day(n):
#     if n < 1 or n > 4:
#         print('Неправильный номер')
#     elif n == 1:
#         print('x > 0, y > 0')
#     elif n == 2:
#         print('x < 0, y > 0')
#     elif n == 3:
#         print('x < 0, y < 0')
#     elif n == 4:
#         print('x > 0, y < 0')
# print_day(getNumber01 ())
#Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.


# getNumber = int(input('Введите номер четверти: ') )
# for i in range(getNumber+1):
#      if (i%2 == 0 and i != 0):
#         print (i)
