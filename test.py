from tkinter import *
from datetime import date
from datetime import datetime
import mysql.connector


agenda = Tk()
vari = StringVar()
hoy = date.today()

#Titulos de Tkinter.

Label(agenda, text= hoy.strftime('%d/%m/%Y')).grid(row=0, column=1, sticky=N)
Label(agenda, text="Hoy es:").grid(row=0, column=0, sticky=N)
Label(agenda, text="Año:").grid(row=1, column=0, sticky=N)
Label(agenda, text="Mes:").grid(row=2, column=0, sticky=N)
Label(agenda, text="Día:").grid(row=3, column=0, sticky=N)
Label(agenda, text="Ingrese el recordatorio:").grid(row=4, column=0, sticky=N)
Label(agenda, text="Evento hoy:").grid(row=5, column=0, sticky=N)

#Caracteristica de campos.

e1 = Entry(agenda)
e2 = Entry(agenda)
e3 = Entry(agenda)
e4 = Entry(agenda)
e5 = Label(agenda, textvariable = vari, padx =50, pady= 5)

#Posicion de campos

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

#Crea BD

def crearbd():
    mibase = mysql.connector.connect(   
        host="localhost",  
        user="gerardo",  
        passwd="6003823")
    micursor = mibase.cursor()
    micursor.execute("CREATE DATABASE Agenda")

#Crea la tabla

def crearagenda():
    mibase = mysql.connector.connect(   
        host="localhost",  
        user="root",  
        passwd="",
        database="Agenda")
    micursor = mibase.cursor()
    micursor.execute("CREATE TABLE Agenda(Fecha date NOT NULL,Recordatorio text NOT NULL)")

#Agrega recordatorios.

def alta():
    mibase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "Agenda"
    )        
    micursor = mibase.cursor()
    sql = "INSERT INTO Agenda (Fecha,Recordatorio) VALUES (%s,%s)"
    datos = (date(int(e1.get()),int(e2.get()),int(e3.get())),e4.get())
    micursor.execute(sql, datos)
    mibase.commit()

#Borra recordatorio en la fecha ingresada.

def borrar():
    mibase = mysql.connector.connect(
        host="localhost",  
        user="root",  
        passwd="",  
        database="Agenda"
    )
    micursor = mibase.cursor()
    sql = "DELETE FROM Agenda WHERE Fecha = %s"
    dato = (date(int(e1.get()),int(e2.get()),int(e3.get())),)
    micursor.execute(sql, dato)
    mibase.commit()

#Busqueda de recordatorio en el dia de la fecha.

def proximorecordatorio():
    mibase = mysql.connector.connect(
        host="localhost",  
        user="root",  
        passwd="",  
        database="Agenda"
    )
    micursor = mibase.cursor()
    sql = "SELECT Recordatorio FROM Agenda WHERE Fecha = %s"
    dato = (date.today(),)
    micursor.execute(sql,dato)
    resultado = micursor.fetchall()
    vari.set("")
    vari.set(resultado)
    
b = Button(agenda, text="Ingresar", command=alta, padx=5, pady=5)
b.grid(row=6, column=0)

c = Button(agenda, text="Proximo recodatorio", command=proximorecordatorio, padx=5, pady=5)
c.grid(row=6, column=3)

d = Button(agenda, text="Crear BD", command=crearbd, padx=5, pady=5)
d.grid(row=0, column=3)

e = Button(agenda, text="Borrar recordatorio", command=borrar, padx=5, pady=5)
e.grid(row=6, column=1)

f = Button(agenda, text="Crear Tabla", command=crearagenda, padx=5, pady=5)
f.grid(row=1, column=3)


mainloop()