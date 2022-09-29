# a - дописать данные в файл
# r - чтение
# w - запись

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # Разделителя не будет: redgreenblue
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# При таком подходе вызывать close() не надо
with open(path, 'w'):
    data = open('file.txt', 'a')
    data.writelines(colors)
