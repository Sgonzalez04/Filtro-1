import json
general={}
general['Departamentos']=[]
with open('manuales.json', "r") as manuales:
    data=json.load(manuales)
    lenguaje = data["manuales"]

#lee los datos
def leer_Datos():
    with open("manuales.json", "r",encoding="utf-8") as manuales:
        data=json.load(manuales)
    return data

#escribe los datos
def escribir(data):
    with open ("manuales.json","w",encoding="utf-8") as file: #utf-8 para aceptar caracteres especiales
        json.dump(data,file,ensure_ascii=False,indent=4)#ensure_ascii=False es para admitir caracteres especiales

#reintentar
def reintetar():
    act=input("desea volver a realizar la operacion(si) o volver al menu(no): ")
    if act.lower() == "si":
        return True
    elif act.lower() == "no":
        return False
    elif act != "si" or act != "no":
        print("escriba solo si o no")
        return reintetar()

def crear_nuevo():
    data = leer_Datos()
    lenguaje = input("Introduzca el nombre del lenguaje que desea agregar: ")
    
    if lenguaje in data["manuales"]:
        print("El lenguaje ya existe en los datos, volvera al inicio.")
        input("Presione una tecla para continuar")
        return
    
    len_n = {"author": "",
             "paginas": "",
             "temas": []}
    
    len_n["author"] = input("Introduzca el nombre del nuevo autor: ")
    len_n["paginas"] = input("Introduzca el número de páginas: ")

    while True:
        tema = temas()
        len_n["temas"].append(tema)
        if not reintetar():
            break

def temas():
    titulo_nuevo = input("Introduzca el nuevo título del tema: ")
    clasificacion_nueva = int(input("Introduzca el tipo de clasificación (1 = básico, 2 = intermedio, 3 = avanzado): "))
    tema_nuevo = {"Titulo": titulo_nuevo,
                  "Clasificación": clasificacion_nueva}
    print("Se le preguntara la cantidad de veces que usted quiere si quiere agregar otro tema")
    return tema_nuevo

def actualizar():
    data = leer_Datos()
    print(listar())
    lenguaje = input("Introduzca el nombre del lenguaje que desea actualizar: ")

    if lenguaje not in data["manuales"]:
        print("El lenguaje no existe en los datos.")
        input("Presione una tecla para continuar")
        return
    
    len_n = data["manuales"][lenguaje]
    
    len_n["author"] = input(f"Nuevo autor ({len_n['author']}): ")
    len_n["paginas"] = input(f"Nuevo número de páginas ({len_n['paginas']}): ")

    len_n["temas"] = []

    while True:
        tema = temas()
        len_n["temas"].append(tema)
        if not reintetar():
            break

    data["manuales"][lenguaje] = [len_n]
    print("Completado. Se le mostrarán los datos actualizados:")
    print(len_n)
    escribir(data)
    input("Presione una tecla para continuar")

def eliminar():
    data=leer_Datos()
    print(listar())
    eliminar=(input("Ingrese el nombre del lenguaje a borrar: "))
    if eliminar in data["manuales"]:
        del data["manuales"][eliminar]
        with open('manuales.json', 'w') as manuales:
            json.dump(data, manuales, indent=4)#.dump para guardar
        print("Lenguaje eliminado correctamente")
    else:
        print("Nombre no encontrado")

    input("Presione una tecla para continuar")

def listar():
    data = leer_Datos()
    manuales_data = data["manuales"]
    i = 1
    for lenguaje, info in manuales_data.items():
        print(f"{i}) Lenguaje: {lenguaje}")
        print(f"   Author: {info['author']}")
        print(f"   Páginas: {info['paginas']}")
        print("   Temas:")
        for tema in info['temas']:
            print(f"     - {tema['Titulo']} (Clasificación: {tema['Clasificación']})")
        print()
        i += 1
    input("Presione una tecla para continuar")

def informe():
    with open("manuales.json", "r") as archivo_entrada:
        datos = json.load(archivo_entrada)
    lineas_a_escribir = []

    for nombre, info in datos["manuales"].items():
    #a cada se le coloca a la clave nombre y el valor info
        basicos = len([tema for tema in info["temas"] if tema["Clasificación"] == 1])
        #en clave es temas y el valor es info, crea una lista en que todos los temas solo contienen 1
        #calcula el numero de elementos de la lista que sean 1 y con len se asigna como valor de basicos
        intermedios = len([tema for tema in info["temas"] if tema["Clasificación"] == 2])
        avanzados = len([tema for tema in info["temas"] if tema["Clasificación"] == 3])
        
        linea = f"{nombre}:\n"
        linea += f"     Temas Básicos: {basicos}\n"
        linea += f"     Temas Intermedios: {intermedios}\n"
        linea += f"     Temas Avanzados: {avanzados}\n"
        lineas_a_escribir.append(linea)

    with open("datos.txt", "w") as archivo_salida:
        for linea in lineas_a_escribir:
            archivo_salida.write(linea)

    print("Operación completada, informe realizado")
    input("Presione una tecla para continuar")

def menu():
    seguir=True
    while seguir:
        print("="*46)
        print("===============Manuales Técnicos==============")
        print("="*46)
        print(" ")
        print(" "*4+" 1) Crear.")
        print(" "*4+" 2) Modificar.")
        print(" "*4+" 3) Eliminar.")
        print(" "*4+" 4) Listar.")
        print(" "*4+" 5) Generar informe de datos.")
        print(" "*4+" 6) Salir del programa\n")
        print("="*46)

        opcion = int(input('Opcion ==========> '))
        if (opcion) == 6:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
        switch = {1: crear_nuevo, 2:actualizar ,3:eliminar ,4:listar ,5:informe}
        switch[opcion]()

menu()
