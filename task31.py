# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#     70=2*5*7= > [2, 5, 7]
#     140=2*2*5*7= > [2, 2, 5, 7]
#     140 | 2
#     70 | 2
#     35 | 5
#     7 | 7

num = int(input("Введите число: "))
i = 2
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")
