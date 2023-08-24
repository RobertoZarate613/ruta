/*Problema10*/
/*Nombre: Julio Roberto Zarate Lopez*/
/*Carnet: 202300868*/
/*CUI: 2997331650101*/
#include <stdio.h>
#include <stdlib.h>
#include <iostream> 
#include <vector>

// Función para eliminar duplicados
std::vector<int> eliminarDuplicados(std::vector<int> arr) {
    std::vector<int> resultado;
    std::vector<bool> visitado(1001, false); // Asume que los números en la matriz son menores que 1001

    for (int i = 0; i < arr.size(); i++) {
        if (!visitado[arr[i]]) {
            visitado[arr[i]] = true;
            resultado.push_back(arr[i]);
        }
    }

    return resultado;
}

int main() {
    std::vector<int> arr = {1, 3, 8, 8, 2, 3, 4, 1}; // Cambia esto a la matriz que quieras
    std::vector<int> resultado = eliminarDuplicados(arr);

    printf("Matriz sin duplicados: ");
    for (int i = 0; i < resultado.size(); i++) {
        printf("%d ", resultado[i]);
    }

    return 0;
}