// ───────────────────────────────────────────────────────────────
//  PROGRAMA DE PRUEBA (DEBUG) · ENLACE C + ARM64
// ───────────────────────────────────────────────────────────────
//  Asignatura: Lenguajes de Interfaz en TECNM Campus ITT
//  Autor(a): Torres Moreno Diego Antonio
//  Fecha: 2026/04/16
// ───────────────────────────────────────────────────────────────
//  Descripción:
//  Punto de entrada para pruebas de depuración con GDB. 
//  Invoca las funciones de Assembly para validar registros.
// ───────────────────────────────────────────────────────────────

#include <stdio.h>

// Prototipo de la función en Assembly
extern long long sum_array(int* arr, int n);

int main() {
    int datos[] = {10, 20, 30};
    int n = 3;
    
    printf("--- Modo Debug: Iniciando prueba de suma ---\n");
    long long res = sum_array(datos, n);
    printf("Resultado obtenido: %lld\n", res);
    
    return 0;
}
