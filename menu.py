import os
import opciones_menu
from decoracionMenu import superior_menu

def menu_principal(uri,db):
    while True:
        os.system("cls")
        print(superior_menu(22,1) + " MENÚ " + superior_menu(22,2))

        print("|| - [1] Listado de eventos" + "\t" * 5 +"||")
        print("|| - [2] Listado de por categoría" + "\t" * 4 +"||")
        print("|| - [3] Listado de invitados" + "\t" * 5 +"||")
        print("|| - [4] Buscar invitados por correo" + "\t" * 4 +"||")
        print("|| - [5] Top 3 eventos por números de invitados confirmados" + "\t" * 1 +"||")
        print("|| - [x] Volver" + "\t" * 7 +"||")

        opcion = input(superior_menu(50) + "\n\n Opción: ")

        if opcion.isalpha():
            opcion.lower()

        match opcion:
            case "1":
                col = db["eventos"]
                opciones_menu.listadoEventos(uri,db,col)
            case "2":
                opciones_menu.listadoEventosCategoria(uri,db,col)
            case "3":
                col = db["invitados"]
                opciones_menu.listadoInvitados(uri,db,col)
            case "4":
                opciones_menu.invitadosCorreo(uri,db,col)
            case "5":
                opciones_menu.topEventos(uri,db,col)
            case "x":
                return
            case _:
                print("Error: valor inválido")
                input("Presione Enter para continuar...")