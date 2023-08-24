/*Problema2*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
  int numero; // El número del que se quiere mostrar la tabla de multiplicar
  printf("Ingresa el numero para la tabla de Multiplicar:\n");
  scanf("%d", &numero); //El numero que se va ingresar
  printf("La tabla de multiplicar del %d es:\n", numero); // muestra el mensaje con el número ingresado
  for (int i = 1; i <= 10; i++) { //Un bucle que va desde 1 hasta 10, que son los factores de la tabla de multiplicar
    int producto = numero * i; //Calcula el producto del número por el factor i
    printf("%d x %d = %d\n", numero, i, producto); //Muestra el resultado de la multiplicación
  }
  return 0;
}