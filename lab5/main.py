from datetime import datetime
import matplotlib.pyplot as plt

ALPHABET = 'абвгдеёжзійклмнопрстуўфхцчшыьэюя'


def routing(action, source):
    start_time = datetime.now()
    alphabet = list(set(source))
    cipher_text = ''
    table = [[], [], [], [], [], []]
    source_alphabet_dict = {}
    substance_alphabet_dict = {}
    if action == 'encryption':
        line_number = 0
        element_number = 0
        for s in source:
            if s in ALPHABET:
                if s in source_alphabet_dict:
                    source_alphabet_dict[s] += 1
                else:
                    source_alphabet_dict[s] = 1
            if element_number != 601:
                table[line_number].append(s)
                element_number += 1
            else:
                line_number += 1
                element_number = 1
                table[line_number].append(s)
        for v0, v1, v2, v3, v4, v5 in zip(table[0], table[1], table[2], table[3], table[4], table[5]):
            value = v0 + v1 + v2 + v3 + v4 + v5
            cipher_text += value
        print('routing.encryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(source_alphabet_dict.keys()), source_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы исходного алфавита')
        plt.show()
    elif action == 'decryption':
        line_number = 0
        for s in source:
            if s in ALPHABET:
                if s in substance_alphabet_dict:
                    substance_alphabet_dict[s] += 1
                else:
                    substance_alphabet_dict[s] = 1
            if line_number != 6:
                table[line_number].append(s)
                line_number += 1
            else:
                line_number = 0
                table[line_number].append(s)
                line_number += 1
        v_list = []
        for v in table:
            for e in v:
                v_list.append(e)
        cipher_text = cipher_text.join(v_list)
        print('routing.decryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(substance_alphabet_dict.keys()), substance_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы алфавита')
        plt.show()
    return cipher_text


def multiple_permutation(action, source, keyword1, keyword2):
    start_time = datetime.now()
    alphabet = list(set(source))
    cipher_text = ''
    table = []
    table_true = []
    table_true_second = []
    columns_second = []
    dict_column = {}
    dict_column_index = {}
    dict_row = {}
    dict_row_index = {}
    for i in range(0, len(keyword2)):
        table.append([])
    for i in range(0, len(keyword1)):
        columns_second.append([])
    source_alphabet_dict = {}
    substance_alphabet_dict = {}
    if action == 'encryption':
        line_number = 0
        element_number = 0
        for s in source:
            if s in ALPHABET:
                if s in source_alphabet_dict:
                    source_alphabet_dict[s] += 1
                else:
                    source_alphabet_dict[s] = 1
            if line_number != len(keyword2):
                if element_number != len(keyword1):
                    table[line_number].append(s)
                    element_number += 1
                elif line_number != len(keyword2) - 1:
                    line_number += 1
                    element_number = 1
                    table[line_number].append(s)
        for s, l in zip(keyword2, table):
            dict_row[s] = l
        for j in keyword2:
            Ai = ALPHABET.index(j)
            dict_row_index[Ai] = j
        for e in range(0, len(ALPHABET)):
            if e in dict_row_index.keys():
                table_true.append(dict_row[dict_row_index[e]])
        for ri, row in enumerate(table_true):
            for ei, element in enumerate(row):
                columns_second[ei].append(element)
        for s, l in zip(keyword1, columns_second):
            if s in dict_column.keys():
                dict_column[s + '2'] = l
            else:
                dict_column[s] = l
        for j in keyword1:
            Ai = ALPHABET.index(j)
            if Ai in dict_column_index.keys():
                dict_column_index[Ai + 0.1] = j
            else:
                dict_column_index[Ai] = j
        for e in range(0, len(ALPHABET)):
            if e in dict_column_index.keys():
                table_true_second.append(dict_column[dict_column_index[e]])
                if e + 0.1 in dict_column_index.keys():
                    table_true_second.append(dict_column[dict_column_index[e + 0.1] + '2'])
        v_list = []
        for v in table_true_second:
            for e in v:
                v_list.append(e)
        cipher_text = cipher_text.join(v_list)
        print('multiple_permutation.encryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(source_alphabet_dict.keys()), source_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы исходного алфавита')
        plt.show()
    elif action == 'decryption':
        for i in range(0, len(keyword1)):
            table_true_second.append([])
        line_number = 0
        element_number = 0
        for s in source:
            if s in ALPHABET:
                if s in substance_alphabet_dict:
                    substance_alphabet_dict[s] += 1
                else:
                    substance_alphabet_dict[s] = 1
            if line_number != len(keyword1):
                if element_number != len(keyword2):
                    table_true_second[line_number].append(s)
                    element_number += 1
                elif line_number != len(keyword1) - 1:
                    line_number += 1
                    element_number = 1
                    table_true_second[line_number].append(s)
        for j in keyword1:
            Ai = ALPHABET.index(j)
            if j in dict_column_index.keys():
                dict_column_index[j + '2'] = Ai
            else:
                dict_column_index[j] = Ai
        temp = []
        for i in range(0, len(keyword1)):
            temp.append([])
        h = 0
        for e in ALPHABET:
            if e in dict_column_index.keys():
                ai = keyword1.index(e)
                temp[ai] = table_true_second[h]
                h += 1
                if e + '2' in dict_column_index.keys():
                    ai = 5
                    temp[ai] = table_true_second[h]
                    h += 1
        for i in range(0, len(keyword2)):
            table_true.append([])
        for ri, row in enumerate(temp):
            for ei, element in enumerate(row):
                table_true[ei].append(element)
        for j in keyword2:
            Ai = ALPHABET.index(j)
            if j in dict_row_index.keys():
                dict_row_index[j + '2'] = Ai
            else:
                dict_row_index[j] = Ai
        temp = []
        for i in range(0, len(keyword2)):
            temp.append([])
        h = 0
        for e in ALPHABET:
            if e in dict_row_index.keys():
                ai = keyword2.index(e)
                temp[ai] = table_true[h]
                h += 1
                if e + '2' in dict_row_index.keys():
                    ai = 5
                    temp[ai] = table_true[h]
                    h += 1
        v_list = []
        for v in temp:
            for e in v:
                v_list.append(e)
        cipher_text = cipher_text.join(v_list)
        print('multiple_permutation.decryption: ' + str(datetime.now() - start_time))
        fig, ax = plt.subplots()
        plt.bar(list(substance_alphabet_dict.keys()), substance_alphabet_dict.values(), color='g')
        ax.set_ylabel('количество появившихся символов')
        ax.set_xlabel('символы алфавита')
        plt.show()
    return cipher_text


if __name__ == '__main__':
    text = ''
    with open('is_text.txt', 'r', encoding='utf-8') as source:
        text = source.read()
    with open('ci_text.txt', 'w', encoding='utf-8') as cipher_text:
        cipher_text.write(routing('encryption', text.lower()))
    with open('dec_text.txt', 'w', encoding='utf-8') as decryption_text:
        decryption_text.write(
            routing('decryption', routing('encryption', text.lower())))
    with open('ci_text_m.txt', 'w', encoding='utf-8') as cipher_text:
        cipher_text.write(multiple_permutation('encryption', text.lower(), 'яраслаў', 'піцуха'))
    with open('dec_text_m.txt', 'w', encoding='utf-8') as decryption_text:
        decryption_text.write(
            multiple_permutation('decryption', multiple_permutation('encryption', text.lower(), 'яраслаў', 'піцуха'), 'яраслаў', 'піцуха'))
