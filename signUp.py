from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from cuentasBancarias import *
from movimientos import *

colorFrame2= "#D8BFD8"
colorFondo = "#E6E6FA"
colorLetra = "#BC8F8F"
usuarios = []

class VentanaRegistro:
    def __init__(self):
        self.ventanaRegistro = Toplevel()
        self.ventanaRegistro.title("Sign Up - BANCO CAMI")
        self.ventanaRegistro.resizable (width=FALSE, height=FALSE)
        
        self.ventanaRegistro.config(bg=colorFondo)

        self.labelBienvenida = Label(self.ventanaRegistro, text="SignUp • Bienvenidx!", fg = colorLetra, bg= colorFondo, font= ("", 12, "bold"))
        self.labelBienvenida.pack(pady=5)

        self.frame1 = Frame (self.ventanaRegistro, bg= colorFrame2)
        self.frame1.pack(padx=20, pady=20)
        self.frame2 = LabelFrame (self.frame1, text= "Complete los datos para registrarse", bg= colorFrame2, border= 5)
        self.frame2.grid(row=1 , column=0, padx=20, pady=20)

        #NOMBRE
        self.labelName = Label(self.frame2, text="Nombre: ", bg= colorFrame2)
        self.labelName.grid(row=2 ,column=0)
        self.newUserName = StringVar()
        self.entryName = Entry(self.frame2, textvariable=self.newUserName)
        self.entryName.grid(row=2 , column=1)

        #APELLIDO
        self.labelLastName = Label(self.frame2, text="Apellido: ", bg= colorFrame2)
        self.labelLastName.grid(row=2 ,column=2)
        self.newUserLastName = StringVar()
        self.entryLastName = Entry(self.frame2, textvariable=self.newUserLastName)
        self.entryLastName.grid(row=2 , column=3)

    
        #DNI
        self.labelDni = Label(self.frame2, text="D.N.I (solo números): ", bg= colorFrame2)
        self.labelDni.grid(row=3 ,column=0)
        self.newUserDni = IntVar()
        self.entryDni = Entry(self.frame2, textvariable=self.newUserDni)
        self.entryDni.grid(row=3 , column=1)

        #TIPO DE CTA.
        self.labelTipoCc = Label(self.frame2, text="Tipo de cuenta: ", bg= colorFrame2)
        self.labelTipoCc.grid(row=3 ,column=2)
        self.newUserTipoCc = ttk.Combobox(self.frame2, values= ["seleccione", "cuenta corriente", "caja de ahorros"])
        self.newUserTipoCc.grid(row=3 ,column=3)
        self.newUserTipoCc.set("seleccione")

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=5, pady=8)

        self.botonRegistro = Button (self.ventanaRegistro, text="Registrar", bg= colorFrame2, command= self.registro)
        self.botonRegistro.pack(side=LEFT, expand= TRUE, padx=10, pady=10, fill= "both")

        self.botonCancel = Button (self.ventanaRegistro, text="Cancelar", bg= colorFrame2, command= self.ventanaRegistro.destroy)
        self.botonCancel.pack(side=RIGHT, expand= TRUE, padx=10, pady=10, fill= "both")

        self.ventanaRegistro.mainloop()

    def registro(self):
        try:
            match self.newUserTipoCc.get():
                case "cuenta corriente":
                    nuevo_usuario = CuentaCorriente(self.newUserName.get(), self.newUserDni.get(), self.newUserLastName.get())
                case "caja de ahorros":
                    nuevo_usuario = CajaDeAhorros(self.newUserName.get(), self.newUserDni.get(), self.newUserLastName.get())
                case "":
                    mb.showerror("ERROR - BANCO CAMI", "Todos los datos deben estar completos")
        except TclError:
            mb.showerror("ERROR - BANCO CAMI", "Ingrese un dato válido según corresponda")
        if nuevo_usuario != any:
            usuarios.append ([self.newUserName.get(), self.newUserDni.get()])
            print(usuarios)
            VentanaMovimientos(nuevo_usuario)



#app = VentanaRegistro()

