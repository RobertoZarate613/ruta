/*Problema8*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
    char cadena[100]; 
    char resultado [200]; 
    int r=0;
    printf("---Poblema 8---\n"); 
    printf("Ingrese una cadena:\n");
    scanf("%s", cadena); //Ingresar la cadena
    for(int i=0; i < strlen(cadena); i++){ //caracter de la cadena
        resultado[r]=cadena[i];//copiar el caracter al resultado
        r++;//incrementar el indice del resultado
        resultado[r]=cadena[i];//repetir el caracter en el resultado
        r++;
        }
    resultado[r]= '\0'; //agregar el caracter nulo al final del resutlado
    printf("La cadena resultante es: %s\n", resultado);//imprimir el resultado          
return 0;
}  