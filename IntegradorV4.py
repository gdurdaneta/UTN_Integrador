from os import curdir
import tkinter
from tkinter import LabelFrame, Tk, messagebox
import sqlite3

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Integrador V4")

def conectadb():
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE PALERMO (interno INTEGER(20),
        equu VARCHAR(20), ubicapatch VARCHAR(40), sddatos VARCHAR(40), 
        usuario VARCHAR(20)""")
    except sqlite3.OperationalError:
        pass
    finally:
        return cursor

def altadb():
    cursor = conectadb()
    cursor.execute("""INSERT INTO PALERMO('interno, equu, ubicapatch,
    ssdatos, usuario
    ') VALUES (?,?,?,?,?)""")
    cursor.commit()
    cursor.close()
    
def consultadb():
    try:
        cursor = conectadb()
        cursor.execute("SELECT equu, ubicapatch, ssdatos, usuario FROM PALERMO where interno=?")
        cursor.fetchall()
        cursor.close()
    finally:
        return cursor.fetchall()
    
def bajadb():
    try: 
        cursor = conectadb()
        cursor.execute("DELETE equu, ubicapatch, ssdatos, usuario FROM PALERMO where interno=?")
        cursor.commit()
        cursor.close()
    finally:
        return cursor.fetchall()
    
def modificadb():
    cursor = conectadb()
    cursor.execute("UPDATE PALERMO SET equu, ubicapatch, ssdatos, usuario VALUES(?,?,?,?)")    
    cursor.commit()
    cursor.close()

def ventana():





conectadb()
















ventana.mainloop()