# TODO Дан список чисел, необходимо его развернуть без использования метода revese и
#  функции reversed, а так же дополнительного списка и среза


def reverse_numbers(numbers: list) -> list:
    rev_numbers = [numbers[i] for i in range(len(numbers)-1, -1, -1)]
    # for i in range(len(numbers)-1, -1, -1):
    #     rev_numbers.append(numbers[i])

    return rev_numbers


print(reverse_numbers([1, 6, 4, 8, 7, 6]))
