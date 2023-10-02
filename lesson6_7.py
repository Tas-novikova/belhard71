# TODO Дан список чисел, необходимо для каждого элемента посчитать сумму его
#  соседей, для крайних чисел одним из соседей является число с противоположной
#  стороны списка


def sum_neighbors(numbers: list) -> list:
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i+1] + numbers[-1])
        elif i == len(numbers) - 1:
            result.append(numbers[0] + numbers[i-1])
        else:
            result.append(numbers[i-1] + numbers[i+1])
    return result


print(sum_neighbors([1, 90, 8, 25, 9]))
