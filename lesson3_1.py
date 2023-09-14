# TODO: пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

#  text = 'Nice to meet you'
text = input()
split_text = text.split(' ')
join_text = '-'.join(split_text)
print(text.replace(' ', '-'))
print(f"{join_text}")
