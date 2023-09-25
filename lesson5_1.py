# TODO Вывести первые N чисел кратные M и больше K

N = int(input())
M = int(input())
K = int(input())

total = 0

while total < N:
    if K % M == 0:
        print(K)
        total += 1
    K += 1
