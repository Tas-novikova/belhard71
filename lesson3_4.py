# TODO Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных


num1 = float(input())
num2 = float(input())
num3 = float(input())
check_num1 = num1 > 0
check_num2 = num2 > 0
check_num3 = num3 > 0
sum_positive_numbers = check_num1 + check_num2 + check_num3  # использовать сам класс bool() - плохая практика
sum_negative_numbers = 3 - sum_positive_numbers
print('Положительных чисел -', sum_positive_numbers, ', отрицательных чисел -', sum_negative_numbers)
