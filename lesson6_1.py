# TODO Написать функцию перевода десятичного числа в двоичное и обратно, без
#  использования функции int


def convert_number_bin_decimal(number: int):
    bin_number = []
    if number == 0:
        bin_number.append(number)
    else:
        while number // 2:
            bin_number.append(number % 2)
            number //= 2
        else:
            bin_number.append(1)
    bin_number.reverse()
    str_bin_number = "".join(map(str, bin_number))

    step = 0
    decimal_number = 0
    for digital in bin_number[::-1]:
        decimal_number += digital * (2 ** step)
        step += 1
    return f'Двоичное число - {str_bin_number}\nДесятичное число - {decimal_number}'


print(convert_number_bin_decimal(47))
