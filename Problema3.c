/*Problema3*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

int main() { 
    char cadena[100]; //Declamramos una variable tipo char que puede almacenar hasta 100 caracteres
    printf("Ingrese una cadena de texto:\n");
    scanf("%s", cadena); //ingresamos el caracter para la cadena
    int longitud = strlen(cadena); //usamos la funcion strlen para obtener la longitud de la cadena
    printf("La cadena ingresada tiene %d caracteres.\n", longitud);//Imprime el resultado
return 0; 
}