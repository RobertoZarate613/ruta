/*Problema6*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>

int main() {
int inicio, fin;
int contador=0;
printf("ingrese el numero Inicial:\n");
scanf("%d", &inicio); //Ingresar el numero inicial
printf("ingrese el numero Final:\n");
scanf("%d", &fin); //ingresar el numero final 
for(int i = inicio; i<=fin; i++){ //Ciclo que empieza
    if(i % 2 == 0){ //si el numero es par
        contador++; //Incrementar el contador
}
}
printf("La cantidad de numeros pares en el rango [%d, %d] es: %d\n", inicio, fin, contador);
return 0;
}   