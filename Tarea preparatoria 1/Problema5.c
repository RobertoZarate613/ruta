/*Problema5*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
int main() { 
    char opcion;
    float temperatura;
     while (1) { 
        printf("\n------------------------------\n");
        printf("Seleccione la Conversion:\n");
        printf("1. Celsius a Fahrenheit\n");
        printf("2. Fahrenheit a Celsius\n");
        printf("3. Cerrar el prgrama\n");
        scanf("%c", &opcion);

        switch (opcion) {
            case '1':  
                printf("Ingrese la temperatura en grados Celsius:");
                scanf("%f", &temperatura);
                float fahrenheit = (temperatura * 9 / 5)+32;
                printf("%.2f grados Celsius son %.2f grados fahrenheit.", temperatura, fahrenheit);
                break;
            case '2':
                printf("Ingresa la temperatura en grados Fahrenheit:");
                scanf("%f", &temperatura);
                float celsius = (temperatura - 32)*5/9;
                printf("%.2f grados Fahrenheit son %.2f grados Celsius.", temperatura, celsius);
                break;
            case '3':
                printf("Programa cerrado.\n"); 
                return 0;
            default: 
                printf("opcion no valida.\n");
       }
    }
     return 0;
}