# TODO пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами


# text = 'Nice to meet you'
text = input()
split_text = text.split(' ')
join_text = '-'.join(split_text)
change_text1 = text.replace(' ', '-')
change_text2 = f"{join_text}"
print(change_text1)
print(change_text2)
