/*Programa Apoyo Arreglos-Matriz*/
#include <stdio.h>
#include <stdlib.h>
main()
{
	//Declaracion de Variables
	int fila=0,columna=0,Matriz[3][3];
	float suma=0.0,prom=0.0;
	//Sentencia FOR
	for (fila=0; fila<3; fila++)
	{
		for(columna=0; columna<3; columna++)
		{
			printf("Elemento [%d][%d]: ",fila+1,columna+1);
			scanf("%d",&Matriz[fila][columna]);
		}
	}
	system("cls");
	for (fila=0; fila<3; fila++)
	{
		printf("\n");
		for (columna=0; columna<3; columna++)
		{
			printf("| %3d|",Matriz[fila][columna]);
			suma+=Matriz[fila][columna];
		}
	}
	//Proceso
	prom=suma/9;
	//Impresion a Pantalla
	printf("\n");
	printf("\nLa suma es %.2f",suma);
	printf("\nEl promedio es %.2f",prom);
}

