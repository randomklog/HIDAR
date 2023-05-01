
print("          _____                    _____                    _____                    _____                    _____")
print("         /\    \                  /\    \                  /\    \                  /\    \                  /\    \ ")
print("        /::\____\                /::\    \                /::\    \                /::\    \                /::\    \ ")
print("       /:::/    /                \:::\    \              /::::\    \              /::::\    \              /::::\    \ ")
print("      /:::/    /                  \:::\    \            /::::::\    \            /::::::\    \            /::::::\    \ ")
print("     /:::/    /                    \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \ ")
print("    /:::/____/                      \:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \ ")
print("   /::::\    \                      /::::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \ ")
print("  /::::::\    \   _____    ____    /::::::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \ ")
print(" /:::/\:::\    \ /\    \  /\   \  /:::/\:::\    \  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ ")
print("/:::/  \:::\    /::\____\/::\   \/:::/  \:::\____\/:::/____/     \:::|    |/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |")
print("\::/    \:::\  /:::/    /\:::\  /:::/    \::/    /\:::\    \     /:::|____|\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|")
print(" \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/  \:::\    \   /:::/    /  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /")
print("          \::::::/    /    \::::::/    /            \:::\    \ /:::/    /            \::::::/    /         |:::::::::/    /")
print("           \::::/    /      \::::/____/              \:::\    /:::/    /              \::::/    /          |::|\::::/    /")
print("           /:::/    /        \:::\    \               \:::\  /:::/    /               /:::/    /           |::| \::/____/")
print("          /:::/    /          \:::\    \               \:::\/:::/    /               /:::/    /            |::|  ~|")
print("         /:::/    /            \:::\    \               \::::::/    /               /:::/    /             |::|   |")
print("        /:::/    /              \:::\    \               \::::/    /               /:::/    /              \::|   |")
print("       /:::/    /                \:::\____\               \::/    /               /:::/    /               \::|   |")
print("       \::/    /                  \::/    /                \/____/                \::/    /                 \:|   |")
print("        \/____/                    \/____/                                         \/____/                   \|___|")
print("      /| ___________________")
print("O|===|* >_DEVICE_HIDAR______> VERSION CHILE")
print("      \|")
import argparse
import subprocess
import re
import socket
import os
import platform
import ctypes
import requests
from bs4 import BeautifulSoup
import webbrowser

def abrir_paginas():
    url = input("Introduzca la url: ")
    while True:
        webbrowser.open(url, new=1)

def mostrar_comandos():
    print("Los comandos disponibles son:")
    for comando in comandos.keys():
        print(comando)

def buscar_nickname():
    nickname = input("Introduzca el nickname a buscar: ")
    urls = [
        f"https://www.instagram.com/{nickname}/",
        f"https://twitter.com/{nickname}/",
        f"https://www.twitch.tv/{nickname}",
        f"https://steamcommunity.com/id/{nickname}",
    ]
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            if "This Account is Private" in soup.text:
                print(f"{nickname} en {url} es una cuenta privada")
            elif "Sorry, that page doesn’t exist!" in soup.text:
                print(f"No se encontró {nickname} en {url}")
            else:
                print(f"{nickname} encontrado en {url}")
        else:
            print(f"Error al buscar {nickname} en {url}")

def cambiar_fondo():
    ruta_imagen = "imagen.png"
    
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, ruta_imagen, 0)
    print("Fondo de pantalla cambiado con éxito")

def informacion_pc():
    print(f"Sistema Operativo: {platform.system()}")
    print(f"Nombre del nodo: {platform.node()}")
    print(f"Arquitectura de la máquina: {platform.architecture()[0]}")
    print(f"Procesador: {platform.processor()}")
    print(f"Versión de Python: {platform.python_version()}")


def Notepad_abrir():
    #nada complejo
    os.system("notepad.exe")
    print("Abierto correctamente y cerrado correctamente el note")



def buscar_ip():
    ip = input("Introduzca la dirección IP: ")
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lat_long = data.get("loc")
        if lat_long:
            url_maps = f"https://www.google.com/maps/search/?api=1&query={lat_long}"
            webbrowser.open(url_maps, new=1)
        else:
            print("No se encontró la ubicación para la IP ingresada")
    else:
        print("Error al realizar la búsqueda de la IP")

def ip_info():
    direccion = input("Introduzca la dirección IP: ")
    try:
        info = socket.gethostbyaddr(direccion)
        print("Información de la dirección IP {}: ".format(direccion))
        print("Nombre de host: ", info[0])
        print("Alias: ", info[1])
        print("Direcciones IP: ", info[2])
    except socket.herror as e:
        print("Error al buscar información de la dirección IP: ", e)

def rutchile():
 url = "https://rutchile.cl/"
 webbrowser.open(url)





comandos = {
    "rutchile": rutchile,
    "ipinfo": ip_info,
    "iplocation": buscar_ip,
    "note": Notepad_abrir,
    "pcinfo": informacion_pc,
    "fondo": cambiar_fondo,
    "url": abrir_paginas,
    "help": mostrar_comandos,
    "nickname": buscar_nickname,
    
}

while True:
    entrada_usuario = input("~~$: ")
    if entrada_usuario in comandos:
        comandos[entrada_usuario]()
    elif entrada_usuario == "exit":
        break
    else:
        print("Comando no válido")
