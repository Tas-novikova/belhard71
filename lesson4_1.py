# TODO Заполнить список степенями числа 2 (от 2^1 до 2^n)

# n = 9
n = int(input())
two_in_n = [pow(2, n) for i in range(1, n+1)]  # or  two_in_n = [2 ** n for n in range(1, n+1)]
print(two_in_n)
