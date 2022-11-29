from random import randint

# ## Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.


# groups = 5
# grades = [0] * groups

# for i in range (len(grades)):
#     grades[i] = list(randint(2,5) for s in range(randint(20,30)))

# print(grades)

# meen_grades = []

# for grades_in_group in grades:
#     mean = 0
#     for grade in grades_in_group:
#         mean += grade
#     meen_grades.append(round(mean/len(grades_in_group),2))

# for grades_in_group in grades:
#     print(grades_in_group)

# print(meen_grades)

# max_grade = max(meen_grades)
# number_group = meen_grades.index(max_grade)
# print(f'Наилучший средний балл {max_grade} получила группа {number_group+1}')

# ##Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
# n = int(input('Введите количество строк'))

# mas = [[randint(-10, 10) for i in range(n)] for j in range(n)]
# for i in range(n):
#     print(mas[i])

# sum_dia = 0
# for i in range(n):
#     for j in range(n):  
#         if i == j:
#             print('%4.f, ' % mas[i][j], end='')
#             sum_dia += mas[i][j]
# print(" - числа по диагонали")
# print()
# print(f'сумма диагонали  {sum_dia}')

# sum_in_rows = []
# for i in mas:
#     sum_in_rows.append(sum(i))
# print(f'суммы с строках  {sum_in_rows}')

# for i in range(len(sum_in_rows)):
#     if sum_in_rows[i] > sum_dia:
#         print(f'в строке {i+1} сумма больше,  чем сумма эл. диагонали')

size = int(input('Введите количество строк '))
period = 2
matrix = [0] * size
for i in range(size):
    matrix[i] = list(randint(-10, 10) for i in range(size))
for i in matrix:
    print(i)
    
matrix_in_row = []

for row_matrix in matrix:
    for el in row_matrix:
        matrix_in_row.append(el)
print(matrix_in_row)
    
mean_temp = []
for i in range(len(matrix_in_row) - period + 1):
    mean_temp.append(sum(matrix_in_row[i:i+period]))
print(mean_temp)

max_el = max(mean_temp)
index_max_el = mean_temp.index(max_el)

print(max_el)
print(index_max_el)

for row_matrix in matrix:
    if len(row_matrix) > index_max_el:
        print(f"максимальный элемент в строке {row_matrix} равен {row_matrix[index_max_el]}, {index_max_el}")

        break
    else:
        index_max_el -= len(row_matrix)
    