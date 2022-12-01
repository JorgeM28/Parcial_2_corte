from tkinter import *
import random

#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Generador de matriz")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="white")

m = StringVar()
b = StringVar()


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "green", width = 480 , height = 480)
frame_entrada.place(x = 10, y = 10)


lb_m = Label(frame_entrada, text = "Tamaño: ")
lb_m.config(bg="green2", fg="black", font=("Arial",16))
lb_m.place(x=10, y=400, width=115, height=30)

entry_m = Entry(frame_entrada, textvariable=m)
entry_m.config(font=("Arial",20), justify=LEFT,fg="black")
entry_m.focus_set()
entry_m.place(x=130, y=400, width=115, height=30)

lb_b = Label(frame_entrada, text = "Buscar: ")
lb_b.config(bg="green2", fg="black", font=("Arial",16))
lb_b.place(x=250, y=400, width=115, height=30)

entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(font=("Arial",20), justify=LEFT,fg="black")
entry_b.focus_set()
entry_b.place(x=370, y=400, width=100, height=30)

c = Canvas(frame_entrada, width=455,height=300)
c.place(x=10,y=10)
c.create_text(10 , 10)

def ventana_sec1():

    M = []

    for i in range(m):
        M.append([])
    for j in range(n):
        M[i].append(random.randint(1,9))

    # Mostrar matriz
    for k in range(m):
        print()
    for j in range(n):
        print(M[k][j], end= "\t")

    

bt_ejecutar = Button(frame_entrada, text="Crear la matriz", command=ventana_sec1)
bt_ejecutar.place(x=70, y=440, width=100, height=30)

bt_buscar = Button(frame_entrada, text="Buscar numero: ")
bt_buscar.place(x=300, y=440, width=100, height=30)

# Dimensiones de la matriz
n = m



ventana_principal.mainloop()