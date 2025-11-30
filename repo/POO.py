'''
class Perro:
    def __init__(self, nombre, raza, edad):
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
    def ladrar(self):
        print('guau')
    def saludar(self):
        print(f'Hola, soy un perro llamado {self._nombre} de raza {self._raza}.')
    def comer(self):
        print(f'{self._nombre} esta comiendo')
    def dormir(self):
        print(f'{self._nombre} esta durmiendo')
    def envejecer(self):
        self._edad += 1
    def edad(self):
        return self._edad
    

perro = Perro('maria', 'callejera', 10)

print(perro._nombre)
print(perro._raza)
print(perro._edad)

perro.ladrar()
perro.saludar()
perro.envejecer()
perro.edad()

class Perrodomesticado(Perro):
    def __init__(self, nombre, raza, edad, duenio):
        super().__init__(nombre, raza, edad)
        self.duenio = duenio
    def saludar(self):
        print(f'Hola soy {self._nombre}, soy un perro de raza {self._raza}, mi duenio es {self.duenio}')
    def ladrar(self):
        return super().ladrar()
    

perrodos = Perrodomesticado('Max', 'Callejero', 10, 'Teo')
perrodos.ladrar()
perrodos.saludar()
'''

'''Libros'''


class Libro:
    def __init__(self, titulo, autor, ISBN, num_pag, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.num_pag = num_pag
        self.genero = genero 
    def prestar():
        
    def devolver()
    def buscarporTitulo()
