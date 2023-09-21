# TODO Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

#text = 'Nice to meet you'
text = input()

dict_count_symbol = {symbol: text.count(symbol) for symbol in text}
print(dict_count_symbol)
