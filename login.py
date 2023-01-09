# VENTANA PRINCIPAL - LOGIN

from tkinter import *
import signUp as sU
import movimientos as mov
from cuentasBancarias import CuentaBancaria as Cb
from signUp import usuarios as userList
from tkinter import messagebox as mb

colorFrame2 = "#D8BFD8"
colorFondo = "#E6E6FA"
colorLetra = "#BC8F8F"


class VentanaLogin:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Login - BANCO CAMI")
        self.ventana.config(bg=colorFondo)
        self.ventana.resizable(width=FALSE, height=FALSE)

        self.bienvenida = Label(self.ventana, text="BIENVENIDx", font=("", 16, "bold"), fg=colorLetra, bg=colorFondo)
        self.bienvenida.pack(pady=5)

        self.frame1 = Frame(self.ventana, bg=colorFrame2)
        self.frame1.pack()
        self.bienvenida2 = LabelFrame(self.frame1, text="Ingrese los datos solicitados para iniciar sesion", bg=colorFrame2, border=5)
        self.bienvenida2.grid(row=2, column=0, padx=20, pady=20)

        # NOMBRE
        self.userName = Label(self.bienvenida2, text="Nombre: ", bg=colorFrame2)
        self.userName.grid(row=2, column=0)
        self.newUserName = StringVar()
        self.entryName = Entry(self.bienvenida2, textvariable=self.newUserName)
        self.entryName.grid(row=2, column=1)

        #APELLIDO
        self.LastName = Label(self.bienvenida2, text="Apellido: ", bg= colorFrame2)
        self.LastName.grid(row=3 ,column=0)
        self.newUserLastName = StringVar()
        self.entryLastName = Entry(self.bienvenida2, textvariable=self.newUserLastName)
        self.entryLastName.grid(row=3 , column=1)

        # DNI
        self.userDni = Label(self.bienvenida2, text="D.N.I (solo números): ", bg=colorFrame2)
        self.userDni.grid(row=4, column=0)
        self.newUserDni = IntVar()
        self.entryDni = Entry(self.bienvenida2, textvariable=self.newUserDni)
        self.entryDni.grid(row=4, column=1)

        # ORDENAMIENTO
        for widget in self.bienvenida2.winfo_children():
         widget.grid_configure(padx=5, pady=8)

        # BOTONES
        self.botonRegistro = Button(self.ventana, text="Registrarse", bg=colorFrame2, command= sU.VentanaRegistro)
        self.botonRegistro.pack(side=LEFT, expand=TRUE, padx=10, pady=10, fill="both")

        self.botonInvitado = Button(self.ventana, text="Ingresar", bg=colorFrame2, command= self.ingreso)
        self.botonInvitado.pack(side=RIGHT, expand=TRUE, padx=10, pady=10, fill="both")

        self.botonExit = Button(self.ventana, text="Salir", bg=colorFrame2, command=self.ventana.destroy)
        self.botonExit.pack(side=RIGHT, expand=TRUE, padx=10, pady=10, fill="both")

        self.ventana.mainloop()

    def ingreso (self):
        print (userList)
        for user in userList:
            if self.newUserDni.get() == user[1]:
                usuario = Cb(self.newUserName.get(), self.newUserDni.get(), self.newUserLastName.get())   
                mov.VentanaMovimientos(usuario)
            # else:
            #     mb.showerror("ERROR - BANCO CAMI", "Credenciales inexistentes. Por favor, registrese para ingresar")
                
                    

        
