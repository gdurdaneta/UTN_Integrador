import sqlite3
from IntegradorV4 import *

def conectadb():
    try:
        con = sqlite3.connect("database2.db")
        con.text_factory=str
        cursor = con.cursor()
        cursor.execute("CREATE TABLE PALERMO(interno VARCHAR(20), tipo VARCHAR(20), equu VARCHAR(20), ubicapatch VARCHAR(20), ssdatos VARCHAR(20), usuario VARCHAR(20))")
    except sqlite3.OperationalError:
        pass
    finally:
        return con

# def creaddb():
    try:
        cursor = conectadb()
        cursor.execute("CREATE TABLE PALERMO(interno VARCHAR(20), tipo VARCHAR(20), equu VARCHAR(20), ubicapatch VARCHAR(20), ssdatos VARCHAR(20), usuario VARCHAR(20))")
    except sqlite3.OperationalError:
        pass    

def altadb():
    cursor = conectadb()
    sql = "insert into PALERMO (interno, tipo, equu, ubicapatch, ssdatos, usuario) values (?,?,?,?,?,?)"
    alta = cursor.execute(sql,guardar())
    cursor.commit()
    cursor.close()
    
def consultadb():

    try:
        con = conectadb()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM PALERMO where interno=?")
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