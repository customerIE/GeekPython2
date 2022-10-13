# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
N = int(input('Введите число N: '))
a=[]
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
for i in range(N):
    a.append(factorial(i+1))
print('Набор произведений чисел от 1 до N: ', a)