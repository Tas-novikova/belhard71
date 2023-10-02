# TODO Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
#  четные, потом нечётные


def sort_even_odd(numbers: list) -> list:
    # numbers.sort(key=lambda x: x % 2)
    # numbers.sort()
    new_numbers = sorted(numbers, key=lambda x: x % 2)
    return new_numbers


print(sort_even_odd([1, 6, 48, 8, 31, 7, 65]))
