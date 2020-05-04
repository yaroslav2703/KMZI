from datetime import datetime
import matplotlib.pyplot as plt

ALPHABET = 'абвгдеёжзійклмнопрстуўфхцчшыьэюя'


def сaesar(action, source, keyword, a):
    start_time = datetime.now()
    cipher_text = ''
    source_alphabet = ALPHABET
    source_alphabet_dict = {}
    true_keyword = ''
    for i in keyword:
        if i not in true_keyword:
            true_keyword += i
    temp = ''
    for i, v in enumerate(source_alphabet):
        if v not in true_keyword:
            temp += v
    substance_alphabet = temp[-2:] + true_keyword + temp[:(len(source_alphabet) - a - len(true_keyword))]
    substance_alphabet_dict = {}
    if action == 'encryption':
        for s in source:
            if s in ALPHABET:
                if s in source_alphabet_dict:
                    source_alphabet_dict[s] += 1
                else:
                    source_alphabet_dict[s] = 1
                for i, v in enumerate(ALPHABET):
                    if s == v:
                        cipher_text += substance_alphabet[i]

            else:
                cipher_text += s
        print('сaesar.encryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(source_alphabet_dict.keys()), source_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы исходного алфавита')
        plt.show()
        return cipher_text
    elif action == 'decryption':
        for s in source:
            if s in ALPHABET:
                if s in substance_alphabet_dict:
                    substance_alphabet_dict[s] += 1
                else:
                    substance_alphabet_dict[s] = 1
                for i, v in enumerate(substance_alphabet):
                    if s == v:
                        cipher_text += ALPHABET[i]
            else:
                cipher_text += s
        print('сaesar.decryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(substance_alphabet_dict.keys()), substance_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы зашифровонного алфавита сaesar')
        plt.show()
        return cipher_text


def trisemus_table(action, source, keyword):
    start_time = datetime.now()
    cipher_text = ''
    source_alphabet = ALPHABET
    source_alphabet_dict = {}
    true_keyword = ''
    for i in keyword:
        if i not in true_keyword:
            true_keyword += i
    temp = ''
    for i, v in enumerate(source_alphabet):
        if v not in true_keyword:
            temp += v
    substance_alphabet = true_keyword + temp
    substance_alphabet_dict = {}
    substance_alphabet = list(substance_alphabet)
    table = [[], [], [], [], [], [], [], []]
    j = 0
    k = 0
    for v in substance_alphabet:
        if k != 4:
            table[j].append(v)
            k += 1
        else:
            j += 1
            table[j].append(v)
            k = 1
    if action == 'encryption':
        line_number = 0
        element_number = 0
        for s in source:
            if s in ALPHABET:
                if s in source_alphabet_dict:
                    source_alphabet_dict[s] += 1
                else:
                    source_alphabet_dict[s] = 1
                for li, line in enumerate(table):
                    for ei, element in enumerate(line):
                        if s == element:
                            line_number = li
                            element_number = ei
                            if line_number != len(table) - 1:
                                cipher_text += table[line_number + 1][element_number]
                            else:
                                cipher_text += table[0][element_number]
            else:
                cipher_text += s
        print('trisemus_table.decryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(source_alphabet_dict.keys()), source_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы исходного алфавита')
        plt.show()
        return cipher_text
    elif action == 'decryption':
        line_number = 0
        element_number = 0
        for s in source:
            if s in ALPHABET:
                if s in substance_alphabet_dict:
                    substance_alphabet_dict[s] += 1
                else:
                    substance_alphabet_dict[s] = 1
                for li, line in enumerate(table):
                    for ei, element in enumerate(line):
                        if s == element:
                            line_number = li
                            element_number = ei
                            if line_number != 0:
                                cipher_text += table[line_number - 1][element_number]
                            else:
                                cipher_text += table[len(table) - 1][element_number]
            else:
                cipher_text += s
        print('trisemus_table.decryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(substance_alphabet_dict.keys()), substance_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы зашифровонного алфавита trisemus_table')
        plt.show()
        return cipher_text


if __name__ == '__main__':
    text = ''
    with open('is_text.txt', 'r', encoding='utf-8') as source:
        text = source.read()
    with open('ci_text.txt', 'w', encoding='utf-8') as cipher_text:
        cipher_text.write(сaesar('encryption', text.lower(), 'інфарматыка', 2))
    with open('dec_text.txt', 'w', encoding='utf-8') as decryption_text:
        decryption_text.write(
            сaesar('decryption', сaesar('encryption', text.lower(), 'інфарматыка', 2), 'інфарматыка', 2))
    with open('ci_text_tr.txt', 'w', encoding='utf-8') as cipher_text:
        cipher_text.write(trisemus_table('encryption', text.lower(), 'яраслаў'))
    with open('dec_text_tr.txt', 'w', encoding='utf-8') as decryption_text:
        decryption_text.write(
            trisemus_table('decryption', trisemus_table('encryption', text.lower(), 'яраслаў'), 'яраслаў'))
