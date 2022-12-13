import random
from tkinter import messagebox as mb

class CuentaBancaria:
    def __init__(self, name, dni, lastName):
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.saldo = 0
        self.numeroDeCta = random.randrange(10000, 15000)

class CuentaCorriente (CuentaBancaria):
    def __init__(self, namecc, dnicc, lastNamecc):
        CuentaBancaria.__init__(self, namecc, dnicc, lastNamecc)

    def depositar(self, monto):
        if (monto <= 20000 and monto != 0):
            self.saldo += monto
            mb.showinfo( f"Deposito realizado con exito, tu salgo actual es: {self.saldo}")
        else:
            mb.showinfo ("ERROR", "Por favor, ingrese un monto entre $1,00 y $20.000")
        
    def extraccion (self, monto):
        if monto <= self.saldo and (monto <= 50000 and monto != 0):
            self.saldo -= monto
            mb.showinfo("BANCO-CAMI", f"Extracción realizada con exito, tu salgo actual es: {self.saldo}")
        elif (monto >= self.saldo):
            mb.showinfo ("ERROR - BANCO-CAMI", f"Fondos insuficientes, su saldo actual es: {self.saldo}")
        else:
            mb.showinfo ("ERROR - BANCO-CAMI", "Limite de extraccion $50.000. Ingrese un monto valido.")

class CajaDeAhorros (CuentaBancaria):
    def __init__(self, nameca, dnica, lastNameca):
        CuentaBancaria.__init__(self, nameca, dnica, lastNameca)

    def depositar(self, monto):
        if (monto >= 5000):
            self.saldo += monto
            mb.showinfo( f"Deposito realizado con exito, tu salgo actual es: {self.saldo}")
        else:
            mb.showinfo ("ERROR", "Por favor, ingrese un monto mayor a $5.000")
        
    def extraccion (self, monto):
        if (monto <= self.saldo and monto != 0):
            self.saldo -= monto
            mb.showinfo("BANCO-CAMI", f"Extracción realizada con exito, tu salgo actual es: {self.saldo}")
        elif (monto >= self.saldo):
            mb.showinfo ("ERROR - BANCO-CAMI", f"Fondos insuficientes, su saldo actual es: {self.saldo}")
        else:
            mb.showinfo ("ERROR - BANCO-CAMI", "Ingrese un monto mayor a 0")