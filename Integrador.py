# Ejercicio Integrado
# Diseñar una APP
# Agenda telefonica de ubicacion de los internos a nivel de infraestructura de uno varios sanatorios
# Unidad 3 – Toma de datos
# Unidad 4  y 5 – Uso de funciones, condicionales y bucles.
# Unidad 6 – Uso de base de datos (MySQL ó SQLite3 a elección). En algunos sistemas operativos la 
# implementación de Python con MySQL toma un tiempo pues el sistema operativo puede que no tenga 
# algún archivo necesario para la conexión, en estos casos se recomienda el uso de SQLite3 mientras 
# se pone el sistema operativo en condiciones de trabajo. 
# Aquí se pide: 
#   Creación de base de datos y tablas desde Python.
#   Realizar un alta de registro en la base de datos solicitando al usuario que ingrese los datos ya 
# sea mediante consola si solo se utiliza Python o mediante campos del tipo Entry si se utiliza Tkinter.
# Unidad 7 y 8: Implementación de regex para validación de uno de los datos tomados en la unidad 6, 
# realización de abmc (crud en ingles) (alta, baja, modificación, consulta) 

from tkinter import *
from tkinter import messagebox
import BaseSQL





lista = []

def guardar(): #Funcion de Guardar en Lista // Pasar a guardar en base de datos SQLITE
    num = interno.get()
    numt = tipo.get()
    numr = reflejo.get()
    nump = patchera.get()
    numsdd = sdDatos.get()
    numuser = usuario.get()
    numubica = ubicacion.get()
    numsanatorio = sanatorio.get()
    numfecha = fechaAct.get()
    lista.append(
        num+"$"+
        numt+"$"+
        numr+"$"+
        nump+"$"+
        numsdd+"$"+
        numuser+"$"+
        numubica+"$"+
        numsanatorio+"$"+
        numfecha
        )
    #lista.append(str(interno)+"$"+str(tipo)+"$"+str(reflejo)+"$"+str(patchera)+"$"+str(sdDatos)+"$"+str(usuario))
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
    interno.set("")
    tipo.set("")
    reflejo.set("")
    patchera.set("")
    sdDatos.set("")
    usuario.set("")
    ubicacion.set("")
    sanatorio.set("")
    fechaAct.set("")
    consultar()
    

def eliminar(): #Funcion Eliminar
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if conteliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)
   

def consultar(): #Funcion Consultar en la BD tiene problemas 
    r = Text(ventana, width=100, height=10)
    lista.sort()
    valores =[]
    r.insert(INSERT, "Interno\t\tTipo\t\tReflejos\t\tSala datos\t\tPatchera\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[5])
        r.insert(INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
        r.place(x=20,y=300)
        spinTelefono = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=450, y=50)
        if lista ==[]:
            spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)
        r.config(state=DISABLED)

def iniciarArchivo(): #Funcion de iniciar BD Hay q pasarla a Sqlite
    archivo = open("BD.txt","a")
    archivo.close()

def cargar(): #Funcion de cargar BD hay q pasarla a SQL lite
    archivo = open("BD.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto(): #funcion de escribir en la bd
    archivo = open("BD.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()

#Configuracion Ventana 
ventana = Tk()
colorFondo = "#006"
colorLetra = "#FFF"
ventana.title("Agenda con archivos")
ventana.geometry("850x500")
ventana.configure(background = colorFondo)

#Declaracion de variables tk
interno = StringVar()
tipo = StringVar()
reflejo = StringVar()
patchera = StringVar()
sdDatos = StringVar()
conteliminar = StringVar()
ubicacion = StringVar()
usuario = StringVar()
sanatorio = StringVar()
fechaAct = StringVar()

#Inicializando las funciones
iniciarArchivo()
cargar()
consultar()

#Etiquetas y Cajas
etiquetaTitulo = Label(ventana, text="Agenda de Internos",bg=colorFondo, fg=colorLetra).place(x=270,y=10)
etiquetaI = Label(ventana, text="Interno", bg=colorFondo,fg=colorLetra).place(x=50, y=50)
cajaI = Entry(ventana, textvariable=interno).place(x=150, y=50)
etiquetaT = Label(ventana, text="Tipo", bg=colorFondo,fg=colorLetra).place(x=50, y=80)
cajaT = Entry(ventana, textvariable=tipo).place(x=150, y=80)
etiquetaR = Label(ventana, text="Reflejo", bg=colorFondo,fg=colorLetra).place(x=50, y=110)
cajaR = Entry(ventana, textvariable=reflejo).place(x=150, y=110)
etiquetaD = Label(ventana, text="Sala datos", bg=colorFondo,fg=colorLetra).place(x=50, y=140)
cajaD = Entry(ventana, textvariable=sdDatos).place(x=150, y=140)
etiquetaP = Label(ventana, text="Patchera", bg=colorFondo,fg=colorLetra).place(x=50, y=170)
cajaP = Entry(ventana, textvariable=patchera).place(x=150, y=170)
etiquetaUser = Label(ventana, text="Usuario", bg=colorFondo,fg=colorLetra).place(x=50, y=200)
cajaUser = Entry(ventana, textvariable=usuario).place(x=150, y=200)
etiquetaUbi = Label(ventana, text="Ubicacion", bg=colorFondo,fg=colorLetra).place(x=50, y=230)
cajaUbi = Entry(ventana, textvariable=ubicacion).place(x=150, y=230)


etiquetaEliminar = Label(ventana, text="Interno: ", bg= colorFondo,fg=colorLetra).place(x=370, y=50)
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)

#Botones
bGuardar = Button(ventana, text="Guardar", command=guardar, bg="#009",fg="white").place(x=320, y=230)
bEliminar = Button(ventana, text="Eliminar", command=eliminar, bg="#009",fg="white").place(x=490, y=80)
bConsultar = Button(ventana, text="Consultar", command=consultar, bg="#009",fg="white").place(x=490, y=117)

mainloop()