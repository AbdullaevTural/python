# a = int(input ())
# b = int(input ())
# if a**2 == b or b**2 == a:
#     print('Yes')
# else:
#     print('No')
 


# 2 задание 
# 2. Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

number= None
count = 0
while number != 0:
    number = int (input('Введите число'))
    if number %3 == 0  and number !=0:
        count +=1
print(count)


