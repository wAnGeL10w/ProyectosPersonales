/*Progrma Rebibo de Luz Sentencia SWITCH*/
#include <stdio.h>
//Declaración de constantes
#define Z1 0.793
#define Z2 0.956
#define Z3 1.025
#define Z4 2.802

//Declaración de función
void ConsumoTotal(float zona);

//Función principal
main()
{
	//Declaracion de Variables
	int zona;
	float consumo, total;
	//Lectura de Datos
	printf("Seleccione la zona en la cual vive\n");
	printf("1.-Escobedo\n");
	printf("2.-Monterrey\n");
	printf("3.-Apodaca\n");
	printf("4.-San Pedro\n");
	printf("En cual de estas zonas vive?\n");           scanf("%d",&zona);
	//Sentencia SWITCH
	switch (zona)
	{
		case 1:
			ConsumoTotal(Z1);
		break;
		case 2:
			ConsumoTotal(Z2);
		break;
		case 3:
			ConsumoTotal(Z3);
		break;
		case 4:
			ConsumoTotal(Z4);
		break;
		default:
			printf("Zona invalida\n");
		break;	
	}
	return 0;
}

//Definición de función
void ConsumoTotal(float zona){
	float consumo=0.0,total=0.0;
	printf("Teclee la cantidad consumida: ");    scanf("%f",&consumo);
	total=zona*consumo;
	printf("\nEl consumo total es de %.2f pesos",total);
}
