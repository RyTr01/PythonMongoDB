from pymongo import MongoClient
import pymongo
import menu
import os

if __name__ == "__main__":
    os.system("cls")
    menu.superior_menu(75)
    uri = input("||\tIngrese el enlace de la base de datos (URI): ")
    
    os.system("cls")
    menu.superior_menu(100)
    print("||\tRECORDATORIO: Ingresar como Nombre el Nombre de una DB que no existe, creará una DB con ese nombre.\t||")
    nombre_db = input("||\tIngrese el Nombre de la base de datos (DB): ")
    
    os.system("cls")
    menu.superior_menu(125)
    print("||\tRECORDATORIO: Ingresar como Nombre el Nombre de una Colección que no existe, creará una Colección con ese nombre.\t\t||")
    nombre_coleccion = input("||\tIngrese el Nombre de la colección (Colección): ")

    try:
        cliente = MongoClient(uri)
        db = cliente[nombre_db]
        coleccion = db[nombre_coleccion]

    except Exception:
        os.system("cls")
        menu.superior_menu(65)
        print("||\tError: Ha habido un problema al conectar con la base de datos\t\t||")