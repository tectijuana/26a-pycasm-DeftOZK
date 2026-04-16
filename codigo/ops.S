// ───────────────────────────────────────────────
//  LIBRERÍA ARM64 · RUTINAS OPTIMIZADAS
// ───────────────────────────────────────────────
//  Asignatura: Lenguajes de Interfaz en TECNM Campus ITT
//  Autor(a): Torres Moreno Diego Antonio
//  Fecha: 2026/04/15
// ───────────────────────────────────────────────
//  Descripción:
// Rutinas matemáticas optimizadas en Ensamblador 
// ARM64 para integrarse con C y Python.
// ───────────────────────────────────────────────

.text
.global add
add:
    add x0, x0, x1
    ret

.global sub
sub:
    sub x0, x0, x1
    ret

.global mul
mul:
    mul x0, x0, x1
    ret

.global max
max:
    cmp x0, x1
    csel x0, x0, x1, gt
    ret

.global min
min:
    cmp x0, x1
    csel x0, x0, x1, lt
    ret

.global sum_array
    .text
    .p2align 2

sum_array:
    mov x2, 0           // x2 será nuestro acumulador (suma = 0)
    cbz x1, end_loop    // Si el número de elementos (x1) es 0, saltar al final

loop:
    ldr w3, [x0]        // Cargar un entero (32 bits) desde la memoria apuntada por x0
    sxtw x3, w3         // Extender el valor a 64 bits en x3 (para la suma larga)
    add x2, x2, x3      // suma (x2) = suma (x2) + valor actual (x3)
    add x0, x0, 4       // Mover el puntero del arreglo 4 bytes adelante (siguiente entero)
    subs x1, x1, 1      // Restar 1 al contador de elementos (x1--)
    b.ne loop           // Si el contador no es cero, repetir el ciclo

end_loop:
    mov x0, x2          // Mover el resultado final a x0 (el registro de retorno para C)
    ret                 // Regresar al programa principal
