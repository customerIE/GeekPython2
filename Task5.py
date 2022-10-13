# Реализуйте алгоритм перемешивания списка.
# Вариант с shuffle
import random
n= int(input('Введите количество элементов списка: '))
print('Вариант с shuffle: ')
a = list(range(n))
print(a)
random.shuffle(a)
print(a)
#
# Вариант с циклом
print('Вариант с циклом: ')
b = list(range(n))
index1 = 0
index1 = 0
print(b)
for i in range(n):
    index1 = random.randint(0,n-1)
    index2 = random.randint(0,n-1)
    temp = b[index1]
    b[index1]=b[index2]
    b[index2]=temp
print(b)
    
    

