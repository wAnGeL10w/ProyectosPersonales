/*Programa Arreglos-Matriz*/
#include <stdio.h>
#include <stdlib.h>

//Función principal
main()
{
	//Declaracion de Variales
	int fila=0, columna=0, n_p=0, n_ne=0, n_n=0, Matriz[3][3];
	//Entrada de datos
	for (fila=0; fila<3; fila++)
	{
		for (columna=0; columna<3; columna++)
		{
			printf("Elemento [%d][%d]: ",fila+1,columna+1);
			scanf("%d",&Matriz[fila][columna]);
		}
	}
	system("cls");
	//Impresion de datos
	for (fila=0; fila<3; fila++)
	{
		printf("\n");
		for (columna=0; columna<3; columna++)
		{
			//Validación de tipos de numeros
			if (Matriz[fila][columna]>0){
				n_p++;
			}else{
				if (Matriz[fila][columna]<0){
					n_ne++;
				}else{
					n_n++;
				}
			}
			//Impresion de matriz
			printf("| %3d|",Matriz[fila][columna]);
		}
	}
	printf("\n");
	printf("\nNumeros positivos: %d",n_p);
	printf("\nNumeros negativos: %d",n_ne);
	printf("\nNumeros neutros:   %d",n_n);
	
}
