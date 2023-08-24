/*Problema14*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
    int filas;

    printf("---Poblema 14---\n");
    printf("Introduce el numero de filas:\n"); //Solicita al usuario el numero de filas
    scanf("%d", &filas); //Ingresar en numero de filas

    for (int i = 1; i <= filas; i++) {  //Bucle externo para controlar el numero de filas
        for (int j = 1; j <= i; j++) { //Bucle interno para controlar el numero de asterisco en cada fila
            printf("*");
        }
        printf("\n"); //Imprime una nueva linea al final de cada
    }

    return 0;
}