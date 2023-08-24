/*Problema9*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
  int n, c; 
  int a = 0; 
  int b = 1; 
  printf("Ingrese el número de términos:\n");
  scanf("%d", &n); //Ingresar el numero de terminos
  printf("Los primeros %d términos de la serie de Fibonacci son:\n", n);
  for (int i = 0; i < n; i++) { // El ciclo
    printf("%d ", a); // mostrar el término actual
    c = a + b; // calcular el siguiente término como la suma de los dos anteriores
    a = b; // actualizar el primer término con el segundo
    b = c; // actualizar el segundo término con el siguiente
  }
  printf("\n");
  return 0;
}