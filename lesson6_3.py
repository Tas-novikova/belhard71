# TODO Дан список чисел и на вход поступает число N, необходимо сместить список на
#  указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


def change_list_index(numbers: list, n: int) -> list:
    if len(numbers) > abs(n):
        new_numbers = numbers[-n:] + numbers[:-n]
    else:
        raise ValueError("n must be less than the length of the list")
    return new_numbers


print(change_list_index([1, 2, 3, 4, 5, 6, 7], 3))
