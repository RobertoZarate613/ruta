/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

// Función para calcular el IVA de un precio
float iva(float precio) {
    return precio * 0.12;
}

// Función para calcular el precio sin IVA
float sin_iva(float precio) {
    return precio - iva(precio);
}

// Función para mostrar el menú de opciones
void menu() {
    printf("Seleccione una opcion:\n");
    printf("1. Ingresar precio\n");
    printf("2. Ver historial de precios\n");
    printf("3. Salir\n");
}

// Función principal del programa
int main() {
    
    // Declaración de variables
    int opcion;
    float precio, iva_precio, sin_iva_precio;
    
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
                // Leer el precio del usuario
                printf("Ingrese el precio en quetzales:\n");
                scanf("%f", &precio);
                
                // Calcular el IVA y el precio sin IVA
                iva_precio = iva(precio);
                sin_iva_precio = sin_iva(precio);
                
                // Mostrar los resultados en pantalla
                printf("El IVA es: %.2f Q\n", iva_precio);
                printf("El precio sin IVA es: %.2f Q\n", sin_iva_precio);
                
                // Escribir los datos en el archivo de texto
                archivo = fopen("salida.txt", "a");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                fprintf(archivo, "Precio: %.2f Q\n", precio);
                fprintf(archivo, "IVA: %.2f Q\n", iva_precio);
                fprintf(archivo, "Sin IVA: %.2f Q\n", sin_iva_precio);
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
                printf("Cerra Programa.\n");
                
                break;
            
            default:
                // Opción inválida
                printf("Opción inválida. Intente de nuevo.\n");
                
        }
        
    } while (opcion != 3);
    
    return 0;
}