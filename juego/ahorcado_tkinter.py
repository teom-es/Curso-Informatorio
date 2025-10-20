import tkinter as tk
import random

ventana = tk.Tk()
ventana.title('Mi primer juego en python')
ventana.geometry('1000x1000')

etiquetas = {
    'etiqueta1' :  tk.Label(ventana, text= '-----Hola, este es el juego del ahorcado-----\n'),
    'etiqueta2' : tk.Label(ventana, text= 'En este juego tendra 6 oportunidades para completar la palabra o adivinar la palabra \n'),
    'etiqueta3' :  tk.Label(ventana, text= 'Reglas del juego \n'),
    'etiqueta4' :  tk.Label(ventana, text= 'Solo se puede intentar adivinar una letra o la palabra por cada turno \n'),
    'etiqueta5' :  tk.Label(ventana, text= 'Contara con 6 vidas para adivinar la palabra. Cada acierto incorrecto sera una oportunidad menos para adivinar la palabra \n'),
    'etiqueta6' :  tk.Label(ventana, text= 'No se pueden usar numeros o caracteres especiales para adivinar la palabra, en ese caso se le restara una vida \n'),
    'etiqueta7' :  tk.Label(ventana, text= 'Tampoco se pueden usar ni letras ni palabras repetidas \n'),
    'etiqueta8' :  tk.Label(ventana, text= 'Que comience el juego'),
}

for etiqueta in etiquetas.values():
    etiqueta.pack()

resultado = False

soga = tk.Label(ventana,  text= '__________ ')
palo1 = tk.Label(ventana, text= '|          ')
palo2 = tk.Label(ventana, text= '|          ')
palo3 = tk.Label(ventana, text= '|          ')

cabeza = tk.Label(ventana,  text= '|        O ')
torso = tk.Label(ventana,   text= '|       /|\\ ')
cintura = tk.Label(ventana, text= '|        | ')
piernas = tk.Label(ventana, text= '|       / \\ ')

brazo1 = tk.Label(ventana,  text= '|       /| ')
brazo2 = tk.Label(ventana,  text= '|        |\\ ')
pierna1 = tk.Label(ventana, text= '|       /  ')
pierna2 = tk.Label(ventana, text= '|         \\ ')

global entrada
global comentario1
global comentario2
global comentario3
global comentario4
global comentario5
global comentario6
global comentario7
global comentario8
global comentario9
global list_ad
global list_pa
global palabra
list_ad = tk.Listbox(ventana)
list_pa = tk.Listbox(ventana)
comentario1 = tk.Label(ventana, text= 'Incorrecto, la letra o palabra son incorrectos')
comentario2 = tk.Label(ventana, text= 'O ingreso un numero o caracter especial, por lo que se le restara una vida')
comentario3 = tk.Label(ventana, text= 'Vidas restantes: ')
comentario4= tk.Label(ventana)
comentario5 = tk.Label(ventana, text= 'Letra ya usada')
comentario6 = tk.Label(ventana, text= 'Adivinado')
comentario7 = tk.Label(ventana, text= 'Has perdido')
comentario8 = tk.Label(ventana, text= 'Felicidades has ganado!')
comentario9 = tk.Label(ventana, text= 'La palabra completa era: ')
entrada = tk.Entry(ventana)
palabra2 = tk.Label(ventana)

vidas = 6

