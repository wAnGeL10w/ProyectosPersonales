
#Defino la base de mi diccionario
libro={
    "Titulo": "",
    "Autor": "",
    "Año": 0,
    "Categoria": ""
    }
#Defino las categorias
categorias=["Programacion","Ciencias","Filosofia"]
#Lista para guardar los libros
datos=[]
#Lista para guardar la biblioteca
biblioteca=[[],[],[]]
#Lista para contar los libros por categoria
cont=[]
c=0
for i in range(3):
    #El ciclo se repite hasta que el usuario decida no agregar mas libros
    while True:
        c+=1
        print(f"AÑADIENDO UN LIBRO DE {categorias[i]}")
        #Captura de datos
        tit=input("Escribe el titulo del libro: ")
        aut=input("Escribe el nombre del autor: ")
        año=int(input("Escribe el año: "))
        #Inserto los datos en el diccionario
        libro["Titulo"]=tit
        libro["Autor"]=aut
        libro["Año"]=año
        libro["Categoria"]=categorias[i]
        #Validacion para dejar de agregar libros
        op=int(input("DESEA AÑADIR UN NUEVO LIBRO:\n1) Si\n2)No\n"))
        if op==1:
            #Agrego el libro a la lista de datos
            datos.append(libro.copy())
            libro.clear()
        else:
            cont.append(c)
            c=0
            break
    #Agrego la lista de libros a la biblioteca
    biblioteca[i]=(datos.copy())
    datos.clear()
    
#Busqueda de libros por año
año_s=int(input("Escribe un año a buscar: "))
for categorias in biblioteca:
    for libros in categorias:
        if libros["Año"]==año_s:
            for clave,valor in libros.items():
                print(f"{clave}: {valor}",end="")
            print()

#Impresion de total de libros de cada categoria
print("\tLIBROS POR CATEGORIA")
for y in range(3):
    print(f"Libros de categoria {categorias[y]}: {cont[y]}")
print(biblioteca)