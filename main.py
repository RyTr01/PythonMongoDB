from pymongo import MongoClient
import pymongo
import menu
import os
import sys

if __name__ == "__main__":
    while True:
        os.system("cls")
        print(menu.superior_menu(75))
        print(menu.superior_menu(75,4))
        print("||\tIngrese el enlace de la base de datos (URI)" + "\t"*5 + "||")
        print("||\tPor defecto: mongodb://localhost:27017/ " + "\t"*5 + "||")
        print(menu.superior_menu(75,4))
        print(menu.superior_menu(75))
        uri = input("\nURI: ")

        if uri == "":
            uri = "mongodb://localhost:27017/"
        
        os.system("cls")
        print(menu.superior_menu(100))
        print(menu.superior_menu(100,4))
        print("||\tRECORDATORIO: Ingresar como Nombre el Nombre de una DB que no existe, creará una DB con ese nombre.\t||")
        print("||\tIngrese el Nombre de la base de datos (DB)" + "\t"*8 + "||")
        print("||\tPor defecto: test" + "\t"*11 + "||")
        print(menu.superior_menu(100,4))
        print(menu.superior_menu(100))
        nombre_db = input("\nDB: ")

        if nombre_db == "":
            nombre_db = "test"
    
        try:
            cliente = MongoClient(uri)
            db = cliente[nombre_db]
    
        except Exception:
            os.system("cls")
            print(menu.superior_menu(65))
            print(menu.superior_menu(65,4))
            print("||\tError: Ha habido un problema al conectar con la base de datos\t\t||")
            print(menu.superior_menu(65,4))
            print(menu.superior_menu(65))
            sys.exit()
    
        
        menu.menu_principal(uri,db)