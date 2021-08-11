# Realizar una aplicación que maneje una Lista de Tareas.
# Deben decidir que categorías utilizar (ej: trabajo, estudio, personal, etc.), el manejo del tiempo 
# (fechas, urgencias, límites temporales, etc.)
# También deben decidir que estructuras de datos usar, listas y/o diccionarios y/o archivos de texto, etc.
# Agregar la mayor cantidad de variantes útiles posible!
from datetime import datetime
from validacion import validacionEntero
import csv

def encabezado():
    f=datetime.now()
    dia = f.day
    mes = f.month
    año = f.year
    
    print("\n******************************")
    print("\t¡¡To Do List!!")
    print("******************************")
    print("     Hoy es:",dia, "-", mes, "-", año)
    print("******************************\n")

def verRegistroDeActividades(): # Necesito ver la lista de actividades guardadas
    # Tarea,Categoria,Fecha (Orden de datos almacenados)
    archivo = open("to_do_list.txt", newline='', encoding="utf-8")
    lector_csv = csv.reader(archivo, delimiter=',', quotechar='\t', quoting=csv.QUOTE_ALL)
    for linea in lector_csv:
        print(linea[-1], linea[0])
    archivo.close()
    # Creo un objeto lector de csv = delimito las lineas usando la coma (delimitador) haciendo 
    # que cada linea pueda separarse facilmente en varios objetos.
    # Los objetos los almacena en una lista por eso uso un bucle for e imprimo el ultimo objeto (fecha)
    # y el primero (nombre).
    
def agregarActividad(tarea,categoria,fecha): # Necesito guardar los datos
    file = open("to_do_list.txt","a", encoding="utf-8")
    file.write("\n" + tarea + "," + categoria + "," + fecha)
    file.close()

def actividadParaHoy():
    fecha = datetime.now().strftime("%Y/%m/%d") # año, mes y dia
    fechaStr = str(fecha)
    archivo = open("to_do_list.txt", encoding="utf-8")
    while True:
        # Se ejecutara siempre
        f = archivo.readline()
        if f == "":
            # Si la linea está vacía (final del archivo)
            # rompera el bucle.
            break
        if fechaStr in f:
            print()
            print(">>",f.split("\n"))
    archivo.close()

def menu():
    encabezado()
    print(">>>Bienvenido a su Asistente Virtual<<<\n")
    print("Menú de Opciones\n")
    print("1) Registrar Actividad")
    print("2) Ver Lista de Actividades")
    print("3) Actividades para Hoy")
    print("4) Salir\n")
    opcion = validacionEntero(">>> ",min=0,max=4)
    
    if opcion == 1:
        tarea = input("Ingrese nombre de la actividad: ")
        categoria = input("Ingrese tipo de actividad (tarea,compra,examen,etc):")
        fecha = input("Ingrese fecha de la actividad (aaaa/mm/dd): ")
        agregarActividad(tarea,categoria,fecha)
        print("Actividad completada...")
        return menu()
    elif opcion == 2:
        print("Actividades registradas: ")
        verRegistroDeActividades()
        return menu()
    elif opcion == 3:
        print("\nActividades para Hoy: ")
        actividadParaHoy()
        return menu()
    elif opcion == 4:
        print("\nExit..\n")
        exit()

if __name__ == '__main__':
    menu()

