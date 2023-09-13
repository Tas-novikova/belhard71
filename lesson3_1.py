# TODO: пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = input()
split_text = text.split(' ')
print(f"{'-'.join(split_text)}")
print(text.replace(' ', '-'))
