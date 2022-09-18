# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

import os
os.system('cls||clear')
print('Определение простых множителей числа')
num = int(input("Введите число: "))
i = 2
lst = []
user_num = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {user_num} приведены в списке: {lst}")