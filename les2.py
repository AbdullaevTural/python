# Задача 2. При работе с документацией менеджер допустил ошибку, названия товаров перемешались с ценами. Помогите восстановить документ. 
# Порядковый номер товара совпадает с номером цены

text = open("text.txt", encoding="utf-8")
string = text.readline()
text.close()
clothes = []
prices = []
string = string.split()
print(string)
for i in string:
    if i.isdigit():
        prices.append(i)
    else:
        clothes.append(i)
for i in range(len(prices)):
    prices[i] 
    print( clothes[i] + ' '+ prices[i] )
    print(f'{clothes[i]} - {prices[i]}')




