# Dart - Security
# Basic Tool for Cybersecurity
import sys
import os
import nmap
import socket
import json
import requests
from art import *

def run():
    welcome()
    # menu
    menu()
    try:
        opc = True
        while opc:
            res1 = input("Ingrese una opcion a ejecutar \r\n >  ")
            res1 = int(res1)
            if res1 == 1:
                get_info()
                opc = False
            elif res1 == 2:
                networking()
                opc=False
            elif res1 == 3:
                print("Saliendo del Programa")
                opc = False
                sys.exit(0)
    except ValueError as e:
        print("La opcion no esta dentro del menu seleccione otra opcion....")
        run()
    except KeyboardInterrupt as k:
        print("\r\n El programa fue detenido de manera forzada")
def welcome():
    tprint("Dart - Security", font="random-small")
    art_0=art("coffe")
    print(art_0 + "By Equinockx")
def menu():
    print('''
    ---------------------------------
    | [*] 1 > Information Gathering |
    | [*] 2 > Scan IP               |
    | [-] 3 > Salir                 |
    ---------------------------------
    ''')
def get_info():
    dom = input("Escribe el dominio: \r\n")
    info = requests.get("https://"+dom)
    # print("\n"+str(info.headers))

    dic = info.headers
    for date,key in dic.items():
        print("|",date,": ",key,"|")

    gethostby_ = socket.gethostbyname(dom)
    print("\nThe IP address of "+ dom + " is " + gethostby_+ "\n")

    info_2 = requests.get("https://ipinfo.io/"+gethostby_+"/json")
    respuesta = json.loads(info_2.text)

    # print("Location: "+respuesta["loc"])
    # print("Region: "+respuesta["region"])
    # print("City: "+ respuesta["city"])
    # print("Country: "+ respuesta["country"])
    datos = [[respuesta["loc"],respuesta["region"],respuesta["city"],respuesta["country"]]]

    detalles ='''\
    ------------------------------------------------------------------------
    |   Location        |  Region      |   City         |    Country      |
    ------------------------------------------------------------------------
    | {}                                                                   
    |-----------------------------------------------------------------------\
    '''
    details = (detalles.format("\n".join("{:<8}     {:<10}     {:>8}     {:>6}    ".format(*fila)for fila in datos)))
    print(details)
    print("\r\nSe obtubo la informacion con exito...\r\n Selecciones una nueva opcion......")
    get_info_menu()
def get_info_menu():
    
    print('''
    ----------------------------------
    | [-] 1 Escanear nuevo dominio   |
    | [-] 2 Regesar al menu          |
    | [-] 3 Salir de la herramienta  |
    ----------------------------------
    ''')
    
    opc = input("\r\n >  ")
    opc = int(opc)
    try:
        res = True
        while res:
            if opc == 1:
                networking()
                res = False
            elif opc == 2:
                run()
                res = False
            elif opc == 3 :
                print("Saliento de la Herramienta gracias por usarla.....")
                res = False
                sys.exit(0)
            else:
                print("Opcion no existente ....")
    except ValueError as v:
        print("\r\n La opcion no esta dentro del menu..saliendo de la herramienta")
    except KeyboardInterrupt as e:
        print("\r\n El progreama fue detenido de manera forzada")
        sys.exit(1)
def networking():

    target = input("Escriba la direccion IP a escanear: \r\n >  ")
    # target = str(sys.argv[1]) # 3
    ports = [21,22,80,8080,135,139,443,4444] # 4

    scanning = nmap.PortScanner() # 5

    print("\nScanning target ",target,"for ports 21,22,80,8080,135,139...\n") # 6

    for port in ports: # 7
        portscan_result = scanning.scan(target,str(port)) # 8
        print("Port: ",port," is ",portscan_result['scan'][target]['tcp'][port]['state'])
    
    print("\r\n Elija una nueva opcion: \r\n")
    networking_menu()
def networking_menu():
    
    print('''
    ----------------------------------
    | [-] 1 Escanear una IP nueva    |
    | [-] 2 Regesar al menu          |
    | [-] 3 Salir de la herramienta  |
    ----------------------------------
    ''')
    opc = input("\r\n >  ")
    opc = int(opc)
    try:
        res = True
        while res:
            if opc == 1:
                networking()
                res = False
            elif opc == 2:
                run()
                res = False
            elif opc == 3 :
                print("Saliento de la Herramienta gracias por usarla.....")
                res = False
                sys.exit(0)
            else:
                print("Opcion no existente ....")
    except ValueError as v:
        print("\r\n La opcion no esta dentro del menu..saliendo de la herramienta...")
    except KeyboardInterrupt as e:
        print("\r\n El progreama fue detenido de manera forzada")
        sys.exit(1)

run()