n = int(input())

def get_fib(n):
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib_sum = 0
        fib_sum = fib1 + fib2
        fib1 = fib2 
        fib2 = fib_sum
        print(fib2, end=' ')
get_fib(n)  
#Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
text = open("fruits.txt", encoding="utf-8")
string = text.read()
text.close()
print("Было прочитано:")
print(string, '\n')
fruits = []
letter = input('Введите букву: ').lower()

for frut in string.split():
    if frut.lower().startswith(letter):
      if not frut[-1].isalpha():
        frut = frut[:-1]
      fruits.append(frut)
print(', '.join(fruits))


# Text = dict()


# Text['Привет'] = 'Привет'
# Text['Как тебя зовут?'] = 'Робот'
# Text['Где ты?'] = 'Я везде'



# key = input()
# if key in Text:
#     print(Text[key])
# else:
#     print('Не понял')
#     key1 = input()
#     Text[key] = key1
#     print(Text[key])