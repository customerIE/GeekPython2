# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции вводятся с клавиатуры .
import random
N= int(input('Введите число N: '))
a=[]
product = 0
for i in range(N):
    a.append(random.randint(-N, N))
print(a)
pos1=int(input(f'Введите номер первого множителя от 0 до {N-1} : '))
pos2=int(input(f'Введите номер первого множителя от 0 до {N-1} : '))
if -1<pos1<N and -1<pos2<N:
    product = a[pos1] * a[pos2]
else:
    print('Позиции множителя не существует!')
print('Произведение чисел = ', product)