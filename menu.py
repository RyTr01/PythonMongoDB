import os
import opciones_menu
from decoracionMenu import superior_menu

def menu_principal(uri,db):
    while True:
        os.system("cls")
        print(superior_menu(22,1) + " MENÚ " + superior_menu(22,2))
        """
        Filtrar datos de clientes e invitados según criterios definidos.
        Usar regex a partir de requerimientos de busqueda.
        Búsqueda en subdocumentos simple usar lookup para combinar datos entre colecciones.
        Búsqueda en subdocumentos con asociaciones lógicas complejas.
        """
        print("|| - [1] Listado de eventos" + "\t" * 5 +"||")
        print("|| - [2] Listado de invitados" + "\t" * 5 +"||")
        print("|| - [3] Validación de acceso" + "\t" * 5 +"||")
        print("|| - [4] Top 3 eventos por números de invitados confirmados" + "\t" * 1 +"||")
        print("|| - [x] Volver" + "\t" * 7 +"||")

        opcion = input(superior_menu(50) + "\n\n Opción: ")

        if opcion.isalpha():
            opcion.lower()

        match opcion:
            case "1":
                col = db["eventos"]
                opciones_menu.listadoEventos(uri,db,col)
            case "2":
                col = db["invitados"]
                opciones_menu.listadoInvitados(uri,db,col)
            case "3":
                pass
            case "4":
                pass
            case "x":
                return
            case _:
                pass