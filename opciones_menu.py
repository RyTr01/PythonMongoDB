from pymongo import MongoClient
import os
import sys
from decoracionMenu import superior_menu
import decoracionMenu

def listadoEventos(uri,db,col):
    os.system("cls")
    decoracionMenu.texto("="*40 + " Listado de Eventos " + "="*40)
    documentos = col.find({},{'codigo':1,'nombre':1,'fecha':1,'lugar':1,'categoria':1})

    if col.count_documents({})==0:
        decoracionMenu.texto(f"No se encontraron registros en la colección '{col.name}'.")
        decoracionMenu.texto("="*100)
    else:
        for doc in documentos:
            decoracionMenu.texto(" Código: " + f"     {doc['codigo']}", 100, "izq")
            decoracionMenu.texto(" Nombre: " + f"     {doc['nombre']}", 100, "izq")
            decoracionMenu.texto(" Fecha: " + f"      {doc['fecha']}", 100, "izq")
            decoracionMenu.texto(" Lugar: " + f"      {doc['lugar']}", 100, "izq")
            decoracionMenu.texto(" Categoría: " + f"  {doc['categoria']}", 100, "izq")
            decoracionMenu.texto("="*100, 100, "izq")
    
    input("\nPresione Enter para volver...")
    return

def listadoEventosCategoria(uri,db,col):
    os.system("cls")
    
    decoracionMenu.texto("="*100)
    decoracionMenu.texto("Ingrese la categoría del evento que busca")
    decoracionMenu.texto("En caso de no tener la categoría, dejarlo en blanco y mostrará todos los eventos")
    decoracionMenu.texto("="*100)

    categoria = input("\nCategoría: ")
    os.system("cls")

    decoracionMenu.texto("=" * 40 + " Listado de Eventos " + "=" * 40)

    if categoria != "":
        documentos = col.find({'categoria': {'$regex': f"{categoria}", '$options': 'i'}},{'codigo':1,'nombre':1,'fecha':1,'lugar':1,'categoria':1})

    else:
        documentos = col.find({},{'codigo':1,'nombre':1,'fecha':1,'lugar':1,'categoria':1})
        
    if col.count_documents({})==0:
        decoracionMenu.texto(f"No se encontraron registros en la colección '{col.name}'.")
        decoracionMenu.texto("="*100)
    else:
        for doc in documentos:
            decoracionMenu.texto("Código: " + f"     {doc['codigo']}", 100, "izq")
            decoracionMenu.texto("Nombre: " + f"     {doc['nombre']}", 100, "izq")
            decoracionMenu.texto("Fecha: " + f"      {doc['fecha']}", 100, "izq")
            decoracionMenu.texto("Lugar: " + f"      {doc['lugar']}", 100, "izq")
            decoracionMenu.texto("Categoría: " + f"  {doc['categoria']}", 100, "izq")
            decoracionMenu.texto("="*100)

    
    input("\nPresione Enter para volver...")
    return

def listadoInvitados(uri,db,col):
    os.system("cls")
    
    decoracionMenu.texto("="*100)
    decoracionMenu.texto("Ingrese el nombre o parte de nombre del invitado que busca")
    decoracionMenu.texto("="*100)
    letra = input("\nLetra: ")
    
    documentos = col.find({'nombre': {'$regex': f'{letra}', '$options': 'i'}})

    os.system("cls")
    decoracionMenu.texto("=" * 39+ " Listado de Invitados " + "=" * 39,100)
    if col.count_documents({})==0:
        decoracionMenu.texto(f"No se encontraron registros en la colección '{col.name}'.")
        decoracionMenu.texto("="*100)
    else:
        for doc in documentos:
            decoracionMenu.texto("Rut: " + f"       {doc['rut']}", 100, "izq")
            decoracionMenu.texto("Nombre: " + f"    {doc['nombre']}", 100, "izq")
            decoracionMenu.texto("Correo: " + f"    {doc['correo']}", 100, "izq")
            decoracionMenu.texto("Empresa: " + f"   {doc['empresa']}", 100, "izq")
            decoracionMenu.texto("Estado: " + f"    {doc['estado']}", 100, "izq")
            decoracionMenu.texto("="*100)
    
    input("\nPresione Enter para volver...")
    return

