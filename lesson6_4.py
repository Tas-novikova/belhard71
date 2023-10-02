# TODO Дан список содержащий в себе различные типы данных, отфильтровать таким
#  образом, чтобы остались только строки, использование дополнительного списка
#  незаконно

def filter_list_to_only_str(some_list: list) -> list:
    new_list = list(filter(lambda x: isinstance(x, str), some_list))
    return new_list


print(filter_list_to_only_str([1, 5, "sdf", "sgsb", "5"]))
