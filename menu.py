import os
import opciones_menu
import decoracionMenu

def menu_principal(uri,db):
    while True:
        os.system("cls")
        decoracionMenu.texto("="*47 + " MENÚ " + "="*47, 100 , "cen")
        decoracionMenu.texto(" - [1] Listado de todos los eventos", 100 , "izq")
        decoracionMenu.texto(" - [2] Listado de eventos por categoría", 100 , "izq")
        decoracionMenu.texto(" - [3] Lista de invitados", 100 , "izq")
        decoracionMenu.texto(" - [4] Validar Acceso de un invitado a un evento", 100 , "izq")
        decoracionMenu.texto(" - [5] Buscar invitados por correo", 100 , "izq")
        decoracionMenu.texto(" - [6] Top 3 eventos por números de invitados confirmados", 100 , "izq")
        decoracionMenu.texto(" - [X] Volver", 100 , "izq")

        opcion = input(decoracionMenu.superior_menu(100) + "\n\n Opción: ")

        if opcion.isalpha():
            opcion.lower()

        match opcion:
            case "1":
                col = db["eventos"]
                opciones_menu.listadoEventos(uri,db,col)
            case "2":
                col = db["eventos"]
                opciones_menu.listadoEventosCategoria(uri,db,col)
            case "3":
                col = db["invitados"]
                opciones_menu.listadoInvitados(uri,db,col)
            case "4":
                col = db["eventos"]
                opciones_menu.validarAcceso(uri,db,col)
            case "5":
                col = db["invitados"]
                opciones_menu.invitadosCorreo(uri,db,col)
            case "6":
                col = db["eventos"]
                opciones_menu.topEventos(uri,db,col)
            case "x":
                return
            case _:
                print("Error: valor inválido")
                input("Presione Enter para continuar...")