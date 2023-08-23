/*Problema10*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h> // librería para usar funciones matemáticas

int main() {
  int opcion; // variable para almacenar la opción del usuario
  float lado; // variable para el lado del cubo
  float radio; // variable para el radio de la esfera
  float base; // variable para la base de la pirámide
  float altura; // variable para la altura de la pirámide
  float volumen; // variable para el resultado del volumen
  const float PI = 3.14159; // constante para el valor de pi
   printf("---Poblema 10---\n"); 
  printf("Calculadroa de Volumenes.\n");
  printf("Elegir alguna opcion:\n");
  printf("1. calcular el volumen de un cubo.\n");
  printf("2. calcular el volumen de una esfera.\n"); 
  printf("3. calcular el voluemn de una piramide de base triangular.\n");
  printf("4. calcular el volumen de una piramide de base cuadrada.\n");
  scanf("%d", &opcion); // leer la opción del usuario 
  switch (opcion) { // evaluar la opción del usuario
    case 1: // si el usuario eligió la opción 1
      printf("Ingrese el lado del cubo: ");
      scanf("%f", &lado); // leer el lado del cubo
      volumen = lado * lado * lado; // aplicar la fórmula del volumen del cubo
      printf("El volumen del cubo es: %.2f\n", volumen); // mostrar el resultado con dos decimales
      break;
    case 2: // si el usuario eligió la opción 2
      printf("Ingrese el radio de la esfera: ");
      scanf("%f", &radio); // leer el radio de la esfera
      volumen = (4 / 3) * PI * pow(radio, 3); // aplicar la fórmula del volumen de la esfera
      printf("El volumen de la esfera es: %.2f\n", volumen); // mostrar el resultado con dos decimales
      break;
    case 3: // si el usuario eligió la opción 3
      printf("Ingrese la base de la piramide de base triangular: ");
      scanf("%f", &base); // leer la base de la pirámide
      printf("Ingrese la altura de la piramide de base trinagular: ");
      scanf("%f", &altura); // leer la altura de la pirámide
      volumen = (1 / 3) * (base * altura / 2) * altura; // aplicar la fórmula del volumen de la pirámide
      printf("El volumen de la piramide de base triangular es: %.2f\n", volumen); // mostrar el resultado con dos decimales
      break;
    case 4: // si el usuario eligió la opción 4
      printf("Ingrese la base de la piramide de base cuadrada: ");
      scanf("%f", &base); // leer la base de la pirámide
      printf("Ingrese la altura de la piramide de base cuadrada: ");
      scanf("%f", &altura); // leer la altura de la pirámide
      volumen = (1 / 3) * pow(base, 2) * altura; // aplicar la fórmula del volumen de la pirámide
      printf("El volumen de la piramide de base cuadrada es: %.2f\n", volumen); // mostrar el resultado con dos decimales
      break;
    default: // si el usuario no eligió una opción válida
      printf("Opcion no valida.\n");
      break;
  }
  
  return 0;
}