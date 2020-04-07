from lab3 import primeSearch, findNOD

if __name__ == '__main__':
    while True:
        print()
        print('1 - нахождение НОД ')
        print('2 - нахождение всех простых чисел из интервала ')
        print('введите номер задания, для выхода нажмите 0: ', end=' ')
        inp = int(input())
        if inp == 0:
            break
        elif inp == 1:
            print('введите через запятую 2 или 3 числа для нахождения их НОД: ', end=' ')
            inpnod = str(input()).split(',')
            if len(inpnod) == 2:
                print(f'НОД равен: {findNOD.findNOD(int(inpnod[0]), int(inpnod[1]))}')
            elif len(inpnod) == 3:
                print(f'НОД равен: {findNOD.findNOD(int(inpnod[0]), int(inpnod[1]), int(inpnod[2]))}')
            else:
                print('неверное количество чисел')
        elif inp == 2:
            print('введите через запятую число или интервал для нахождения всех простых чисел: ', end=' ')
            inpprime = str(input()).split(',')
            if len(inpprime) == 1:
                print(f'количество простых чисел равно: {len(primeSearch.primeSearch(int(inpprime[0])))}')
            elif len(inpprime) == 2:
                print(f'количество простых чисел равно: {len(primeSearch.primeSearch(int(inpprime[1]), int(inpprime[0])))}')
            else:
                print('неверное количество чисел')
        else:
            print('такого номера нет')
