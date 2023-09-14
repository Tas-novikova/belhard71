# TODO: Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных


num1 = input()
num2 = input()
num3 = input()
sum_positive_numbers = bool(num1.isdigit()) + bool(num2.isdigit()) + bool(num3.isdigit())
sum_negative_numbers = 3 - sum_positive_numbers
print('Положительных чисел -', sum_positive_numbers, ', отрицательных чисел -', sum_negative_numbers)
