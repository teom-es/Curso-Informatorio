print('Hola, este es el juego del ahorcado')
print('En este juego tendra 6 oportunidades para completar la palabra o adivinar la palabra')
print('Reglas del juego')
print('Solo se puede intentar adivinar una letra o palabra por turno')
print('Cada acierto incorrecto sera una oportunidad menos para adivinar la palabra')
print('No se pueden usar ni letras ni palabras repetidas \n')
print('Se pueden elegir tanto letras como palabras, pero no numeros ni caracteres especiales')
print('Que comience el juego')

print('__________'),
print('|        O ')
print('|       /|\ ')
print('|        | ')
print('|       / \ ')

letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z')

import random

f = open('palabras.txt', 'r', encoding='utf-8')
diccionario = f.readlines()
f.close()
diccionario = [p.strip() for p in diccionario]
palabra = random.choice(diccionario)

adivinado = []
palabras_usadas = []

for letra in palabra:
    adivinado.append('_')

print('__________'),
print('|')
print('|')
print('|')
print('|')
print(adivinado)

vidas = 6
resultado = False
print(palabra)

while (vidas != 0) and (resultado != True):
    respuesta = input('Ingrese una letra o palabra ')
    if respuesta in adivinado:
        print('letra ya usada')
    elif respuesta == palabra:
        print('adivinado')
        resultado = True
    elif respuesta in palabra:
        i = 0
        for letra in palabra:
            if (respuesta == letra):
                adivinado.remove('_')
                adivinado.insert(i,respuesta)
            i = i + 1 
    else:
        print('Incorrecto, la letra o palabra son incorrectos')
        vidas = vidas - 1
        if vidas == 5:
            print('__________'),
            print('|        O ')
            print('|')
            print('|')
            print('|')
        elif vidas == 4:
            print('__________'),
            print('|        O')
            print('|        |')
            print('|        |')
            print('|')
        elif vidas == 3:
            print('__________'),
            print('|        O')
            print('|       /|')
            print('|        |')
            print('|')
        elif vidas == 2:
            print('__________'),
            print('|        O')
            print('|       /|\ ')
            print('|        |')
            print('|')
        elif vidas == 1:
            print('__________'),
            print('|        O ')
            print('|       /|\ ')
            print('|        | ')
            print('|         \ ')
        elif vidas == 0:
            print('__________'),
            print('|        O ')
            print('|       /|\ ')
            print('|        | ')
            print('|       / \ ')
    palabras_usadas.append(respuesta)
    print(adivinado)
    print(palabras_usadas)