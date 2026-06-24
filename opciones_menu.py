from pymongo import MongoClient
import os
from decoracionMenu import superior_menu

def listadoEventos(uri,db,col):
    os.system("cls")
    print(superior_menu(25,1) + " Listado de Eventos " + superior_menu(25,2))
    documentos = col.find({},{'codigo':1,'nombre':1,'fecha':1,'lugar':1,'categoria':1})

    if col.count_documents({})==0:
        print(f"No se encontraron registros en la colección '{col.name}")
    else:
        for doc in documentos:
            print("Código: \t" + doc["codigo"])
            print("Nombre: \t" + doc["nombre"])
            print("Fecha: \t\t" + doc["fecha"])
            print("Lugar: \t\t" + doc["lugar"])
            print("Categoría: \t" + doc["categoria"])
            print("=="*40)
    
    input("\nPresione Enter para volver...")
    return

def listadoInvitados(uri,db,col):
    os.system("cls")
    
    print(superior_menu(75))
    print(superior_menu(75,4))
    print("||\tIngrese la primera letra del nombre del invitado que busca" + "\t"*3 + "||")
    print(superior_menu(75,4))
    print(superior_menu(75))
    letra = input("\nLetra: ")
    
    documentos = col.find({'nombre': {'$regex': f'^{letra}', '$options': 'i'}})

    os.system("cls")
    print(superior_menu(25,1) + " Listado de Invitados " + superior_menu(25,2))
    if col.count_documents({})==0:
        print(f"No se encontraron registros en la colección '{col.name}")
    else:
        for doc in documentos:
            print("Rut: \t\t" + doc["rut"])
            print("Nombre: \t" + doc["nombre"])
            print("Correo: \t" + doc["correo"])
            print("Empresa: \t" + doc["empresa"])
            print("Estado: \t" + doc["estado"])
            print("=="*40)
    
    input("\nPresione Enter para volver...")
    return

def validacionAcceso(uri,db,col):
    os.system("cls")

    print(superior_menu(75))
    print(superior_menu(75,4))
    print("||\tIngrese el rut del invitado a comprobar" + "\t"*5 + "||")
    print(superior_menu(75,4))
    print(superior_menu(75))
    rut = input("\nRut: ")


