from pymongo import MongoClient
import pymongo
import menu
import os
import sys
import decoracionMenu

if __name__ == "__main__":
    while True:
        os.system("cls")
        print(decoracionMenu.superior_menu(100))
        print(decoracionMenu.superior_menu(100,4))
        decoracionMenu.texto("Ingrese el enlace de la base de datos (URI)", 100)
        decoracionMenu.texto("Por defecto: mongodb://localhost:27017/ ")
        print(decoracionMenu.superior_menu(100,4))
        print(decoracionMenu.superior_menu(100))
        uri = input("\nURI: ")

        if uri == "":
            uri = "mongodb://localhost:27017/"
        
        os.system("cls")
        print(decoracionMenu.superior_menu(100))
        print(decoracionMenu.superior_menu(100,4))
        decoracionMenu.texto("Ingrese el Nombre de la base de datos (DB)",100)
        decoracionMenu.texto("RECORDATORIO: Ingresar como Nombre el Nombre de una DB que no existe, creará una DB con ese nombre.",100)
        decoracionMenu.texto("Por defecto: test",100)
        print(decoracionMenu.superior_menu(100,4))
        print(decoracionMenu.superior_menu(100))
        nombre_db = input("\nDB: ")

        if nombre_db == "":
            nombre_db = "test"
    
        try:
            cliente = MongoClient(uri, serverSelectionTimeoutMS=2500)
            cliente.admin.command("ping")
            db = cliente[nombre_db]
    
        except Exception:
            os.system("cls")
            print(decoracionMenu.superior_menu(100))
            print(decoracionMenu.superior_menu(100,4))
            decoracionMenu.texto("Error: Ha habido un problema al conectar con la base de datos")
            print(decoracionMenu.superior_menu(100,4))
            print(decoracionMenu.superior_menu(100))
            input("\nPresione Enter para continuar...")
            sys.exit()
    
        
        menu.menu_principal(uri,db)