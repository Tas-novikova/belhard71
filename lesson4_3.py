# TODO Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры

n = int(input())

new_data = {n: {'name': input('Your name'), 'email': input('Your email')} for n in range(0, n)}
print(new_data)
