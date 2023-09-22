#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>
#include <time.h> 
 
// Función para generar una contraseña aleatoria 
void generarContrasena(char *contrasena, int longitud) { 
    const char caracteres[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?"; 
    int numCaracteres = sizeof(caracteres) - 1; 
 
    srand(time(NULL)); 
 
    for (int i = 0; i < longitud; i++) { 
        int indice = rand() % numCaracteres; 
        contrasena[i] = caracteres[indice]; 
    } 
 
    contrasena[longitud] = '\0'; 
} 
 
int main() { 
    int longitudMinima = 12; 
    char contrasena[longitudMinima + 1]; 
 
    do { 
        generarContrasena(contrasena, longitudMinima); 
    } while (strlen(contrasena) < longitudMinima); 
 
    printf("Contrasena generada: %s\n", contrasena); 
 
    return 0; 
}