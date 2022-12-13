from tkinter import *
from tkinter import messagebox as mb 
from tkinter import ttk

class VentanaMovimientos:
    def __init__(self,usuario):
        self.usuarioAbierto = usuario 

        self.ventanaMovi = Toplevel()

        self.ventanaMovi.title("Movimientos")

        self.cuaderno = ttk.Notebook(self.ventanaMovi)
        self.paginaExtracciones()
        self.paginaDepositos()

        self.cuaderno.pack()        
        self.ventanaMovi.mainloop()

    def paginaExtracciones(self):
        self.pagEx = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagEx,text="Extracciones")

        self.labelMonto = Label(self.pagEx,text="Indica el monto a extraer").pack()

        self.datoMontoEx = IntVar()
        self.entryEx = Entry(self.pagEx,textvariable=self.datoMontoEx).pack()

        self.botonEx = Button(self.pagEx,text="Extraer").pack()
        
    def paginaDepositos(self):
        self.pagDep = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagDep,text="Depositos")

        self.labelMonto1 = Label(self.pagDep,text="Indica el monto a depositar").pack()

        self.datoMontoDep = IntVar()
        self.entryDep = Entry(self.pagDep,textvariable=self.datoMontoDep).pack()

        self.botonDep = Button(self.pagDep,text="Depositar").pack()


