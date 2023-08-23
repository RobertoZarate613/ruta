/*Problema7*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n; 
    int factorial = 1; 
    printf("---Poblema 7---\n"); 
    printf("Ingrese un numero:\n");
    scanf("%d", &n); //Ingresar el numero
    if(n<0){  //si el numero es negativo
        printf("El factorial no esta definido para numeros negativos.\n");
        } 
    else { //si el numero es positivo o cero
        for (int i= 1; i <=n; i++){ //desde 1 hasta n
            factorial = factorial *i;  //multiplicar el factorial por 1
          }  
          printf("El factorial de %d es: %d\n", n, factorial);
        }   
return 0;
}   