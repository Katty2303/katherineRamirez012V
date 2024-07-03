import os
import time
import random
import csv

pedidos = {}

def limpiaPantalla():
    os.system("cls")
    
def tiempo():
    time.sleep(2)

def opcionesSacos():
    limpiaPantalla()
    print("*"*10, "OPCIONES DE SACOS", "*"*10)
    print("1. 5 kilos")
    print("2. 10 kilos")
    print("3. 20 kilos")
    
def menu():
    limpiaPantalla()
    print("*"*10, "MENÙ CAT PREMIUN", "*"*10)
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")


def registro():
    limpiaPantalla()
    sacosDisponibles = {}   
    print("*"*10, "REGISTRAR PEDIDO", "*"*10)
    print("\nIngrese los siguiente datos")
    try:
        nombre = input("\nnombre: ")
        apellido = input("apellido: ")
        comuna = input("comuna: ")
        direccion = input("direcciòn: ")
        opcionesSacos()
        cinco = 0
        diez = 0
        veinte = 0
        saco = int(input("\nIngrese la opciòn de saco: "))
        cantidad = int(input(f"Ingrese la cantidad: "))
        if saco == 1:
            cinco = cantidad
        elif saco == 2:
            diez = cantidad
        else:
            veinte = cantidad
        numeroPedido = random.randint(1,1000)
        numeroPedido += 1
        pedidos["Nro. Pedido"] = numeroPedido
        pedidos["Cliente"] = nombre + " " + apellido
        pedidos["Direcciòn"] = direccion
        pedidos["Comuna"] = comuna
        pedidos["Saco 5kg"] = cinco
        pedidos["Saco 10kg"] = diez
        pedidos["Saco 20kg"] = veinte
    except ValueError:
        print("El valor ingresado no es correcto")
        tiempo()

def listarPedidos():
    limpiaPantalla()
    print("*"*10, "LISTA DE PEDIDOS", "*"*10)
    print("\nNro. Pedido", " "*5, "Cliente", " "*7, "Direcciòn", " "*5, "Comuna", " "*10, "Saco 5kg", " "*10, "Saco 10kg", " "*5, "Saco 20kg\n")
    print("-"*112)
    print(pedidos["Nro. Pedido"]," "*8, pedidos["Cliente"]," "*5, pedidos["Direcciòn"]," "*5, pedidos["Comuna"]," "*10, pedidos["Saco 5kg"]," "*15, pedidos["Saco 10kg"]," "*15, pedidos["Saco 20kg"])
    tiempo()

def imprimir():
    limpiaPantalla()
    print("*"*10, "IMPRESIÒN DE HOJA DE RUTA", "*"*10)
    rutas = ["San Bernardo", "Calera de Tango", "Buin"]
    print(f"\nLas rutas disponibles son: ")
    for i,j in enumerate(rutas, start=1):
        print(f"{i}.",j)
    sector = input("\nIngrese el nombre del sector: ")
    pedidos["Sector"] = sector

def salir():
    limpiaPantalla()
    nuevaKeys = list(pedidos.keys())
    nuevaValues = list(pedidos.values())
    with open("rutas.csv", "w", newline=" ") as rutasCsv:
            escrito_csv = csv.writer(rutasCsv)
            escrito_csv.writerow(nuevaKeys)
            escrito_csv.writerows([nuevaValues])
    print("Usted està saliendo del programa, gracias por preferir CatPremiun...")
    tiempo()

def opcionesMenu():
    opcion = True
    opElegida = 0
    while opcion == True:
        menu()
        try:
            opElegida = int(input("\nIngrese la opciòn del menù: "))
            if opElegida == 1:
                registro()
            elif opElegida == 2:
                listarPedidos()
            elif opElegida == 3:
                imprimir()
            elif opElegida == 4:
                salir()
                break
            else:
                print("La opciòn elegida no es correcta, vuelva a intentar")
                tiempo()
        except ValueError:
            print("El valor ingresado no es correcto, vuelva a intentar")
            tiempo()

opcionesMenu()
