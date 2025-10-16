/*Programa Casa de Cambio*/
#include <stdio.h>
#include <stdlib.h>
//Declaración de constantes
#define USD 19.44 //Dolar Estadounidense
#define EUR 20.11 //Euro
#define JPY 0.014 //Yen Japonés
#define GBP 23.13 //Libra esterlina
#define AUD 12.98 //Dolar Auatraliano

/*La divisa principal se toma como MXN*/

//Función principal
main()
{
	//Declaración de Variables
	int  opcion=0, seguir=0, usd=0, eur=0, jpy=0, gbp=0, aud=0;
	float cantidad=0.0, tot_usd=0.0, tot_eur=0.0, tot_jpy=0.0, tot_gbp=0.0;
	float tot_aud=0.0, c_usd, c_eur=0.0, c_jpy=0.0, c_gbp=0.0, c_aud=0.0;
	//Sentencia Do
	do
	{
		system("cls");
		printf("Seleccione el tipo de divisa al que desee cambiar\n");
		printf("1-Dolar Estadounidense........19.44\n");
		printf("2-Euro........................20.11\n");
		printf("3-Yen Japone..................0.014\n");
		printf("4-Libra Esterlina.............23.13\n");
		printf("5-Dolar Australiano...........12.98\n");
		printf("Elija su opcion: ");
		scanf("%d",&opcion);
		//Valido la entrada de opcion correcta
		if (opcion>=1 and opcion<=5){
			printf("Teclee la cantidad a cambiar: ");
			scanf("%f",&cantidad);
			switch (opcion){
				case 1: usd++; c_usd+=cantidad; break;
				case 2: eur++; c_eur+=cantidad; break;
				case 3: jpy++; c_jpy+=cantidad; break;
				case 4: gbp++; c_gbp+=cantidad; break;
				case 5: aud++; c_aud+=cantidad; break;
			}
		}else{
			printf("\nOpcion invalida, vuelva a intentar!\n");
		}
		//cantidad++;
		printf("Teclee 1 para contuinuar...");
		scanf("%d",&seguir);
	}while (seguir==1);
	tot_usd=c_usd/USD;
	tot_eur=c_eur/EUR;
	tot_jpy=c_jpy/JPY;
	tot_gbp=c_gbp/GBP;
	tot_aud=c_aud/AUD;
	printf("\nDolares USA cambiados...........%d",usd);
	printf("\nEuros cambiados.................%d",eur);
	printf("\nYenes cambiados.................%d",jpy);
	printf("\nLibras cambiados................%d",gbp);
	printf("\nDolares AUD cambiados...........%d",aud);
	printf("\nCantidad en Dolar USA...........%.2f",tot_usd);
	printf("\nCantidad en Euro................%.2f",tot_eur);
	printf("\nCantidad en Yenes...............%.2f",tot_jpy);
	printf("\nCantidad en Libras..............%.2f",tot_gbp);
	printf("\nCantidad en Dolar AUD...........%.2f",tot_aud);
}
