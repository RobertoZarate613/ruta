/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

// Función para determinar si un número es primo
int es_primo(int n) {
    int i;
    if (n <= 1) {
        return 0;
    }
    for (i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

// Función para mostrar el menú de opciones
void menu() {
    printf("Seleccione una opcion\n");
    printf("1. Ingresar el numero\n");
    printf("2. Ver el historial de los numeros\n");
    printf("3. Salir\n");
}

// Función principal del programa
int main() {
    
    // Declaración de variables
    int opcion, numero, primo;
    
    // Apertura del archivo de texto
    FILE *archivo;
    
    // Bucle principal del programa
    do {
        
        // Mostrar el menú y leer la opción
        menu();
        scanf("%d", &opcion);
        
        // Ejecutar la opción elegida
        switch (opcion) {
            
            case 1:
                // Leer el número del usuario
                printf("Ingrese el numero:\n");
                scanf("%d", &numero);
                
                // Determinar si el número es primo o compuesto
                primo = es_primo(numero);
                if (primo == 1) {
                    printf("El numero %d es primo\n", numero);
                } else {
                    printf("El numero %d es compuesto\n", numero);
                }
                
                // Escribir los datos en el archivo de texto
                archivo = fopen("salida.txt", "a");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                fprintf(archivo, "Numero: %d\n", numero);
                if (primo == 1) {
                    fprintf(archivo, "Primo: Sí\n");
                } else {
                    fprintf(archivo, "Primo: No\n");
                }
                fclose(archivo);
                
                break;
            
            case 2:
                // Leer los datos del archivo de texto
                archivo = fopen("salida.txt", "r");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                
                // Mostrar el historial de datos en pantalla
                printf("El historial de datos es:\n");
                char linea[100];
                while (fgets(linea, 100, archivo) != NULL) {
                    printf("%s", linea);
                }
                
                fclose(archivo);
                
                break;
            
            case 3:
                // Salir del programa
                printf("Cerrar programa\n");
                
                break;
            
            default:
                // Opción inválida
                printf("Opcion no valida, Ingrese una opcion valida.\n");
                
        }
        
    } while (opcion != 3);
    
    return 0;
}
