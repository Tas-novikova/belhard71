#  TODO Код Морзе для представления цифр и букв использует тире и точки. Напишите
#   функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
#   (словари в помощь)


def encrypt_text_with_morse_code(text: str, morse_code: dict[str, str]) -> str:
    text = text.upper()
    result = ''
    for i in text:
        for keys, vals in morse_code.items():
            if i == ' ':
                i = '    '
                result += ''.join(i)
            elif i in keys:
                i = vals + ' '
                result += ''.join(i)
    return result


morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
                    'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
                    '9':'----.', '0':'-----'}

message = 'Nice to meet you'


print(encrypt_text_with_morse_code(message, morse_code))
