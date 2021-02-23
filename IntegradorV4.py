import tkinter as tk
from tkinter import Button, Entry, IntVar, Label, StringVar, ttk, scrolledtext 
from tkinter import LabelFrame, Tk, messagebox
import sqlite3


def conectadb():
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        
    except sqlite3.OperationalError:
        pass
    finally:
        return cursor

def creaddb():
    try:
        cursor = conectadb()
        cursor.execute("CREATE TABLE PALERMO(interno INTERGER(20), tipo VARCHAR(20), equu VARCHAR(20), ubicapatch VARCHAR(20), ssdatos VARCHAR(20), usuario VARCHAR(20))")
    except sqlite3.OperationalError:
        pass    

def altadb():
    creaddb()
    cursor = conectadb()
    sql = "insert into PALERMO (interno, tipo, equu, ubicapatch, ssdatos, usuario) values (?,?,?,?,?,?)"
    alta = cursor.execute(sql,datos)
    cursor.commit()
    cursor.close()
    return alta
    
def consultadb():
    try:
        cursor = conectadb()
        cursor.execute("SELECT tipo, equu, ubicapatch, ssdatos, usuario FROM PALERMO where interno=?")
        cursor.fetchall()
        cursor.close()
    finally:
        return cursor.fetchall()
    
def bajadb():
    try: 
        cursor = conectadb()
        cursor.execute("DELETE tipo, equu, ubicapatch, ssdatos, usuario FROM PALERMO where interno=?")
        cursor.commit()
        cursor.close()
    finally:
        return cursor.fetchall()
    
def modificadb():
    cursor = conectadb()
    cursor.execute("UPDATE PALERMO SET tipo, equu, ubicapatch, ssdatos, usuario VALUES(?,?,?,?)")    
    cursor.commit()
    cursor.close()




conectadb()
   
    
#Ventana Principal
ventana = Tk()
ventana.geometry("800x400")
ventana.title("Integrador V4")
#******************************

datos = []
interno = IntVar()
tipo = StringVar()
patchera = StringVar()
equu = StringVar()
usuario = StringVar()
ssdatos = StringVar()

"""datos.append(interno+","+
            tipo+","+
            patchera+","+
            equu+","+
            ssdatos+","+
            usuario)"""

interno = interno.get()
tipo = tipo.get()
equu = equu.get()
patchera = patchera.get()
ssdatos = ssdatos.get()

#Pannel de pestañas
pestaña = ttk.Notebook(ventana)
p1 = ttk.Frame(pestaña)   # first page, which would get widgets gridded into it
p2 = ttk.Frame(pestaña)   # second page
pestaña.add(p1, text='Consulta')
pestaña.add(p2, text='Modificar')
pestaña.grid(column= 0, row=0)

#Penstaña Consulta
sInterno = Label(p1, text="Interno")
sInterno.grid(column=0, row=0, padx=0, pady=0)
sInternoEntry = Entry(p1, textvariable=interno)
sInternoEntry.grid(column=1 , row=0)

sTipo = Label(p1, text="Tipo")
sTipo.grid(column=0, row=1, padx=0, pady=0)
sTipoEntry = Entry(p1, textvariable=tipo, state="readonly")
sTipoEntry.grid(column=1 , row=1)

sEquu = Label(p1, text="Equu")
sEquu.grid(column=0, row=2, padx=0, pady=0)
sEquuEntry = Entry(p1, textvariable=equu, state="readonly")
sEquuEntry.grid(column=1 , row=2)

sPatchera = Label(p1, text="Patchera")
sPatchera.grid(column=0, row=3, padx=0, pady=0)
sPatcheraEntry = Entry(p1, textvariable=patchera, state="readonly")
sPatcheraEntry.grid(column=1 , row=3)

varSdDatos = Label(p1, text="Sala de datos")
varSdDatos.grid(column=0, row=4, padx=0, pady=0)
varSdDatosEntry = Entry(p1, textvariable=ssdatos, state="readonly")
varSdDatosEntry.grid(column=1 , row=4)

mostrarlabelframe = ttk.Labelframe(p1,text="Consulta")
mostrar = scrolledtext(mostrarlabelframe, width=30, height=10)



consulta = Button(p1, text="Consulta")
consulta.grid(column=1, row=7)

ventana.mainloop()






