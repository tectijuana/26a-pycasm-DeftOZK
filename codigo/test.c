// ---------------------------------------------------------------
//  WRAPPER C · PUENTE HACIA ARM64
// ----------------------------------------------------------------
// Asignatura: Lenguajes de Interfaz en TECNM Campus ITT
//  Autor(a): Torres Moreno Diego Antonio
//  Fecha: 2026/04/16
// -----------------------------------------------------------------
// Descripción:
// Interfaz en C que conecta funciones Assembly (.S)
// con Python, permitiendo su invocación externa.
// -----------------------------------------------------------------

#include <stdio.h>

// Prototipos de las funciones que están en ops.S (Ensamblador)
// Usamos long long para asegurar 64 bits en el resultado de la suma
extern long long sum_array(int* arr, int n);
extern int add(int a, int b);

// Esta función sirve para demostrar que Python puede llamar a C
// y C puede imprimir texto antes o después de usar el Ensamblador.
void interface_log() {
    printf("[C Interface] Preparando llamada a rutinas ARM64...\n");
}

