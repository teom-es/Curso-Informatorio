print('Hola, este es el juego del ahorcado')
print('En este juego tendra 6 oportunidades para completar la palabra o adivinar la palabra')
print('Reglas del juego')
print('Solo se puede intentar adivinar una letra o palabra por turno')
print('Cada acierto incorrecto sera una oportunidad menos para adivinar la palabra')
print('No se pueden usar ni letras ni palabras repetidas \n')
print('Se pueden elegir tanto letras como palabras, pero no numeros ni caracteres especiales')
print('Que comience el juego')

letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z')

f = open('palabras.txt', 'r', encoding='utf-8')
diccionario = f.readlines()
f.close()

diccionario = [p.strip() for p in diccionario]

palabra = input('Ingrese la palabra para el ahorcado')

if palabra in diccionario:
    print('si')
else:
    print('no')
