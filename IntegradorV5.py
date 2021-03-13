from sqlite3.dbapi2 import Cursor
import tkinter as tk
from tkinter import Button, Entry, IntVar, Label, StringVar, ttk, scrolledtext 
from tkinter import LabelFrame, Tk, messagebox
import sqlite3
from tkinter.constants import ANCHOR, CENTER, END, W
from typing import Text, TextIO


#Funciones de base de datos
#------------------------------------------------------------------------------------------------------------------------------------------
def conectadb():
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        sql = "CREATE TABLE PALERMO(interno VARCHAR(20) UNIQUE NOT NULL, tipo VARCHAR(20), equu VARCHAR(20), ubicapatch VARCHAR(20), ssdatos VARCHAR(20), usuario VARCHAR(20))"
        cursor.execute(sql)
    except sqlite3.OperationalError:
        pass
    finally:
        return con

def altadb():
    
    try:
        cursor = conectadb()
        sql = "INSERT INTO PALERMO (interno, tipo, equu, ubicapatch, ssdatos, usuario) values (?,?,?,?,?,?)"
        cursor.execute(sql,guardar())
        cursor.commit()
        cursor.close()
    except sqlite3.IntegrityError:
        messagebox.showerror("ERROR!","El interno: " + str(interno.get()) + " ya existe")

def consultadb():
    try:
        consulta = []
        con = conectadb()
        dato = [str(interno.get())]
        cursor = con.cursor()
        sql = "SELECT * FROM PALERMO WHERE interno=?" 
        cursor.execute(sql,dato)
        tabla = cursor.fetchone()
        for datos in tabla:
            consulta.append(datos)
        print(consulta)
        cursor.close()
    except sqlite3.OperationalError:
        print(sqlite3.OperationalError)
    return consulta
    
def bajadb():
    cursor = conectadb()
   
    try:
        cursor = conectadb()
        
        sql = "delete from PALERMO where interno=" + str(interno.get()) 
        cursor.execute(sql)
        cursor.commit()
        print(cursor.rowcount)
        return cursor.rowcount
    except:
        cursor.close()
    finally:
        messagebox.showinfo("ELIMINANDO"," Los datos han sido eliminados " + str(interno.get()))
    
def modificadb():
    try:
        cursor = conectadb()
        sql = ("UPDATE PALERMO SET tipo, equu, ubicapatch, ssdatos, usuario VALUES (NULL,?,?,?,?) WHERE interno=") + str(interno.get())
        cursor.execute(sql,guardar())
        cursor.commit()
        cursor.close()
    except sqlite3.OperationalError:
        pass

#Fin Funciones de base de datos
#------------------------------------------------------------------------------------------------------------------------------------------

#funciones de Ejecucion
#------------------------------------------------------------------------------------------------------------------------------------------

def guardar():
    
    vinterno = interno.get()
    vtipo = tipo.get()
    vequu = equu.get()
    vpatchera = patchera.get()
    vssdatos = ssdatos.get()
    vusuario = usuario.get()
    datos = [vinterno,vtipo,vequu,vpatchera,vssdatos,vusuario]
    
    var = print(datos)
    messagebox.showinfo("Guardado"," Los datos han sido guardados")
    
    return datos

#Fin de funciones de Ejecucion
#------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------
#Funciones de ventanas

def pestaña_consulta():
    lista = consultadb()
    tipo = lista[1]

    sInterno = Label(p1, text="Interno")
    sInterno.grid(column=0, row=0, padx=0, pady=0)
    sInternoEntry = Entry(p1, textvariable=interno)
    sInternoEntry.grid(column=1 , row=0)

    sTipo = Label(p1, text="Tipo")
    sTipo.grid(column=0, row=1, padx=0, pady=0)
    sTipoEntry = Entry(p1, textvariable=(StringVar(p1,value=str(tipo.get()))), state="readonly")
    sTipoEntry.grid(column=1 , row=1)

    sEquu = Label(p1, text="Equu")
    sEquu.grid(column=0, row=2, padx=0, pady=0)
    sEquuEntry = Entry(p1, textvariable=StringVar(p1,value=str(equu.get())), state="readonly")
    sEquuEntry.grid(column=1 , row=2)

    sPatchera = Label(p1, text="Patchera")
    sPatchera.grid(column=0, row=3, padx=0, pady=0)
    sPatcheraEntry = Entry(p1, textvariable=StringVar(p1,value=str(patchera.get())), state="readonly")
    sPatcheraEntry.grid(column=1 , row=3)

    varSdDatos = Label(p1, text="Sala de datos")
    varSdDatos.grid(column=0, row=4, padx=0, pady=0)
    varSdDatosEntry = Entry(p1, textvariable=StringVar(p1,value=str(ssdatos.get())), state="readonly")
    varSdDatosEntry.grid(column=1 , row=4)
    
    susuario = Label(p1, text="Usuario")
    susuario.grid(column=0, row=5, padx=0, pady=0)
    susuarioEntry = Entry(p1, textvariable=StringVar(p1,value=str(usuario.get())), state="readonly")
    susuarioEntry.grid(column=1 , row=5)

    consulta = Button(p1, text="Consulta", command=pestaña_consulta)
    consulta.grid(column=1, row=7)

