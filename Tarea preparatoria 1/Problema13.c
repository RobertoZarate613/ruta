/*Problema13*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
    int numero;
    
    printf("---Poblema 13---\n");
    printf("Introduce un numero:\n");;
    scanf("%d", &numero);

    if(numero %2 ==0) {
    printf("El numero %d es par.\n", numero); 
    } else {
        printf("El numero %d es impar.\n", numero);
    }
return 0;
}