def juego_ ():
    juego.pack_forget()
    for etiqueta in etiquetas.values():
        etiqueta.destroy()
    f = open('palabras.txt', 'r', encoding='utf-8')
    diccionario = f.readlines()
    f.close()
    diccionario = [p.strip() for p in diccionario]
    palabra = random.choice(diccionario)
    palabra2.config(text= palabra)
    palabra2.pack()
    for letra in palabra:
        list_ad.insert(tk.END, "_")
    soga.pack()
    palo1.pack()
    palo2.pack()
    palo3.pack()
    entrada.pack()
    def obtener_letra():
        global vidas
        global resultado
        respuesta = entrada.get()
        adivinado = list_ad.get(0, tk.END)
        if respuesta in adivinado:
            comentario5.pack()
        elif respuesta == palabra:
            comentario6.pack()
            resultado = True
        elif respuesta in palabra:
            i = 0
            for letra in palabra:
                if (respuesta == letra):
                    list_ad.delete(i)
                    list_ad.insert(i,respuesta)
                    list_ad.config(height=list_ad.size())
                    adivinado = list_ad.get(0, tk.END)
                if '_' not in adivinado:
                    resultado = True
                i = i + 1 
            list_pa.insert(tk.END, respuesta)
            list_pa.config(height=list_pa.size())
            list_ad.pack_forget()
            list_ad.pack()
            list_pa.pack_forget()
            list_pa.pack()
            entrada.pack_forget()
            entrada.pack()
            boton.pack_forget()
            boton.pack()
        else:
            list_pa.insert(tk.END, respuesta)
            list_pa.config(height=list_pa.size())
            vidas = vidas - 1
            comentario4.config(text= vidas)
            comentario4.pack_forget()
            comentario1.pack_forget()
            comentario2.pack_forget()
            comentario3.pack_forget()
            comentario1.pack()
            comentario2.pack()
            comentario3.pack()
            comentario4.pack()
            if vidas == 5:
                soga.pack_forget()
                palo1.pack_forget()
                palo2.pack_forget()
                palo3.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                palo1.pack()
                palo2.pack()
                list_ad.pack()
                list_pa.pack()
                entrada.pack()
                boton.pack()
            elif vidas == 4:
                soga.pack_forget()
                cabeza.pack_forget()
                palo1.pack_forget()
                palo2.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                cintura.pack()
                palo1.pack()
                list_ad.pack()
                list_pa.pack()
                entrada.pack()
                boton.pack()
            elif vidas == 3:
                soga.pack_forget()
                cabeza.pack_forget()
                cintura.pack_forget()
                palo1.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                brazo1.pack()
                cintura.pack()
                list_ad.pack()
                list_pa.pack()
                entrada.pack()
                boton.pack()
            elif vidas == 2:
                soga.pack_forget()
                cabeza.pack_forget()
                brazo1.pack_forget()
                cintura.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                torso.pack()
                cintura.pack()
                list_ad.pack()
                list_pa.pack()
                entrada.pack()
                boton.pack()
            elif vidas == 1:
                soga.pack_forget()
                cabeza.pack_forget()
                torso.pack_forget()
                cintura.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                torso.pack()
                cintura.pack()
                pierna2.pack()
                list_ad.pack()
                list_pa.pack()
                entrada.pack()
                boton.pack()
            elif vidas == 0:
                soga.pack_forget()
                cabeza.pack_forget()
                torso.pack_forget()
                cintura.pack_forget()
                pierna2.pack_forget()
                list_ad.pack_forget()
                list_pa.pack_forget()
                entrada.pack_forget()
                boton.pack_forget()
                soga.pack()
                cabeza.pack()
                torso.pack()
                cintura.pack()
                piernas.pack()
                list_ad.pack()
                list_pa.pack()
        entrada.delete(0, tk.END)
        if vidas == 0:
            comentario7.pack()
            juego.pack_forget()
            juego.config(text='Reintentar', command= reiniciar)
            juego.pack()
        elif resultado == True:
            comentario8.pack()
            comentario9.pack()
            palabra2.pack()
            juego.pack_forget()
            juego.config(text='Reintentar', command= reiniciar)
            juego.pack()
    boton = tk.Button(ventana, text='Enviar',command= obtener_letra)
    boton.pack()

def reiniciar ():
    entrada.pack_forget()
    list_pa.pack_forget()
    list_ad.pack_forget()
    juego.pack_forget()
    palabra2.pack_forget()
    comentario1.pack_forget()
    comentario2.pack_forget()
    comentario3.pack_forget()
    comentario4.pack_forget()
    comentario5.pack_forget()
    comentario6.pack_forget()
    comentario7.pack_forget()
    comentario8.pack_forget()
    comentario9.pack_forget()
    soga.pack_forget()
    palo1.pack_forget()
    palo2.pack_forget()
    palo3.pack_forget()
    cabeza.pack_forget()
    torso.pack_forget()
    cintura.pack_forget()
    piernas.pack_forget()
    brazo1.pack_forget()
    brazo2.pack_forget()
    pierna1.pack_forget()
    pierna2.pack_forget()
    juego_()

juego = tk.Button(ventana, text='Ejecutar juego', command= juego_)
juego.pack()
ventana.mainloop()