def pestaña_agrega():
    sInterno = Label(p2, text="Interno")
    sInterno.grid(column=0, row=0, padx=0, pady=0)
    sInternoEntry = Entry(p2, textvariable=interno)
    sInternoEntry.grid(column=1 , row=0)

    sTipo = Label(p2, text="Tipo")
    sTipo.grid(column=0, row=1, padx=0, pady=0)
    sTipoEntry = Entry(p2, textvariable=tipo)
    sTipoEntry.grid(column=1 , row=1)

    sEquu = Label(p2, text="Equu")
    sEquu.grid(column=0, row=2, padx=0, pady=0)
    sEquuEntry = Entry(p2, textvariable=equu)
    sEquuEntry.grid(column=1 , row=2)

    sPatchera = Label(p2, text="Patchera")
    sPatchera.grid(column=0, row=3, padx=0, pady=0)
    sPatcheraEntry = Entry(p2, textvariable=patchera)
    sPatcheraEntry.grid(column=1 , row=3)

    varSdDatos = Label(p2, text="Sala de datos")
    varSdDatos.grid(column=0, row=4, padx=0, pady=0)
    varSdDatosEntry = Entry(p2, textvariable=ssdatos)
    varSdDatosEntry.grid(column=1 , row=4)

    vusuario = Label(p2, text="Usuario")
    vusuario.grid(column=0, row=5, padx=0, pady=0)
    vusuarioEntry = Entry(p2, textvariable=usuario)
    vusuarioEntry.grid(column=1 , row=5)

    agregar = Button(p2, text="Agregar", command=altadb)
    agregar.grid(column=0, row=7)
  
def pestaña_modifica():
    sInterno = Label(p3, text="Interno")
    sInterno.grid(column=0, row=0, padx=0, pady=0)
    sInternoEntry = Entry(p3, textvariable=interno)
    sInternoEntry.grid(column=1 , row=0)

    sTipo = Label(p3, text="Tipo")
    sTipo.grid(column=0, row=1, padx=0, pady=0)
    sTipoEntry = Entry(p3, textvariable=tipo)
    sTipoEntry.grid(column=1 , row=1)

    sEquu = Label(p3, text="Equu")
    sEquu.grid(column=0, row=2, padx=0, pady=0)
    sEquuEntry = Entry(p3, textvariable=equu)
    sEquuEntry.grid(column=1 , row=2)

    sPatchera = Label(p3, text="Patchera")
    sPatchera.grid(column=0, row=3, padx=0, pady=0)
    sPatcheraEntry = Entry(p3, textvariable=patchera)
    sPatcheraEntry.grid(column=1 , row=3)

    varSdDatos = Label(p3, text="Sala de datos")
    varSdDatos.grid(column=0, row=4, padx=0, pady=0)
    varSdDatosEntry = Entry(p3, textvariable=ssdatos)
    varSdDatosEntry.grid(column=1 , row=4)

    vusuario = Label(p3, text="Usuario")
    vusuario.grid(column=0, row=5, padx=0, pady=0)
    vusuarioEntry = Entry(p3, textvariable=usuario)
    vusuarioEntry.grid(column=1 , row=5)

    consultar = Button(p3, text="Consulta", command=pestaña_consulta())
    consultar.grid(column=0, row=7)

    modificar = Button(p3, text="Modificar", command=modificadb)
    modificar.grid(column=1, row=7)

def pestaña_eliminar():
    sInterno = Label(p4, text="Interno")
    sInterno.grid(column=0, row=0, padx=0, pady=0)
    sInternoEntry = Entry(p4, textvariable=interno)
    sInternoEntry.grid(column=1 , row=0)

    eliminar = Button(p4, text="Eliminar", command=bajadb)
    eliminar.grid(column=0, row=0)

def pestaña_consultar_todos():
    tree = ttk.Treeview(p6)
    tree["columns"] = ("col1", "col2", "col3")
    tree.column("#0", width=50, minwidth=50)
    tree.column("col1", width=80, minwidth=80)
    tree.column("col2", width=80, minwidth=80)
    tree.column("col3", width=100, minwidth=100)
    return tree

#Funciones de ventanas
#------------------------------------------------------------------------------------------------------------------------------------------

#Ventana Principal
ventana = Tk()
ventana.geometry("800x210")
ventana.title("Integrador V4")
ventana.resizable(width=False, height=False)
#******************************

interno = StringVar()
tipo = StringVar()
patchera = StringVar()
equu = StringVar()
usuario = StringVar()
ssdatos = StringVar()


#Pannel de pestañas
pestaña = ttk.Notebook(ventana)
pestaña.grid(column=0, row=1)
pestaña2 = ttk.Notebook(ventana)
pestaña2.grid(column=0, row=9)
p1 = ttk.Frame(pestaña)   
p2 = ttk.Frame(pestaña)   
p3 = ttk.Frame(pestaña)
p4 = ttk.Frame(pestaña)
p5 = ttk.Frame(pestaña)
p6 = ttk.Frame(pestaña2)
pestaña.add(p1, text='Consulta')
pestaña.add(p2, text='Agregar')
pestaña.add(p3, text='Modificar')
pestaña.add(p4, text='Eliminar')
pestaña.add(p5, text='Consultar todo')
pestaña2.add(p6, text='Treeview')


#Panel de funciones
pestaña_agrega()
pestaña_modifica()
pestaña_consulta()
pestaña_eliminar()
pestaña_consultar_todos()
conectadb()

ventana.mainloop()

