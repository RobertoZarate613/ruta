/*Problema15*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void encriptar(char* mensaje, int desplazamiento) { // Función para encriptar el mensaje
    int i;
    char letra;

    for(i = 0; mensaje[i] != '\0'; ++i){
        letra = mensaje[i];

        if(letra >= 'A' && letra <= 'Z'){ // Encripta las letras mayúsculas
            letra = letra + desplazamiento; 

            if(letra > 'Z'){
                letra = letra - 'Z' + 'A' - 1;
            }

            mensaje[i] = letra;
        }
    }
}

int main() {
    char mensaje[100];
    int desplazamiento;
    printf("---Poblema 15---\n");
    printf("Introduce un mensaje de texto en mayusculas:\n");
    fgets(mensaje, sizeof(mensaje), stdin);

    printf("introduce un numero fijo de desplazamiento:\n ");
    scanf("%d", &desplazamiento);
    encriptar(mensaje, desplazamiento);

    printf("Mensaje Incriptado: %s", mensaje);

    return 0;
}