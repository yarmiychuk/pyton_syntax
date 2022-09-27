from os import remove


print('Hello, world')

a = 648
b = 1.23
value = None
# Одинарные и двойные кавычки можно комбинировать,
# они равноценны для замены друг друга
value2 = 'Операция "Ы" и другие приключения Шурика'

print(a)
print(type(a))

print(b)
print(type(b)) # Комментарий

value = 'Дима'
print(value)
print(type(value))

print(a, b, value)
print(a, '-', b, '-', value)

# В этом примере в круглых скобках можно также указать
# порядковый индекс выводимой переменной
print('{} - {} - {}'.format(a, b, value))

# Лично мне нравится вот это
print(f'{a} - {b} - {value}')

bbb = True
ccc = False

# Списки (массивы)
list = []
list2 = [1, 2, 3]
list3 = ['1', '2', '3']
print(list2)
print[list3]
# В списках можно миксовать типы (но не нужно))))
list4 = ['text', 1, 1.55, False]
# Работа со списками 
list3.append(4) # = [1, 2, 3, 4]
list3.remove(3) # = [1, 2, 4]
del list3[1] # = [1, 4]


# Получение данных от пользователя
in1 = input() # Строка
in2 = int(input()) # Число
# ИТД

# Арифметика
# + - * / % // **
# // - целый результат без дробной части
# ** - возведение в степень
# Длина чисел НЕ ограничена - 36278628632963213621832635207632071863218036

a = 12
b = 5
print(a // b) # = 2

a1 = 1.3
b1 = 3
print(a1 / b1) # = 3.900000000004
print(round(a1 / b1)) # = 4
print(round(a1 / b1, 5)) # = 3.9

a2 = 3
a2 = a + 5 # = 8
a2 += 5 # 13

# Логические
# > >= < <= == !=
# not and or (догадайся сам что это)
# is, is not, in, not in 

aaa = [1, 2, 3, 4, 5]
print(2 in aaa) # True

# if else while for
if a2 > 3:
    print('zzzz')
elif a2 < 3:
    print('xxxx')
else:
    print('фигня какая-то')

# "В случае"
peremennaya = 7
match peremennaya:
    case 1:
        print("Один")
    case _:
        print("Во всех остальных случаях")
# break; ставить не надо

i = 0
while i < 10:
    i += 1
    print(i) 
else:
    print('Конец цикла')

for i in 1, 2, 3, 4, 5:
    print(i)
    
for i in range(10):
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(3, 6):
    print(i) # 3, 4, 5

for i in range(1, 9, 2):
    print(i) # 1, 3, 5, 7

# Строки
text = 'Съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
# text.isdigit()
# text.islower()
# text.replace('ещё', 'ЕЩЁ')

# text как массив символов, поэтому все операции возможны
# обращаться к части строки можно через text[:] == substring в Java
# text[5:-12] - отрицательное число == символ с конца (len - 12)

# Функции
# Можно возвращать любые типы и значения, или ничего (void)
def f(x):
    if x == 1:
        return 'int'
    elif x == 2.3:
        return 23 
    else:
        return # NonуType - без типа, или ничего
