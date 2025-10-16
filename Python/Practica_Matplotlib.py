import matplotlib.pyplot as plt
import numpy as np
import random

def GraficaPuntos():
    #Datos a graficar
    x_numbers=[1,2,3]
    y_numbers=[2,4,6]

    #Se dibujan los puntos
    plt.plot(x_numbers,y_numbers,'o')
    #se activa la cuadricula
    plt.grid()
    #Mostramos la grafica
    plt.show()


def GraficaLineas():
    lista=[round(random.uniform(50.0,80.0),2) for x in range(13)]
    años=range(2000,2013)

    plt.plot(años,lista,"--kd",ms=10,mec='r')
    plt.show()


def GraficaDosBarras():
    #Datos a graficar
    x1=np.array([0,1,2,3])
    y1=np.array([3,8,1,10])
    x2=np.array([0,1,2,3])
    y2=np.array([6,2,7,11])

    plt.title("Este es el título")
    plt.xlabel("Texto del eje X")
    plt.ylabel("Texto del eje Y")
    #Se grafican las dos series de datos
    plt.plot(x1,y1,x2,y2)
    #Imprimimos la grafica
    plt.show()

def GraficaDeBarras1():
    #Datos a graficar
    x=[round(random.uniform(50.0,80.0),2) for x in range(10)]
    y=[round(random.uniform(50.0,80.0),2) for x in range(10)]

    #Scatter es para graficar puntos
    plt.scatter(x,y,cmap="viridis")
    #Colorbar es para mostrar la barra de colores
    plt.colorbar()
    #Mostramos la grafica
    plt.show()

def GraficaDeBarras2():
    x=np.array(["A","B","C","D"])
    y=np.array([3,8,1,10])

    plt.bar(x,y)
    #Para invertir la grafica y que se ponga como invertida
    #Modificar el ancho de barra width (verticales) y horizontales (height)
    plt.show()
    plt.barh(x,y,color="b")
    plt.show()


def GraficaDePastel():
    #Datos a graficar, 8 numeros aleatorios del 1 al 21
    y=np.array([random.randint(1,21) for x in range(8)])
    #Definimos las frutas
    frutas=["Manzana","Pera","Platano","Naranja","Mandarina","Kiwi","Sandia","Guayaba"]
    #Definimos los colores
    colores=["b","k","hotpink","orange","purple","cyan","brown","gray"]
    #Graficamos
    plt.pie(y, labels=frutas,shadow=True, colors=colores)
    #Mostramos la grafica
    plt.show()

GraficaLineas()
GraficaPuntos()
GraficaDosBarras()
GraficaDeBarras1()
GraficaDeBarras2()
GraficaDePastel()
