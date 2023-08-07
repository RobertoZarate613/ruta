#include <stdio.h>

int main() {
    int num1, num2;
    char operator;

    printf("Ingrese el primer número: ");
    scanf("%d", &num1);
    printf("Ingrese el segundo número: ");
    scanf("%d", &num2);
    printf("Ingrese el operador (+, -, *, /): ");
    scanf(" %c", &operator);

    double result;

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = (double) num1 / num2;
            break;
        default:
            printf("Operador inválido.");
            return 1;
    }

    printf("El resultado es: %.2f\n", result);

    return 0;
}