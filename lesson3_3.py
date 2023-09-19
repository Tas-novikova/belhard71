# TODO Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами


# name = 'Alex'
# age = 25
# city = 'Minsk'
name = input()
age = int(input())
city = input()
welcome_message1 = 'Hello! My name is %s, I\'m %d years old and I\'m from %s' % (name, age, city)
welcome_message2 = 'Hello! My name is {}, I\'m {} years old and I\'m from {}'.format(name, age, city)
welcome_message3 = f'Hello! My name is {name}, I\'m {age} years old and I\'m from {city}'
print(welcome_message1)
print(welcome_message2)
print(welcome_message3)
