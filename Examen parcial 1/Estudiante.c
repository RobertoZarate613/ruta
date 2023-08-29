/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

// Función para ordenar un arreglo de forma ascendente
void ordenar(float arr[], int n) {
    int i, j;
    float temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Función para calcular la media de un arreglo
float media(float arr[], int n) {
    int i;
    float sum = 0;
    for (i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum / n;
}

// Función para calcular la mediana de un arreglo
float mediana(float arr[], int n) {
    ordenar(arr, n);
    if (n % 2 == 0) {
        return (arr[n / 2] + arr[n / 2 - 1]) / 2;
    } else {
        return arr[n / 2];
    }
}

// Función para calcular la moda de un arreglo
float moda(float arr[], int n) {
    ordenar(arr, n);
    int i, count = 1, max_count = 0;
    float mode = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] == arr[i - 1]) {
            count++;
        } else {
            count = 1;
        }
        if (count > max_count) {
            max_count = count;
            mode = arr[i];
        }
    }
    return mode;
}

// Función para calcular el rango de un arreglo
float rango(float arr[], int n) {
    ordenar(arr, n);
    return arr[n - 1] - arr[0];
}

// Función para calcular la desviación estándar de un arreglo
float desviacion(float arr[], int n) {
    int i;
    float mean = media(arr, n);
    float sum = 0;
    for (i = 0; i < n; i++) {
        sum += pow(arr[i] - mean, 2);
    }
    return sqrt(sum / n);
}

// Función para calcular la varianza de un arreglo
float varianza(float arr[], int n) {
    return pow(desviacion(arr, n), 2);
}

// Función para mostrar el menú de opciones
void menu() {
    printf("Seleccione una opcion:\n");
    printf("1. Ingresar califricaciones\n");
    printf("2. Ver hisotial de calificaciones\n");
    printf("3. salir\n");
}

// Función principal del programa
int main() {
    
    // Declaración de variables
    int opcion, i, n = 5;
    float calificaciones[n], estadisticos[6];
    
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
                // Leer las calificaciones del usuario
                printf("Ingrese las %d calificaciones:\n", n);
                for (i = 0; i < n; i++) {
                    scanf("%f", &calificaciones[i]);
                }
                
                // Calcular los estadísticos descriptivos
                estadisticos[0] = media(calificaciones, n);
                estadisticos[1] = mediana(calificaciones, n);
                estadisticos[2] = moda(calificaciones, n);
                estadisticos[3] = rango(calificaciones, n);
                estadisticos[4] = desviacion(calificaciones, n);
                estadisticos[5] = varianza(calificaciones, n);
                
                // Mostrar los resultados en pantalla
                printf("Los estadisticos descriptivos son:\n");
                printf("Media: %.2f\n", estadisticos[0]);
                printf("Mediana: %.2f\n", estadisticos[1]);
                printf("Moda: %.2f\n", estadisticos[2]);
                printf("Rango: %.2f\n", estadisticos[3]);
                printf("Desviacion Estandar: %.2f\n", estadisticos[4]);
                printf("Varianza: %.2f\n", estadisticos[5]);
                
                // Escribir los datos en el archivo de texto
                archivo = fopen("salida.txt", "a");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                fprintf(archivo, "Calificaciones: ");
                for (i = 0; i < n; i++) {
                    fprintf(archivo, "%.2f ", calificaciones[i]);
                }
                fprintf(archivo, "\n");
                fprintf(archivo, "Estadisticas: ");
                for (i = 0; i < 6; i++) {
                    fprintf(archivo, "%.2f ", estadisticos[i]);
                }
                fprintf(archivo, "\n");
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
                printf("EL historial de datos\n");
                char linea[100];
                while (fgets(linea, 100, archivo) != NULL) {
                    printf("%s", linea);
                }
                
                fclose(archivo);
                
                break;
            
            case 3:
                // Salir del programa
                printf("programa cerrado\n");
                
                break;
            
            default:
                // Opción inválida
                printf("Opcion no valida, ingrese un valor valido\n");
                
        }
        
    } while (opcion != 3);
    
    return 0;
}
