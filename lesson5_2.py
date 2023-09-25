# TODO Сделать калькулятор: у пользователя спрашивается число, потом действие
#  и второе число

num1 = float(input())
act = input()
num2 = float(input())

if act == '+':
        result = num1 + num2
        print(result)
elif act == '-':
        result = num1 - num2
        print(result)
elif act == '*':
        result = num1 * num2
        print(result)
elif act == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("На ноль делить нельзя!")
