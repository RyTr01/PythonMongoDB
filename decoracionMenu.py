def superior_menu(cant, pos=0):
    if pos == 1:
        return "||\t" + "="*cant
    
    elif pos == 2:
        return "="*cant + "\t||"
    
    elif pos == 0:
        return "||" + "=" * cant + "||"
    
    elif pos == 3:
        return "=" * cant
    
    elif pos == 4:
        return "||" + " " * cant + "||"
    
def texto(texto,ancho=100, pos = "cen"):
    if pos == "izq":
        return print(f"||{texto:<{ancho}}||")
    
    elif pos == "der":
        return print(f"||{texto:>{ancho}}||")
    
    elif pos == "cen":
        return print(f"||{texto:^{ancho}}||")