def validarAcceso(uri,db,col):
    os.system("cls")
    decoracionMenu.texto("="*100)
    decoracionMenu.texto("Ingrese el correo del invitado: ")
    decoracionMenu.texto("="*100)
    correo = input("Correo: ")


    os.system("cls")
    decoracionMenu.texto("="*100)
    decoracionMenu.texto("Ingrese el código del evento a revisar: ")
    decoracionMenu.texto("="*100)
    evento = input("Código: ")

    pipeline = [
        {"$match": {"codigo": evento}},
        {"$unwind": "$invitados"},
        {"$lookup": {
            "from": "invitados",
            "localField": "invitados.rut",
            "foreignField": "rut",
            "as": "infoInvitado"
        }},
        {"$unwind": "$infoInvitado"},
        {"$match": {"infoInvitado.correo": correo}},
        {"$project": {"_id": 0, "estadoInvitado": "$infoInvitado.estado", "estadoEvento": "$invitados.estado"}}
        ]
    
    resultado = list(col.aggregate(pipeline))

    if not resultado:
        os.system("cls")
        decoracionMenu.texto("="*100)
        decoracionMenu.texto("Error: El correo no está registrado en este evento, o el evento no existe.")
        decoracionMenu.texto("="*100)
        input("Presione Enter para continuar...")
        return
    
    estadoInvitado = resultado[0]["estadoInvitado"]
    estadoEvento = resultado[0]["estadoEvento"]
    os.system("cls")
    
    decoracionMenu.texto("="*100)
    decoracionMenu.texto(f"Estado invitado (global): {estadoInvitado}")
    decoracionMenu.texto(f"Estado invitado en evento {evento}: {estadoEvento}")
    decoracionMenu.texto("="*100)
    input("Presione Enter para continuar...")
    return


def invitadosCorreo(uri,db,col):
    os.system("cls")

    decoracionMenu.texto("="*100)
    decoracionMenu.texto("Ingrese el Correo de invitado a buscar: ")
    decoracionMenu.texto("Ejemplo: @inacap.cl")
    decoracionMenu.texto("="*100)

    correo = input("correo: ")
    os.system("cls")

    decoracionMenu.texto("="*39 + " Busqueda por correos " + "="*39)

    if correo == "":
        decoracionMenu.texto("Error: Correo no válido")
        decoracionMenu.texto("="*100)
        input("Presione Enter para continuar...")
        return

    filtro = {"correo": {"$regex": correo, "$options": "i"}}

    if col.count_documents(filtro) == 0:
        decoracionMenu.texto(f"No se encontró registros que coincidan con '{correo}'.")
        decoracionMenu.texto("="*100)
        input("Presione Enter para continuar...")
        return
    
    documentos = col.find(filtro)
    
    for doc in documentos:
        decoracionMenu.texto("Rut: " + f"       {doc.get('rut')}", 100, "izq")
        decoracionMenu.texto("Correo: " + f"    {doc.get('correo')}", 100, "izq")
        decoracionMenu.texto("Estado: " + f"    {doc.get('estado')}", 100, "izq")
        decoracionMenu.texto("="*100)
    sys.stdin.flush()
    input("\nPresione Enter para volver...")

def topEventos(uri,db,col):
    os.system("cls")
    decoracionMenu.texto("="*28 + " Top 3 eventos con más personas confirmadas " + "="*28)

    pipeline = [
        {"$unwind": "$invitados"},
        {"$match": {"invitados.estado": "confirmado"}},
        {"$group": {
            "_id": {"codigo": "$codigo", "nombre": "$nombre"},
            "totalConfirmados": {"$sum": 1}
        }},
        {"$sort": {"totalConfirmados": -1}},
        {"$limit": 3}
    ]

    resultado = list(col.aggregate(pipeline))

    if not resultado:
        decoracionMenu.texto("No se encontraron eventos con invitados confirmados.")
        decoracionMenu.texto("="*100)
        input("Presione Enter para continuar...")
        return
    
    for i, doc in enumerate(resultado, start=1):
        decoracionMenu.texto(f"   {i}: {doc['_id']['nombre']} ({doc['_id']['codigo']})",100,"izq")
        decoracionMenu.texto(f"   Confirmados: {doc['totalConfirmados']}",100,"izq")
        decoracionMenu.texto("="*100)
    input("Presione Enter para continuar...")