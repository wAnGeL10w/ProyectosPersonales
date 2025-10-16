
#Creacion de un simulador de cine
sala=[]

#La capacidad de la sala es de 5 filas y 6 columnas
for i in range(5):
    filas=[]
    for j in range(6):
        filas.append('D')
    sala.append(filas)

#Imprime la sala
def ImprimirSala():
    for i in range(0,len(sala)):
        print(sala[i])

#Contador de clientes atendidos
c=0

#Repetimos el ciclo hasta que el usuario decida salir
while True:
    c+=1
    op=int(input("\nBIENVENIDO AL CINE, SELECCIONE ALGUNA OPCION:\n1)Comprar boleto\n2)Imprimir Asientos\n3)Salir\n"))
    #Opcion Comprar boleto
    if op==1:
        #El ciclo se repite hasta que el usuario ingrese una fila y asiento correctos
        while True:
            fila=int(input("\nIngresa la fila donde desea sentarse (1-5): "))
            asiento=int(input("Ingrese el asiento (1-6): "))
            if (fila>=1 and fila<=5 and asiento>=1 and asiento<=6):
                break
            else:
                print("Fila o columna fuera de rango")
        #Validamos si el asiento esta ocupado o no
        if sala[fila-1][asiento-1]=='X':
            print("\nEl asiento esta ocupado!!!!")
            c-=1
            continue
        else:
            for f in range(0,len(sala)):
                for a in range(6):
                    sala[fila-1][asiento-1]='X'
            print("Fuiste añadido con exito!!!")
        print()
    #Opcion Imprimir Asientos
    elif op==2:
        print()
        ImprimirSala()
        c-=1
    #Opcion Salir
    elif op==3:
        print("\nGracias por visitarnos, vuelva pronto!")
        break
    #Opcion no valida
    else:
        print("Opcion no Valida")
        c-=1
        continue

print(f"Total de clientes atendidos: {c}")