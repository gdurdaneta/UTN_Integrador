import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor
from pathlib import Path

class BaseSQL():


    def abrir(self):
        try:
            con=sqlite3.connect("database.db")
            con.execute("CREATE TABLE PALERMO(vInterno INTERGER(20), vTipo VARCHAR(20), vPatchera VARCHAR(20), vssDatos VARCHAR(20), vUsuario VARCHAR(20), vSanatorio VARCHAR(20))")
        except sqlite3.OperationalError:
            pass
        finally:
            return con

    def alta(self, datos):
        con=self.abrir()
        cursor=con.cursor()
        sql="insert into PALERMO (vInterno, vTipo, vPatchera, vssDatos, vUsuario, vSanatorio) }values (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close

    def consulta(self, datos):
        try:
            con=self.abrir()
            cursor=con.cursor()
            sql="select vTipo,vPatchera,vssDatos,vUsuario,vSanatorio from PALERMO where vInterno=?"
            cursor.execute(sql,datos)
            return cursor.fetchall
        finally:
            con.close

    
    def recuperar(self):
        try:
            con=self.abrir()
            cursor=con.cursor()
            sql="select vInterno, vTipo, vPatchera, vssDatos, vUsuario, vSanatorio from PALERMO"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            con.close()

    def baja(self, datos):
        try:
            con=self.abrir()
            cursor=con.cursor()
            sql="dele from PALERMO where vInterno=?"
            cursor.execute(sql,datos)
            con.commit()
            #Retorna las filas borradas
            return cursor.rowcount
        except:
            con.close()

    def modificaciones(self, datos):
        try:
            con=self.abrir()
            cursor=con.cursor()
            sql="update PALERMO set vTipo=?, vPatchera=?, vssDatos=?, vUsuario=?, vSanatorio=? where vInterno=?"
            cursor.execute(sql,datos)
            con.commit()
            return cursor.rowcount
        except:
            con.close()
    #connection()
    


