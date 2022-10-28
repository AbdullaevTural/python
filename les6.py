##Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random
n = int(input())
def rand_number(n):
    numbers = []
    sred =0
    for i in range(0, n):
        numbers.append(random.randint(0, 10))
    print(numbers)
    sred = list(filter(lambda x: (x > 5),numbers))
    print(sred)
rand_number(n)

## Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.

nums = [3, 1, 2, 3, 4, 6, 1, 7]

# Первый вариант

def get_up2(nums):
    ups = []
    max = nums[0]
    mins = nums[0]
    for i in nums:
        if i < mins:
            mins = i
            ups.append(mins)
        if i > max:
            max = i
            ups.append(max)
    return ups
    
print(get_up2(nums))

# Второй вариант

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(get_up(nums))
## Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
import random
from collections import Counter
nums = [1, 4, 2, 3, 6, 7]
n = int(input())
def rand_number(n):
    numbers = []
    new_list =[]
    for i in range(0, n):
        numbers.append(random.randint(1, 10))
        numbers = list(set(numbers))
    print (numbers)
    count = len(set(nums).intersection(set(numbers)))
    print (count)
    for x in numbers:
        for y in nums:
            if x == y:
                numbers.remove(x)
    print(numbers)
rand_number(n)
