import tkinter as tk

def tkinter_saludar():
    ventana = tk.Tk()
    ventana.title('Mi primer ventana con tkinter')
    ventana.geometry('400x400')

    etiqueta = tk.Label(ventana, text='Hola mundo!', font=('Arial',20))
    etiqueta.pack()



def saludar():
    print('Hola mundo!')

ventana = tk.Tk()
ventana.title('Tres botones para saludar!')
ventana.geometry('500x500')

boton1 = tk.Button(ventana, text='Boton 1', command=saludar)
boton2 = tk.Button(ventana, text='Boton 2', command=saludar)
boton3 = tk.Button(ventana, text='Boton 3', command=saludar)
boton4 = tk.Button(ventana, text='Boton 4: tkinter saludar', command=tkinter_saludar)

boton1.pack(side='top')
boton2.pack(side='left')
boton3.pack(side='right')
boton4.pack(side='bottom')

ventana.mainloop()