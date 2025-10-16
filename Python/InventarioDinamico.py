import os

#Funcion para limpiar pantalla y no se acumulen caracteres
def limp_pant():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion donde se ejecutará todo el codigo dependiendo de la opcion
def Inventario(dicci,op_c):
    if op_c==1:
        print("\nVAMOS A AÑADIR UN PERSONAJE!\n")
        while True:
            try:
                nom=input("Ingrese el nombre del personaje: ")
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
            else:
                break
        if nom in dicci:
            print("El personaje ya existe.")
            #Para que salga directamente de la funcion
            exit
        else:
            lista_tup=[]
            #Hize un while anidado porque poner las 3 en uno mismo era un poco contraproducente
            while True:
                while True:
                    try:
                        nom_obj=input("Ingrese el nombre del objeto: ")
                    except ValueError:
                        print("Error de valor")
                    else:
                        break
                while True:
                    try:
                        cant=int(input("Ingrese la cantidad: "))      
                    except ValueError:
                        print("Error de valor")
                    else:
                        if cant>0:
                            break
                        else:
                            print("Cantidad no valida")
                            continue
                while True:
                    try:
                        conti=int(input("Desea agregar otro objeto?\n1.Si\n2.No\n"))
                    except ValueError:
                        print("Error de valor")
                    else:
                        if conti==1 or conti==2:
                            break
                        else:
                            print("Valores no admitidos")
                            continue
                if conti==1:
                    lista_tup.append((nom_obj,cant))
                    continue
                else:
                    lista_tup.append((nom_obj,cant))
                    break
            dicc[nom]=lista_tup.copy()
            lista_tup.clear()
            limp_pant()
        return dicci
    elif op_c==2:
        print("\nINFORMACIÓN DE UN PERSONAJE\n")
        while True:
            try:
                nom=input("Ingrese el nombre del personaje: ")
            except ValueError:
                print("Error de valor")
            else:
                break
        if nom in dicci:
            print(f"Informacion de personaje: {nom}")
            print(dicci[nom])
            input("\nPresione cualquier tecla para continuar ")
            limp_pant()
        else:
            print("El personaje no existe")
        limp_pant()
        return dicci
    elif op_c==3:
        print("\nVAMOS A AÑADIR UN OBJETO!\n")
        while True:
            try:
                nom=input("Ingrese el nombre del personaje: ")
            except ValueError:
                print("Error de valor")
            else:
                break
        if nom in dicci:
            #Datos es una lista de tuplas
            datos=dicci[nom]
            while True:
                try:
                    nuevo_obj=input("Escribe el nuevo objeto: ")
                except ValueError:
                    print("Error de Valor")
                else:
                    break
            #Buscamos el objeto en el la clave especifica (personaje)
            #Esta varaible me ayuda por si se entra al ciclo pero nunca se ejecuta el if anidado
            valid=0
            for y in range(len(datos)):
                if nuevo_obj in datos[y]:
                    nueva_lista=list(datos[y])
                    var=nueva_lista.pop()
                    del datos[y]
                    datos.insert(y,(nuevo_obj,var+1))
                    print(datos[y])
                    valid=1
            if valid!=1:
                cant=int(input("Ingrese la cantidad: "))
                #Aqui abajo truena pero no se bien el porque
                datos.append((nuevo_obj,cant))
            return dicci
        else:
            print("El personaje no existe")
            exit
    elif op_c==4:
        print("\nVAMOS A QUITAR UN OBJETO\n")
        while True:
            try:
                nom=input("Ingrese el nombre del personaje: ")
            except ValueError:
                print("Error de valor")
            else:
                break
        if len(dicci)==0:
            print("No existe ningun personaje")
            exit
        else:
            if nom in dicci:
                datos=dicci[nom]
                while True:
                    try:
                        eli_obj=input("Escribe el objeto a eliminar: ")
                    except ValueError:
                        print("Error de valor")
                    else:
                        break
                valid=0
                for y in range(len(datos)):
                    if eli_obj in datos[y]:
                        del datos[y]
                        valid=1
                if valid!=1:
                    print("El objeto no existe")
                else:
                    print("Objeto eliminado con exito!")
                return dicci
            else:
                print("El objeto no se encuentra ")
                exit
    elif op_c==5:
        if len(dicci)==0:
            print("Inventario vacío")
        else:
            for info in dicci:
                print(info, "=" ,dicci[info])
            print()
    
#Declaro el diccionario fuera de while para que se acumulen los personajes
dicc={}

#Ciclo Principal para mandar a llamar n veces la función
while True:
    opciones=["Añadir Personaje","Mostrar inventario","Agregar objeto","Quitar objeto","Mostrar todos"]
    opciones_nums=[1,2,3,4,5]
    print("BIENVENIDO AL INVENTARIO DE PERSONAJES!!\n")
    while True:
        try:
            print("Seleccione alguna de las siguientes opciones:\n")
            for i in range(0,len(opciones)):
                print(i+1 ,opciones[i])
            print()
            op=int(input())
        except ValueError:
            print("Error de Valor")
        else:
            if op in opciones_nums:
                break
    #Mandamos a llamar a la función
    '''Puedo modificar que se retorne o no el diccionario, ya que no hago nada con el. Lo
    tenia porque al final lo imprimia pero pues da igual xd'''
    Inventario(dicc,op)
    while True:
        try:
            op=int(input("\nDesea seguir ejecutando el programa?\n1).Si\n2).No\n"))
        except ValueError:
            print("Error de valor")
        else:
            if op==1 or op==2:
                break
            else:
                print("Opcion no valida")
                continue
    if op==2:
        break
    else:
        limp_pant()
        continue

for d in dicc:
    print(d, "=" ,dicc[d])
input()
limp_pant()

#Variable para usar en siguientes casos
archivo="Inventario.txt"

#Escribimos el contenido del diccionario en un archivo.txt
with open(archivo,'w',encoding='utf-8') as f:
    f.write('DATOS INVENTARIO DE PERSONAJES\n\n')
    for cve in dicc:
        f.write(f"{cve} = {dicc[cve]}")
        f.write('\n')

#Abrimos el archivo.txt creado
os.startfile(archivo)