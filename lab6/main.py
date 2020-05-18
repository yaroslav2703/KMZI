rotor = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['l', 'e', 'y', 'j', 'v', 'c', 'n', 'i', 'x',
     'w', 'p', 'b', 'q', 'm', 'd', 'r', 't', 'a',
     'k', 'z', 'g', 'f', 'u', 'h', 'o', 's'],
    ['f', 'k', 'q', 'h', 't', 'l', 'x', 'o', 'c',
     'b', 'j', 's', 'p', 'd', 'z', 'r', 'a', 'm',
     'e', 'w', 'n', 'i', 'u', 'y', 'g', 'v'],
    ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v',
     'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u',
     's', 'p', 'a', 'i', 'b', 'r', 'c', 'j']
]

reflector = {
    'a': 'e', 'b': 'n', 'c': 'k', 'd': 'q',
    'f': 'u', 'g': 'y', 'h': 'w', 'i': 'j',
    'l': 'o', 'm': 'p', 'r': 'x', 's': 'z', 't': 'v'
}

rotorShifts = [3, 1, 3]
# [11] Beta VIII I B Dunn 3-1-3


def shiftRotor(n):
    temp = []
    shCount = rotorShifts[n-1]
    for i in range(0, len(rotor[n])):
        if i - shCount < 0:
            temp.append(rotor[n][len(rotor[n]) + (i-shCount)])
        else:
            temp.append(rotor[n][i-shCount])
    for i in range(0, len(rotor[n])):
        rotor[n][i] = temp[i]


def Enigma(m):
    m = m.lower()
    encrypted_m = []

    for e in m:
        encrypted_m.append(e)

    for k in range(0, len(m)):
        for n in range(len(rotor) - 1, 0, -1):
            encrypted_m[k] = rotor[n][rotor[0].index(encrypted_m[k])]

        for e in reflector:
            if encrypted_m[k] == reflector[e]:
                encrypted_m[k] = e
            elif encrypted_m[k] == e:
                encrypted_m[k] = reflector[e]

        for n in range(1, len(rotor)):
            encrypted_m[k] = rotor[n][rotor[0].index(encrypted_m[k])]

        for i in range(1, len(rotor)):
            shiftRotor(i)
    print("".join(encrypted_m))


if __name__ == '__main__':
    message = str(input())
    Enigma(message)
