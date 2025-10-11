'DATOS BASICOS DE PYTHON'

print('hola mundo!')

nombre = input('Ingrese su nombre ')
print(nombre)
print(type(nombre))

edad = int(input('Ingrese su edad '))
print(edad)
print(type(edad))

mayor_edad = True
print(mayor_edad)
print(type(mayor_edad))

valor_decimal = float(input('Ingrese un numero con coma '))
print(valor_decimal)
print(type(valor_decimal))

'ESTRUCTURAS DE DATOS'

'LISTAS'
lista = ['dato', 123, True]
print(lista[0],' ', type(lista[0]),' / ',lista[1],' ', type(lista[1]),' / ',lista[2],' ', type(lista[2]), '\n')

lista = ['dato', 123, True]
print(lista[-1],' ', type(lista[-1]),' / ',lista[-2],' ', type(lista[-2]),' / ',lista[-3],' ', type(lista[-3]), '\n')

lista = [123, True, 'dato']
print(lista[0],' ', type(lista[0]),' / ',lista[1],' ', type(lista[1]),' / ',lista[2],' ', type(lista[2]), '\n')

lista2 = ['dato', 'dato', 'dato']
print(lista2[0],' ', type(lista2[0]),' / ',lista2[1],' ', type(lista2[1]),' / ',lista2[2],' ', type(lista2[2]), '\n')

lista3 = ['dato x', 'Primer lista', lista, 'Segunda lista', lista2]
print(lista3, '\n')

lista2[2] = 'nuevo_dato'
print(lista2, '\n')

lista_nueva = [1, 2]
print(lista_nueva)
lista_nueva.append(3)
print(lista_nueva)
lista_nueva.remove(1)
print(lista_nueva)

'TUPLAS'
tupla = (1, 2, 3, 'dato', True)
print(tupla, '\n')
tupla = (1)
print(tupla, '\n')

'CONJUNTOS'

colores = {'rojo', 'verde', 'amarillo', 'sandia'}
frutas = {'manzana', 'banana', 'sandia', 'rojo'}

if 'rojo' in colores:
    print('rojo esta en el colores')
else:
    print('rojo no esta en el colores')

for i in colores:
    print(i)

frutas_y_colores = frutas | colores
repetidos = frutas & colores
diferencia = frutas - colores

print(frutas_y_colores)
print(repetidos)
print(diferencia)

'DICCIONARIOS'

curso = {
    'estudiantes' : {
        'nombre': 'teo',
        'apellido': 'mielich',
        'edad': 21,
        'residencia' : {
            'provincia' : 'Chaco',
            'ciudad' : 'Resistencia'
        }
    },
    'profesores' : {
        'nombre': 'juan',
        'apellido': 'gomez',
        'materia': 'matematica'
    },
    'horarios' : [
        '10:00-12:00' ,
        '19:00-21:00'
    ]
}

print(curso)
print(type(curso))

print(curso['estudiantes'])
print(curso['horarios'][0])


'BUCLES FOR Y WHILE'

nombre = input('Ingrese su nombre ')
print(nombre)
print(type(nombre))

try:
    edad = int(input('Ingrese su edad '))
    print(edad)
    print(type(edad))
    if edad >= 18:
        mayor_edad = True
        print(mayor_edad)
        print(type(mayor_edad))
    else:
        mayor_edad = False
        print(mayor_edad)
        print(type(mayor_edad))
except ValueError:
    print('Error no se ingreso un numero')

bandera = False

while bandera == False:
    try:
        valor_decimal = float(input('Ingrese un numero con coma '))
        print(valor_decimal)
        print(type(valor_decimal))
        bandera = True
    except:
        print('Tiene que ingresar un numero con coma')


'HOLAAAAAAAAAAAAAAAAAAAAAAAAAAA'

