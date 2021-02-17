import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from BaseSQL import * 
import BaseSQL



class integrador_Internos:
    def __init__(self):
        self.baseDatos=BaseSQL.BaseSQL()
        self.ventana1=tk.Tk()
        self.ventana1.title("Listado de Internos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_interno()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_interno(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de internos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Interno")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.labelinterno=ttk.Label(self.labelframe1, text="Interno:")
        self.labelinterno.grid(column=0, row=0, padx=4, pady=4)
        self.internocarga=tk.IntVar()
        self.entryinterno=ttk.Entry(self.labelframe1, textvariable=self.internocarga)
        self.entryinterno.grid(column=1, row=0, padx=4, pady=4)

        self.labeltipo=ttk.Label(self.labelframe1, text="Tipo:")        
        self.labeltipo.grid(column=0, row=1, padx=4, pady=4)
        self.tipocarga=tk.StringVar()
        self.entrytipo=ttk.Entry(self.labelframe1, textvariable=self.tipocarga)
        self.entrytipo.grid(column=1, row=1, padx=4, pady=4)

        self.labelpatchera=ttk.Label(self.labelframe1, text="Patchera:")
        self.labelpatchera.grid(column=0, row=2, padx=4, pady=4)
        self.patcheracarga=tk.StringVar()
        self.entrypatchera=ttk.Entry(self.labelframe1, textvariable=self.patcheracarga)
        self.entrypatchera.grid(column=1, row=2, padx=4, pady=4)

        self.ssdatos=ttk.Label(self.labelframe1, text="Sala de datos:")
        self.ssdatos.grid(column=0, row=3, padx=4, pady=4)
        self.ssdatoscarga=tk.StringVar()
        self.entrypatchera=ttk.Entry(self.labelframe1, textvariable=self.ssdatoscarga)
        self.entrypatchera.grid(column=1, row=3, padx=4, pady=4)

        self.usuario=ttk.Label(self.labelframe1, text="Usuario:")
        self.usuario.grid(column=0, row=4, padx=4, pady=4)
        self.usuariocarga=tk.StringVar()
        self.entryusuario=ttk.Entry(self.labelframe1, textvariable=self.usuariocarga)
        self.entryusuario.grid(column=1, row=4, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def agregar(self):
        datos=(self.internocarga.get(), self.tipocarga.get(), self.patcheracarga.get(), self.ssdatoscarga.get(),self.usuariocarga.get())

        mb.showinfo("Información", "Los datos fueron cargados")
        self.internocarga.set("")
        self.tipocarga.set("")
        self.patcheracarga.set("")
        self.ssdatoscarga.set("")
        self.usuariocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por Interno")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Consulta")
        self.labelframe2.grid(column=0, row=0, padx=7, pady=10)

        self.labelinterno=ttk.Label(self.labelframe2, text="Interno:")
        self.labelinterno.grid(column=0, row=0, padx=4, pady=4)
        self.interno=tk.IntVar()
        self.entryinterno=ttk.Entry(self.labelframe2, textvariable=self.interno)
        self.entryinterno.grid(column=1, row=0, padx=4, pady=4)

        self.labeltipo=ttk.Label(self.labelframe2, text="Tipo:")        
        self.labeltipo.grid(column=0, row=1, padx=4, pady=4)
        self.tipocarga=tk.StringVar()
        self.entrytipo=ttk.Entry(self.labelframe2, textvariable=self.tipocarga, state="readonly")
        self.entrytipo.grid(column=1, row=1, padx=4, pady=4)

        self.labelpatchera=ttk.Label(self.labelframe2, text="Patchera:")        
        self.labelpatchera.grid(column=0, row=2, padx=4, pady=4)
        self.patcheracarga=tk.StringVar()
        self.entrypatchera=ttk.Entry(self.labelframe2, textvariable=self.patcheracarga, state="readonly")
        self.entrypatchera.grid(column=1, row=2, padx=4, pady=4)

        self.labelsdDatos=ttk.Label(self.labelframe2, text="Sala de Datos:")        
        self.labelsdDatos.grid(column=0, row=3, padx=4, pady=4)
        self.sdDatoscarga=tk.StringVar()
        self.entrysdDatos=ttk.Entry(self.labelframe2, textvariable=self.sdDatoscarga, state="readonly")
        self.entrysdDatos.grid(column=1, row=3, padx=4, pady=4)

        self.labelusuario=ttk.Label(self.labelframe2, text="Sala de Datos:")        
        self.labelusuario.grid(column=0, row=4, padx=4, pady=4)
        self.usuariocarga=tk.StringVar()
        self.entryusuario=ttk.Entry(self.labelframe2, textvariable=self.usuariocarga, state="readonly")
        self.entryusuario.grid(column=1, row=4, padx=4, pady=4)

        self.labelsanatorio=ttk.Label(self.labelframe2, text="Sanatorio")        
        self.labelsanatorio.grid(column=0, row=5, padx=4, pady=4)
        self.sanatoriocarga=tk.StringVar()
        self.entrysanatorio=ttk.Entry(self.labelframe2, textvariable=self.sanatoriocarga, state="readonly")
        self.entrysanatorio.grid(column=1, row=5, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def consultar(self):
        datos=(self.interno.get(), )
        respuesta=self.baseDatos.consulta(datos)
        if len(respuesta)>0:
            self.tipocarga.set(respuesta[0][0])
            self.patcheracarga.set(respuesta[0][1])
            self.sssdDatoscarga.set(respuesta[0][2])
            self.usuariocarga.set(respuesta[0][3])
        else:
            self.tipocarga.set('')
            self.patcheracarga.set('')
            self.sssdDatoscarga.set('')
            self.usuariocarga.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=90, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.baseDatos.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "interno:"+str(fila[0])+
                                              "\nTipo:"+fila[1]+
                                              "\nPatchera:"+str(fila[2])+ 
                                              "\nSala de datos"+str(fila[3])+
                                              "\nUsuario"+str(fila[4])+
                                              "\nSanatorio"+str(fila[5])+
                                              "\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de internos")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Interno")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.internoBorra=tk.IntVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.internoBorra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.internoBorra.get(), )
        cantidad=self.baseDatos.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar interno")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Interno")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.labelinterno=ttk.Label(self.labelframe5, text="Interno:")
        self.labelinterno.grid(column=0, row=0, padx=4, pady=4)
        self.internomod=tk.StringVar()
        self.entryinterno=ttk.Entry(self.labelframe5, textvariable=self.internomod)
        self.entryinterno.grid(column=1, row=0, padx=4, pady=4)

        self.labeltipo=ttk.Label(self.labelframe5, text="Tipo:")        
        self.labeltipo.grid(column=0, row=1, padx=4, pady=4)
        self.tipomod=tk.StringVar()
        self.entrytipo=ttk.Entry(self.labelframe5, textvariable=self.tipomod)
        self.entrytipo.grid(column=1, row=1, padx=4, pady=4)

        self.labelpatchera=ttk.Label(self.labelframe5, text="Patchera:")        
        self.labelpatchera.grid(column=0, row=2, padx=4, pady=4)
        self.patcheramod=tk.StringVar()
        self.entrypatchera=ttk.Entry(self.labelframe5, textvariable=self.patcheramod)
        self.entrypatchera.grid(column=1, row=2, padx=4, pady=4)

        self.labelssDatos=ttk.Label(self.labelframe5, text="Sala de Datos:")        
        self.labelssDatos.grid(column=0, row=3, padx=4, pady=4)
        self.ssdatosamod=tk.StringVar()
        self.entryssdatos=ttk.Entry(self.labelframe5, textvariable=self.ssdatosamod)
        self.entryssdatos.grid(column=1, row=3, padx=4, pady=4)

        self.labelusuario=ttk.Label(self.labelframe5, text="Precio:")        
        self.labelusuario.grid(column=0, row=4, padx=4, pady=4)
        self.usuarioamod=tk.StringVar()
        self.entryusuario=ttk.Entry(self.labelframe5, textvariable=self.usuarioamod)
        self.entryusuario.grid(column=1, row=4, padx=4, pady=4)


        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=0, row=5, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def modifica(self):
        datos=(self.tipomod.get(), self.patcheramod.get(), self.internomod.get(), self.ssdatos.get(), self.usuarioamod.get())
        cantidad=self.baseDatos.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        datos=(self.internomod.get(), )
        respuesta=self.baseDatos.consulta(datos)
        if len(respuesta)>0:
            self.tipomod.set(respuesta[0][0])
            self.patcheramod.set(respuesta[0][1])
            self.ssdatosamod.set(respuesta[0][2])
            self.usuarioamod.set(respuesta[0][3])
        else:
            self.tipomod.set('')
            self.patcheramod.set('')
            self.ssdatosamod.set('')
            self.usuarioamod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

            


app=integrador_Internos()