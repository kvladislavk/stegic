a = "Тут есть English text, точ.ki, запятые, двое:точие, и их strange куз;ен.А теперь Was ADDED ДаЖе ЗАГЛАВНЫЕ БУКВЫ!!! " \
    "И буква Ё вместе с Е"


# служебные функции, неважно
def remove_character(string, index):
    s = list(string)
    del s[index]
    return "".join(s)

def find_in(char, string):
    for i in range(len(string)):
        if(char == string[i]):
            return i
    return -1

def replace(string, char, int):
    string = remove_character(string, int)
    string = ''.join((string[:int], char, string[int:]))
    return string



def GetReady(string):
    leng = int(len(string))
    counter = -1
    i = 0
    # делает распределение типов текста (перед РУ-пластом ставится 2, ASCII - 1) (ЭТАП: ДО ЗАШИФРОВКИ)
    while (i < leng):
        if (ord(string[i]) >= 33 and ord(string[i]) <= 126):
            if (counter == -1):
                counter = 0
            if (counter == 0):
                leng += 1
                counter = 1
                string = ''.join((string[:i], '1', string[i:]))

        if (ord(string[i]) >= 1072 and ord(string[i]) <= 1103 or ord(string[i]) >= 1040 and ord(string[i]) <= 1070):
            if (counter == -1):
                counter = 1
            if (counter == 1):
                leng += 1
                counter = 0
                string = ''.join((string[:i], '2', string[i:]))

        i += 1

    leng = int(len(string))

    ru = "йцукеёнгшщзхъфывапролджэячсмитьбюЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    en = "qwert`yuiop[]asdfghjkl;'zxcvbnm,.QWERT~YUIOP{}ASDFGHJKL:\"ZXCVBNM<>"

    # транслитерация - ASCII не трогает, ру- заменяет, (ПОСЛЕ ЭТОГО -- Шифровать)
    for i in range(leng):
        if (string[i] == '1'):
            mode = 0

        if (string[i] == '2'):
            mode = 1

        if (mode == 0):
            continue
        elif (mode == 1):
            rus_ind = int(find_in(string[i], ru))
            if (rus_ind == -1):
                continue
            string = replace(string, en[rus_ind], i)

    return string


def Fix(string):
    ru = "йцукеёнгшщзхъфывапролджэячсмитьбюЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    en = "qwert`yuiop[]asdfghjkl;'zxcvbnm,.QWERT~YUIOP{}ASDFGHJKL:\"ZXCVBNM<>"
    # Возвращает текст к первозданному виду -- убирает служебные 1,2 (ЭТАП -- ПОсле расшифровки, перед показом)
    leng = int(len(string))
    i = 0
    while i < leng:
        if (string[i] == '1'):
            string = remove_character(string, i)
            leng -= 1
            i -= 1
            mode = 0
        if (string[i] == '2'):
            string = remove_character(string, i)
            leng -= 1
            i -= 1
            mode = 1
        if (mode == 0):
            i += 1
            if (i == leng):
                break
            continue
        elif (mode == 1):
            i += 1
            if (i == leng):
                break
            en_ind = int(find_in(string[i], en))
            if (en_ind == -1):
                continue
            string = replace(string, ru[en_ind], i)

    return string

print(a)

a = GetReady(a)

print(a)

a = Fix(a)

print(a)