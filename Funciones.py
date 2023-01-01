def buscaLista(filepath=R"listadetareas.txt"):
    """ Leer tareas de archivo TXT """
    with open(filepath, 'r') as file_local: 
        listaTareasLocal = file_local.readlines()
    return listaTareasLocal

def escribeLista(listaTareas, filepath="listadetareas.txt"):
    """ Escribe tareas en archivo TXT. 
    Solo en un procedimiento, por eso no hay ningun return"""
    with open(filepath, 'w') as file_local: 
        file_local.writelines(listaTareas)
