/*Problema1*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
int main() { 
    int op, uno, dos; //Las variables que vamos a usar 
    do { 
        printf("---problema 1---\n"); 
        printf("\n¿Que desea hacer?\n"); //Imprimimos las opciones.  
        printf("1) Sumar\n");
        printf("2) Multiplicar\n");
        printf("3) Salir\n");
        scanf("%d",&op); //Ingresa las opccion que eligio

        switch(op) {    //Se ejecuta un bucle
        case 1: //opcion 1 de suma de dos numeros enteros
            printf("\tSumar\n"); 
            printf("Introduzca los numeros a sumar separados por comas\n");
            scanf("%d, %d",&uno, &dos); //Ingresar los dos numeros que se van a sumar
            printf("%d + %d = %d\n", uno, dos, (uno + dos)); //Se Imprime los dos numeros con la respuestas
            break; //Se termina el buque
        case 2: //opcion 2 el producto de dos numeros enteros
            printf("\tMultiplicar\n"); 
            printf("Introduzca los numeros a multiplicar separados por comas\n");
            scanf("%d, %d",&uno, &dos); //Ingresar los dos numeros que se van a multiplicar
            printf("%d * %d = %d\n", uno, dos, (uno * dos)); //Se imprime los dos numeros con la respuesta
            break;//Se termina el buque
        case 3: //opncion 3 se cierra el programa
            printf("\tSalir\n"); 
            break; //Se termina el buque
        default: //Se usa para indicar qué hacer cuando ninguna de las opciones anteriores de un switch se cumple.
            printf("\tOpcion invalida.\n");
        }

    } while (op !=3); //Se ejecuta el programa del bucle hasta elegir la opcion 3

return 0; 
}