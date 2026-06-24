def superior_menu(cant, pos=0):
    if pos == 1:
        return "||\t" + "="*cant
    
    elif pos == 2:
        return "="*cant + "\t||"
    
    elif pos == 0:
        return "||\t" + "="*cant + "\t||"
    
    elif pos == 3:
        return "=" * cant
    
    elif pos == 4:
        return "||\t" + " " * cant + "\t||"