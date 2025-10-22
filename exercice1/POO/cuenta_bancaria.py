import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def imprimir(self):
        print(f"{self.nombre} {self.apellido} | Cuenta: {self.numero_cuenta} | Balance: {self.balance:.2f}€")
    def retirar(self,valor):
        if valor > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= valor
            print(f"Has retirado {valor:.2f}€. Nuevo balance: {self.balance:.2f}€")
            self.imprimir()

    def depositar(self,valor):
        self.balance += valor
        print(f"Has depositado {valor:.2f}€. Nuevo balance: {self.balance:.2f}€")
        self.imprimir()




clientes=[]
while True:
    opcion = input("""
    Que quieres hacer?
    1 - Crear cliente
    2 - Depositar
    3 - Retirar
    4 - Salir
    """)
    if opcion == "1":
        os.system("cls")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        numero_cuenta = input("Número de cuenta: ")
        balance = float(input("Balance inicial: "))
        cliente = Cliente(nombre, apellido, numero_cuenta, balance)
        clientes.append(cliente)
        print("Cliente creado correctamente.")

    elif opcion == "2":
        for index,cliente in enumerate(clientes):
            print(f" {index} : {cliente.nombre}, {cliente.apellido}")
        client_val = input("que cliente eres")
        os.system("cls")
        print(clientes[int(client_val)].imprimir())
        deposito = input("Quanto quieres depositar? ")
        clientes[int(client_val)].depositar(float(deposito))
    elif opcion == "3":
        for index, cliente in enumerate(clientes):
            print(f" {index} : {cliente.nombre}, {cliente.apellido}")
        client_val = input("que cliente eres")
        os.system("cls")
        print(clientes[int(client_val)].imprimir())
        retirar = input("Quanto quieres retirar? ")
        clientes[int(client_val)].depositar(float(retirar))
    else:
        break
