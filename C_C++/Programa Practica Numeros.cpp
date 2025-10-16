/*Programa Sentencia FOR*/
#include <stdio.h>
#include <stdlib.h>

main()
{
	//Declaracion de Variables
	int migrantes=0, respuesta=0, edad=0, est_c=0, dep_eco=0, acep=0, rech=0;
	//Sentencia FOR
	for (migrantes=0; migrantes<7; migrantes++)
	{
		system("cls");
		printf("Es extranjero?\n");
		printf("1-Si\n");
		printf("2-No\n");
		scanf("%d",&respuesta);
		printf("Cual es su edad\n");
		scanf("%d",&edad);
		printf("Cual es su estado civil?\n");
		printf("1-Soltero\n");
		printf("2-Casado\n");
		printf("3-Viudo\n");
		printf("Su opcion?: ");
		scanf("%d",&est_c);
		printf("Tiene dependientes economicos?\n");
		printf("1-Si\n");
		printf("2-No\n");
		scanf("%d",&dep_eco);
		if (respuesta==1 && edad<=40 && est_c==1 && dep_eco==2)
			acep++;
		else
			rech++;
	}
	
	/*El programa solo aceptará migrantes que cumplan con ciertas normas,
	de lo contario serán rechazados*/
	
	//Impresion a pantalla
	printf("\nMigrantes aceptados.........%d",acep);
	printf("\nMigrantes no aceptados......%d",rech);
}

