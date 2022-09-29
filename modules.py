# Работа с модулями
import mydef

print(mydef.getThisNumber)

# Как вариант:
# import mydef as d - ALIAS
# print(d.getThisNumber)

print(mydef.newString('!', 5)) # !!!!!
print(mydef.newString("!")) # !!! 
print(mydef.newString(4)) # 12 (динамическое распознавание переменных)

print(mydef.concantenario('1', '2', '3')) # 123

# Вызов рекурсии
list = []
for e in range(1, 10):
    list.append(mydef.fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# Кортеж (неизменяемый список)
a = (3, 4, 5)
print(a) # (3, 4)
print(a[1]) # 4
for item in a:
    print(item) # 3 4 5

# Словари - неупорядоченные коллекции с доступом по ключу
# Типы ключей могут отличаться
dictionary = {}
# \ Обратный слэш - чтобы не писать в одну строку, разделять
dictionary = \
    {
        # Ключ: Значение
        'up': 'Вверх',
        'left': 'Вверх',
        'down': 'Вниз',
        'right': 'Вправо'
    }
print(dictionary) # Весь словарь
print(dictionary['left']) # Влево
for k in dictionary.keys:
    print(k) # Выведет значения всех ключей

# Множества
colors = ['red', 'green', 'blue']
# add, remove, discard(удалить без ошибки, даже если не существует), clear() очистить

# Списки
# смотри лекцию - там про разницу при list1 = list2 и list1.copy()
# list.pop() - удалить последний элемент
# list.pop(2) - удалить второй элемент
# list.insert(2, значение) - вставить элемент "Значение" в позицию 2
# list.append(значение) - добавить элемент в конец