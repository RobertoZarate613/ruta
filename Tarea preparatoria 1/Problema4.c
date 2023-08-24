/*Problema3*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// Función que calcula el factorial de un número entero
long long factorial(int n) {
  long long f = 1; // Variable que almacena el resultado
  for (int i = 1; i <= n; i++) { // Bucle que multiplica los números desde 1 hasta n
    f = f * i; // Actualiza el resultado
  }
  return f; // Devuelve el resultado
}
// Función que calcula el seno de un ángulo usando la serie de Taylor
double seno(double x, int n) {
  double s = 0; // Variable que almacena el resultado
  for (int i = 0; i < n; i++) { // Bucle que suma los términos de la serie
    s = s + pow(-1, i) / factorial(2 * i + 1) * pow(x, 2 * i + 1); // Actualiza el resultado
  }
  return s; // Devuelve el resultado
}
int main() {
  double x; // Variable que almacena el ángulo en radianes
  int n; // Variable que almacena el número de términos
  printf("Introduzca un angulo en grados:\n "); // Pide al usuario que introduzca un ángulo en grados
  scanf("%lf", &x); // Lee el ángulo en grados
  x = x * M_PI / 180; // Convierte el ángulo a radianes
  printf("Introduzca un numero en terminos:\n "); // Pide al usuario que introduzca un número de términos
  scanf("%d", &n); // Lee el número de términos
  printf("El seno de %.2f grados es %.4f\n", x * 180 / M_PI, seno(x, n)); // Muestra el seno del ángulo usando la función seno
  return 0; // Termina el programa
}