# TODO Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры

# n = 2
# name = 'Ann'
# email = 'ann@gmail.com'

# name = input('Your name')
# email = input('Your email')

n = int(input())

# data = {n: {} for n in range(0, n)}
# data_name_email = {'name': name, 'email': email}
# new_data = {n: data_name_email for n in range(0, n)}

new_data = {n: {'name': input('Your name'), 'email': input('Your email')} for n in range(0, n)}
print(new_data)
