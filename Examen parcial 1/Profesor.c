/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

// Constante para el número máximo de materias
#define MAX_MATERIAS 10

// Estructura para almacenar los datos de un estudiante
typedef struct {
    char nombre[50];
    char materias[MAX_MATERIAS][50];
    float notas[MAX_MATERIAS];
    int num_materias;
    float promedio;
} Estudiante;

// Función para calcular el promedio de las notas de un estudiante
float promedio(Estudiante e) {
    int i;
    float sum = 0;
    for (i = 0; i < e.num_materias; i++) {
        sum += e.notas[i];
    }
    return sum / e.num_materias;
}

// Función para mostrar el menú de opciones
void menu() {
    printf("Seleccione una opcion:\n");
    printf("1. Registrar nuevo estudiante y sus notas\n");
    printf("2. Ver historial de notas\n");
    printf("3. Borrar historial de notas\n");
    printf("4. Salir\n");
}

// Función principal del programa
int main() {
    
    // Declaración de variables
    int opcion, i;
    Estudiante estudiante;
    
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
                // Leer los datos del estudiante
                printf("Ingrese el nombre del estudiante:\n");
                scanf("%s", estudiante.nombre);
                printf("Ingrese el numero de materias:\n");
                scanf("%d", &estudiante.num_materias);
                if (estudiante.num_materias > MAX_MATERIAS) {
                    printf("Error: número máximo de materias excedido\n");
                    break;
                }
                for (i = 0; i < estudiante.num_materias; i++) {
                    printf("Ingrese el nombre de la materia %d:\n", i + 1);
                    scanf("%s", estudiante.materias[i]);
                    printf("Ingrese la nota de la materia %d:\n", i + 1);
                    scanf("%f", &estudiante.notas[i]);
                }
                
                // Calcular el promedio del estudiante
                estudiante.promedio = promedio(estudiante);
                
                // Mostrar los resultados en pantalla
                printf("El promedio del estudiante %s es: %.2f\n", estudiante.nombre, estudiante.promedio);
                
                // Escribir los datos en el archivo de texto
                archivo = fopen("salida.txt", "a");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                fprintf(archivo, "Estudiante: %s\n", estudiante.nombre);
                fprintf(archivo, "Materias: ");
                for (i = 0; i < estudiante.num_materias; i++) {
                    fprintf(archivo, "%s ", estudiante.materias[i]);
                }
                fprintf(archivo, "\n");
                fprintf(archivo, "Notas: ");
                for (i = 0; i < estudiante.num_materias; i++) {
                    fprintf(archivo, "%.2f ", estudiante.notas[i]);
                }
                fprintf(archivo, "\n");
                fprintf(archivo, "Promedio: %.2f\n", estudiante.promedio);
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
                // Borrar los datos del archivo de texto
                archivo = fopen("salida.txt", "w");
                if (archivo == NULL) {
                    printf("Error al abrir el archivo\n");
                    break;
                }
                
                // Mostrar un mensaje de confirmación
                printf("El historial de datos ha sido borrado\n");
                
                fclose(archivo);
                
                break;
            
            case 4:
                // Salir del programa
                printf("Cerrar el programa.\n");
                
                break;
            
            default:
                // Opción inválida
                printf("Opción inválida. Intente de nuevo.\n");
                
        }
        
    } while (opcion != 4);
    
    return 0;
}
