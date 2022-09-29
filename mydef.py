def getThisNumber():
    return 5

def newString(symbol, count = 3): # '= 3' - значение по умолчанию
    return symbol * count

def concantenario(*params): # Передача разного количества параметров
    res: str = "" # явное указание типа данных str
    for item in params:
        res += item
    return res

# Рекурсия
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Кортеж (неизменяемый список)