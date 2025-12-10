tareas = []

def menu():
    print("\n== Menu de opciones ==")
    print("1. Agregar tarea.")
    print("2. Lista de tareas.")
    print("3. Eliminar tarea por su numero.")
    print("4. Salir")
    
    
def agregarTarea():
    
    '''Con esta funcion lo que hacemos es cargar una tarea a la lista vacia que creamos anteriormente cambiandola a global para poder utilizarla, 
    si colocamos una tarea en blanco nos lanza un mensaje de error
    por la cual debemos ingresar una tarea.'''
    
    global tareas
    
    while True:
        agregar = input("\nHola! que tarea desea agregar?: ").lower().strip()
        if agregar == "":
            print("Error. Ingrese una tarea.")
            continue
        
        tareas.append(agregar)
        
        print(f'Tarea: {agregar} ingresada con exito!.\n')
        
        while True:
            otra = input("Desea agregar una otra tarea? (si/no): ").lower().strip()
            if otra == "si":
                break
            elif otra == "no":
                print("Saliendo....")
                return
        
def listaTareas():
    
    '''Con esta funcion basicamente es ver las tareas que agregamos 
    por indice'''
    
    global tareas   
    print("\n== Lista de tareas ==")
    if not tareas:
        print("La lista se encuentra vacia.")
    for i in range(len(tareas)):
        print(f"{i+1}. Tarea: {tareas[i] }")
        
def eliminarTarea():
    
    '''En esta funcion eliminamos una terea mediante el numero de inidice que se le asgino a la tarea
    usamos el metodo pop() para eliminar dicha tarea'''
    
    listaTareas()
    global tareas
    
    print("\n== Eliminar Tareas ==")
    
    if not tareas:
        print("Error. La lista de tareas se encuentra vacia.")
        
    while True:
        try:
            borrar = int(input("Coloque el numero de indice de la tarea que desea eliminar: "))
        except ValueError:
            print("Error. Coloque un numero")
            continue
        
        if borrar < 1 or borrar > len(tareas):
            print("Error. Fuera del rango")
            continue
        
        tarea = tareas[borrar - 1]
        delete = input(f"Desea eliminar la tarea: {tarea}? (si/no): ").lower().strip()
        
        if delete == "si":
            tareas.pop(borrar - 1)
            print(f"\nTarea {tarea} eliminada.")
        
        elif delete == "no":
            print("Volviendo")
            return
        
        if not tareas:
                print("\nLa lista ya se encuentra vacia, volviendo al menu.")
                return
        while True:
            
            listaTareas()
            otra = (input("\nDesea eliminar otra tarea? (si/no): ")).lower().strip()
            if otra == "si":
                break
            if otra == "no":
                print("Volviendo al menu...")
                return
                 
while True:
    menu()
    try:
        inicio = int(input("Hola! Bienvenido al menu de tareas, seleccione una opcion para comenzar: "))
        if inicio < 1 or inicio > 4:
            print("\nError. Se encuentra fuera del rango de opciones.")
    except ValueError:
        print("\nError. Solo se permiten numeros")
        
    if inicio == 1:
        agregarTarea()
        
    elif inicio == 2:
        listaTareas()
        
    elif inicio == 3:
        eliminarTarea()
        
    elif inicio == 4:
        print("Saliendo....")
        break
        
    
    
    
