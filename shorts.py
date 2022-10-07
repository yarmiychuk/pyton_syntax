# Lambda

# def sum(x, y):
#     return x + y
sum = lambda x, y: x + y # то же самое

def mult(x, y):
    return x * y

# В качестве аргумента мб ФУНКЦИЯ
def calc(operation, a, b):
    return(operation(a, b))

print(calc(sum, 5, 10))
print(calc(mult, 6, 2))

print(sum, 4, 5) # использование заранее использованной лямбды
print(lambda x, y: x + y, 4, 5) # лямбда создаётся на ходу


#_______________________________________________
# List Comprehension - быстрое создание списков
list = []
for i in range(1, 20):
    if (i % 2 == 0):
        list.append[i]

def f(x):
    return f**3

# [expressions for item in iterable]
list = [i for i in range(1, 21)] # [1, 2, 3, 4, ...]
# [expressions for item in iterable (if conditional)]
list = [i for i in range(1, 21) if 1 % 2 == 0] # [2, 4, 6, 8, ...]
list = [(i, i) for i in range(1, 21) if 1 % 2 == 0] # [(2, 2), (4, 4), ...]
list = [f(i) for i in range(1, 21) if 1 % 2 == 0] # [8, 64, ...]
list = [(i, f(i)) for i in range(1, 21) if 1 % 2 == 0] # [(2, 8), (4, 16), ...]
# [expressions <if conditional> for item in iterable (if conditional)]

def select(f, collection):
    return [f(x) for x in collection]

def where(f, collection):
    return [x for x in collection if f(x)]

data = '1 2 3 4 5 8 15 38'.split()
res = select(int, data)
print(res) # [1, 2, 3, 4, 5, 8, 15, 38]
# lambda:
res = where(lambda x: not x % 2, res) 
print(res) # [2, 4, 38]
res = select(lambda x: (x, x**2, res))
print(res) # [(2, 8), (4, 64), (38, 1444)]


#_______________________________________________
# MAP
li = [x for x in range(1, 21)] # список от 1 до 20
print(li)
li = list(map(lambda x: x + 10, li)) # список от 11 до 30

data = list(map(int, input().split()))
# введено с клавиатуры: 1 2 3 5 7
print(data) # [1, 2, 3, 4, 5, 7]

data = '1 2 3 4 5 8 15 38'.split()
res = list(map(int, data)) # = функции select выше
res = where(lambda x: not x % 2, res) 
res = list(map(lambda x: (x, x**2, res)))


#_______________________________________________
# FILTER
filter(f, [1, 2, 3, 4, 5]) # [2, 4]

data = [x for x in range(10)] # список от 0 до 9
res = list(map(int, data))
res = list(filter(lambda x: not x % 2, data)) # [0, 2, 4, 6, 8]
res = list(map(lambda x: (x, x**2, res)))


#_______________________________________________
# ZIP
zip([1, 2, 3], ['a', 'b', 'c'], ['а', 'б', 'в'])
# результат:
[(1, 'a', 'а'), (2, 'b', 'б'), (3, 'c', 'в')] 
# нельзя пройтись дважды
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
users = ['user1', 'user2', 'user3']
ids = [3, 5, 8]
data = list(zip(users, ids))
print(data) # [('user1', 3), ('user2', 5), ('user3', 8)]


#_______________________________________________
# ENUMERATE
enumerate(['Москва', 'Питер', 'Дно'])
# результат
[(0, 'Москва'), (1, 'Питер'), (2, 'Дно')]
# нельзя пройтись дважды

