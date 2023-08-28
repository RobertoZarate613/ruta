/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Variables para guardar los valores de los dados, la suma y el resultado
    int dado1, dado2, suma, resultado;
    // Variable para guardar la opción del usuario
    char opcion;
    // Variable para guardar el nombre del archivo
    char nombre_archivo[] = "salida.txt";
    // Variable para guardar el archivo
    FILE *archivo;
    // Inicializar la semilla para generar números aleatorios
    srand(time(NULL));
    // Abrir el archivo en modo escritura
    archivo = fopen(nombre_archivo, "w");
    // Comprobar si se pudo abrir el archivo
    if (archivo == NULL) {
        printf("No se pudo abrir el archivo %s\n", nombre_archivo);
        return 1;
    }
    // Imprimir las instrucciones del juego
    printf("Bienvenidos al juego de dados\n");
    printf("Las reglas del juego son las siguientes:\n");
    printf("- Debes lanzar un par de dados.\n");
    printf("- Si la suma de las caras es 8, ganas.\n");
    printf("- Si la suma de las caras es 7, pierdes.\n");
    printf("- Si no ha salido ni 8 ni 7, puedes seguir lanzando.\n");
    printf("- Si sale 8 ganas, pero si en algún otro lanzamiento sale 7, pierdes.\n");
    printf("Listo para jugar ? (S/N)\n");
    // Leer la opción del usuario
    scanf(" %c", &opcion);
    // Comprobar si el usuario quiere jugar
    if (opcion == 'S' || opcion == 's') {
        // Iniciar el juego
        printf("Comenzar el juego\n");
        // Escribir el inicio del juego en el archivo
        fprintf(archivo, "Inicio del juego\n");
        // Generar los valores de los dados
        dado1 = rand() % 6 + 1;
        dado2 = rand() % 6 + 1;
        // Calcular la suma de los dados
        suma = dado1 + dado2;
        // Imprimir los valores de los dados y la suma
        printf("has sacado un %d y un %d. La suma es %d.\n", dado1, dado2, suma);
        // Escribir los valores de los dados y la suma en el archivo
        fprintf(archivo, "has sacado %d y un %d. La suma es %d.\n", dado1, dado2, suma);
        // Comprobar si la suma es 8 o 7
        if (suma == 8) {
            // El usuario ha ganado
            resultado = 1;
        } else if (suma == 7) {
            // El usuario ha perdido
            resultado = -1;
        } else {
            // El juego continúa
            resultado = 0;
        }
        // Mientras el juego no haya terminado
        while (resultado == 0) {
            // Preguntar al usuario si quiere seguir lanzando
            printf("Quieres seguir jugando (S/N)\n");
            // Leer la opción del usuario
            scanf(" %c", &opcion);
            // Comprobar si el usuario quiere seguir lanzando
            if (opcion == 'S' || opcion == 's') {
                // Generar los valores de los dados
                dado1 = rand() % 6 + 1;
                dado2 = rand() % 6 + 1;
                // Calcular la suma de los dados
                suma = dado1 + dado2;
                // Imprimir los valores de los dados y la suma
                printf("has sacado un %d y un %d. La suma es %d.\n", dado1, dado2, suma);
                // Escribir los valores de los dados y la suma en el archivo
                fprintf(archivo, "has sacado un %d y un %d. La suma es %d.\n", dado1, dado2, suma);
                // Comprobar si la suma es 8 o 7
                if (suma == 8) {
                    // El usuario ha ganado
                    resultado = 1;
                } else if (suma == 7) {
                    // El usuario ha perdido
                    resultado = -1;
                } else {
                    // El juego continúa
                    resultado = 0;
                }
            } else {
                // El usuario no quiere seguir lanzando
                printf("Dejar de lanzar.\n");
                // Escribir que el usuario ha dejado de lanzar en el archivo
                fprintf(archivo, "Dejar de lanzar.\n");
                // El juego termina sin resultado
                resultado = 0;
                break;
            }
        }
        // Comprobar el resultado del juego
        if (resultado == 1) {
            // El usuario ha ganado
            printf("Has ganado el juego\n");
            // Escribir que el usuario ha ganado en el archivo
            fprintf(archivo, "Has ganando el juego\n");
        } else if (resultado == -1) {
            // El usuario ha perdido
            printf("Has perdido\n");
            // Escribir que el usuario ha perdido en el archivo
            fprintf(archivo, "Has perdido\n");
        } else {
            // El juego no tiene resultado
            printf("ningun resultado\n");
            // Escribir que el juego no tiene resultado en el archivo
            fprintf(archivo, "ningun resultado.\n");
        }
        // Escribir el fin del juego en el archivo
        fprintf(archivo, "Fin del juego\n");
    } else {
        // El usuario no quiere jugar
        printf("Has dejado de jugar.\n");
    }
    // Cerrar el archivo
    fclose(archivo);
    // Preguntar al usuario si quiere ver el historial de datos
    printf("Ver el historial (S/N)\n");
    // Leer la opción del usuario
    scanf(" %c", &opcion);
    // Comprobar si el usuario quiere ver el historial de datos
    if (opcion == 'S' || opcion == 's') {
        // Abrir el archivo en modo lectura
        archivo = fopen(nombre_archivo, "r");
        // Comprobar si se pudo abrir el archivo
        if (archivo == NULL) {
            printf("No se pudo abrir el archivo %s\n", nombre_archivo);
            return 1;
        }
        // Imprimir el contenido del archivo
        printf("Historial de datos:\n");
        while (!feof(archivo)) {
            printf("%c", fgetc(archivo));
        }
        // Cerrar el archivo
        fclose(archivo);
    } else {
        // El usuario no quiere ver el historial de datos
        printf("No ver el historial. adios\n");
    }
    return 0;
}