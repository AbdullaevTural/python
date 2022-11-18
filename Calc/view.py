import model
def createMenu():
    print('1 - дней до нового года')
    print('введите нужный пункт меню')
    printResult()

def printResult():
    print(f'{model.newYear()} осталось дней до нового года')