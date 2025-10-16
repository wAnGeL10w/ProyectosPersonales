/*Programa laboratorio PROGRAMACION*/

/*IMPORTANTE, el siguiente codigo fallará en SO que no sean Windows
debido al comando system("cls");*/
#include <stdio.h>
#include <stdlib.h>
//Declaracion de constantes
#define IVA 0.16
#define CAM 357.49
#define PNT 418.95
#define R_INT 139.99
#define CALC 84.75
#define ZAP 1150.89
//Declaracion de funcion
void E_opc();

int resp, punt=0, t_punt=0;
main()
{
	//Declaracion de variables
	int client=0, opcion=0, cantidad=0, camisa=0, pantalon=0;
	int ropa_int=0, calcetines=0, zapatos=0, seguir=0, seguir2=0;
	float efect=0.0, camb=0.0, tot_cam=0.0, tot_pant=0.0, tot_r_int=0.0, tot_calc=0.0;
	float tot_zap=0.0, subt=0.0, tot=0.0, iva=0.0, tot_v=0.0, v_totC=0.0;
	//Ventas totales de cada articulo
	float vt_cam=0.0, vt_pnt=0.0, vt_rint=0.0, vt_calc=0.0, vt_zap=0.0; 
	//Lectura de Datos
	do
	{
		client++;
		punt=0;
		t_punt=0;
		camisa=0; pantalon=0; ropa_int=0; calcetines=0; zapatos=0;
		do
		{
			system("cls");
			printf("Cliente %d Bienvenido a Live to wear\n",client);
			printf("Teclee el numero de la opcion que desee comprar\n");
			printf("1-Camisa..........$357.49\n");
			printf("2-Pantalon........$418.95\n");
			printf("3-Ropa interior...$139.99\n");
			printf("4-Calcetines.......$84.75\n");
			printf("5-Zapatos........$1150.89\n");
			scanf("%d",&opcion);
			printf("Teclee la cantidad: ");
			scanf("%d",&cantidad);
			switch(opcion)
		{
			case 1: camisa+=cantidad;     break;
			case 2: pantalon+=cantidad;     break;
			case 3: ropa_int+=cantidad;;  break;
			case 4: calcetines+=cantidad;    break;
			case 5: zapatos+=cantidad;      break;
			default: printf("Opcion invalida"); break;
		}
		printf("\nSi desea seguir comprando teclee 1: ");
		scanf("%d",&seguir);
		}while(seguir==1);
		printf("\nTeclee su efectivo: ");
		scanf("%f",&efect);
		system("cls");
		//Operaciones
		///Calcetines
		tot_cam=camisa*CAM;
		vt_cam+=tot_cam;
		///Pantalones
		tot_pant=pantalon*PNT;
		vt_pnt+=tot_pant;
		///Ropa interior
		tot_r_int=ropa_int*R_INT;
		vt_rint+=tot_r_int;
		///Calcetines
		tot_calc=calcetines*CALC;
		vt_calc+=tot_calc;
		///Zapatos
		tot_zap=zapatos*ZAP;
		vt_zap+=tot_zap;
		///Otros calculos
		subt=(tot_cam)+(tot_pant)+(tot_r_int)+(tot_calc)+(tot_zap);
		v_totC+=subt;
		iva=subt*IVA;
		tot=subt+iva;
		tot_v+=tot;
		camb=efect-tot;
		//Impresion a pantalla
	    //////////////////TICKET DE COMPRA////////////////
		printf("            Live to wear             \n");
		printf("          TICKET DE COMPRA           \n");
		printf("Adolfo, Av. Ruiz Cortines 5698, Valle\n");
		printf(" de Infonavit, 64350 Monterrey, N.L. \n");
		printf("         Tel. +52 814 860 134        \n");
		printf("Fecha: "); system("date/t "); printf("Hora:  "); system(" time/t\n");
		printf("--------------------------------------\n");
		printf("  Productos   Cantidad    Total      \n");
		printf("Camisas          %d        %f\n",camisa,tot_cam);
		printf("Pantalones       %d        %f\n",pantalon,tot_pant);
		printf("Ropa interior    %d        %f\n",ropa_int,tot_r_int);
		printf("Calcetines       %d        %f\n",calcetines,tot_calc);
		printf("Zapatos          %d        %f\n",zapatos,tot_zap);
		printf("\n");
		printf("                          ------------\n");
		printf("TOTAL                      %.2f\n",tot);
		printf("\nEfectivo                   %f\n",efect);
		printf("Cambio efectivo            %.2f\n",camb);
		printf("\n");
		printf("SUBTOTAL                   %.2f\n",subt);
		printf("Iva al 16                  %.2f\n",iva);
		printf("TOTAL                      %.2f\n",tot);
		printf("**** I.V.A. INCLUIDO EN EL PRECIO ****\n");
		printf("******   GRACIAS POR SU VISITA   *****\n");
		printf("   ||| || ||||| | |||| |||| || | |||  \n");
		printf("             280817928371087          \n");
		system("pause");
		system("cls");
		//Encuesta
		printf("A continuacion se le apliara una encuesta de satisfaccion al cliente\n");
		printf("¿Como fue tu experiencia en nuestra tienda?\n");
		E_opc(); t_punt+=punt;
		system("cls");
		printf("¿Que tan satisfecho(a) esta con su(s) productos?\n");
		E_opc(); t_punt+=punt;
		system("cls");
		printf("¿Como califica la conducta de nuestros empleados?\n");
		E_opc(); t_punt+=punt;
		system("cls");
		printf("¿Como califica nuestras instalaciones?\n");
		E_opc(); t_punt+=punt;
		system("cls");
		printf("¿Que reseña le daria a un conocido sobre nuestra tienda?\n");
		E_opc(); t_punt+=punt;
		//printf("\n");
		system("cls");
		printf("Su porcentaje de satisfaccion es: %d\n",t_punt*4);
		printf("\nTeclee 1 para que siga la siguiente persona: ");
		scanf("%d",&seguir2);
	}while(seguir2==1);
	printf("Clientes atendidos:          %d\n",client);
	printf("Total de lo vendido:         %.2f\n",tot_v);
	printf("Ventas totales por cliente:  %.2f\n",v_totC);
	printf("VENTAS TOTALES POR PRODUCTO\n");
	printf("Ventas Camisa                %.2f\n",vt_cam);
	printf("Ventas Pantalon              %.2f\n",vt_pnt);
	printf("Ventas Ropa interior         %.2f\n",vt_rint);
	printf("Ventas Calcetines            %.2f\n",vt_calc);
	printf("Ventas Zapatos               %.2f\n",vt_zap);
}
void E_opc()
{
	while(true){
		printf("1) Muy bien\n");
		printf("2) Bien\n");
		printf("3) Masomenos\n");
		printf("4) Mal\n");
		printf("5) Muy mal\n");
		printf("\nEscriba su respuesta: ");
		scanf("%d",&resp);
		if (resp>=1 and resp<=5){
			switch(resp){
				case 1: punt=5; break;
				case 2: punt=4; break;
				case 3: punt=3; break;
				case 4: punt=2; break;
				case 5: punt=1; break;
			}
			break;
		}else{
			printf("Opcion no valida, vuelva a intentar!\n");
		}
	}
}
