import random
import itertools
import regulare as curp

abce = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z'


def createAlphabeat():
    alf = [] 
    opc = int(input('Como se ingresaran los datos? \n 1)Rango \n 2)1x1\n'))
    if opc == 1:
        inpt = str(input('Ingresa el rango del alfabeto: '))
        _a = inpt.split('-')
        _b = _a[0]
        print(_b)
        if _b.isdigit():
            for i in range(int(_a[0]),int(_a[1])+1):
                alf.append(str(i))
            return alf
        else:
            for letter in abce:
                if letter >= _a[0] and letter <= _a[1]:
                    alf.append(letter)
            return alf

    elif opc == 2:    
        inpt = int(input('Cuantos elementos agregaras? '))
        for i in range(inpt):
            elem = input('Ingresa el elemento {}'.format(i+1))
            alf.append(elem)
        return alf

'''Parte con duda'''
def generateLanguage(alphabeat,n):
    language = []
    lenlanguage = int(input('Cuantas palabras se van a generar en el lenguaje {}?'.format(n)))
    lenwords = int(input('Que longitud tendra cada palabra?'))
    for i in range(lenlanguage):
        word = ''
        for j in range(lenwords):
            word += random.choice(alphabeat)
        if word in language:
            i -= 1
        else:
            language.append(word)
    return language


def unionLanguage(language_1,language_2):
    union_language = list(set(language_1).union(language_2))
    return union_language


def concatenateLanguage(language_1,language_2):
    concatenate = []
    for elem in language_1:
        for word in language_2:
            _w = str(elem) + str(word)
            concatenate.append(_w)
    return concatenate


def differenceLanguages(language_1,language_2):
    dif = []
    for elem in language_1:
        if elem not in language_2:
            dif.append(elem)
    return dif


def _getRange():
    ran = int(input('Ingresa la potencia del lenguaje: '))
    if(ran >= -5 and ran <= 5):
        return ran
    else:
        return _getRange()

def _selectLanguage():
    option = int(input('De que lenguaje quieres generar la potencia? \n 1)Lenguage 1 \n 2)Lenguaje 2 \n'))
    if(option != 1 and option != 2):
        return _selectLanguage()
    else:
        return option

def powerLanguage(language_1,language_2,opc,opc_rango):
    language_p = []
    _b = []
    if(opc == 1):
        if(opc_rango == 0):
            language_p.append('λ')
            return language_p
        else: 
            if(opc_rango < 0):
                opc_rango *= -1    
                for i in range(opc_rango):
                    _b.append(language_1)
                for j in itertools.product(*_b):
                    language_p.append(j) 
                language_p = list(reversed(language_p))
                return language_p
            else:     
                for i in range(opc_rango):
                    _b.append(language_1)
                for j in itertools.product(*_b):
                    language_p.append(j) 
                language_p = list(reversed(language_p))
                return language_p

    else:
        if(opc_rango < 0):
            opc_rango *= -1    
            for i in range(opc_rango):
                _b.append(language_2)
            for j in itertools.product(*_b):
                language_p.append(j) 
            language_p = list(reversed(language_p))
            return language_p
        else:     
            for i in range(opc_rango):
                _b.append(language_2)
            for j in itertools.product(*_b):
                language_p.append(j) 
            language_p = list(reversed(language_p))
            return language_p

if __name__ == '__main__':
    alphabeat = createAlphabeat()
    print('El alfabeto es: \n {}'.format(alphabeat))
    language_1 = generateLanguage(alphabeat,1)
    language_2 = generateLanguage(alphabeat,2)
    print('El lenguaje 1 es: \n {} '.format(language_1))
    print('El lenguaje 2 es: \n {} '.format(language_2))
    language_Union = unionLanguage(language_1,language_2)
    print('La union de los lenguajes 1 y 2 es:\n {}'.format(language_Union))
    language_Con = concatenateLanguage(language_1,language_2)
    print('La concatenacion de los lenguajes 1 y 2 es: \n {}'.format(language_Con))
    language_Dif = differenceLanguages(language_1,language_2)
    print('La diferencia del lenguage 1 con el lenguage 2 es: \n {}'.format(language_Dif))
    opc = _selectLanguage()
    opc_rango = _getRange()
    language_Power = powerLanguage(language_1, language_2, opc, opc_rango)
    print('El lenguaje {} a la potencia {} es: \n {}'.format(opc, opc_rango, language_Power))
    curp.make_curp()
    curp.comparar()