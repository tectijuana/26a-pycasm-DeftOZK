# ───────────────────────────────────────────────
#  INTERFAZ PYTHON · PROFILING AVANZADO
# ───────────────────────────────────────────────
#  Asignatura: Lenguajes de Interfaz en TECNM Campus ITT
#  Autor(a): Torres Moreno Diego Antonio
#  Fecha: 2026/04/15
# ───────────────────────────────────────────────
#  Descripción: Prueba de rendimiento real usando sum_array.
# ───────────────────────────────────────────────

import ctypes
import time

# Cargar la libreria
lib = ctypes.CDLL("./libops.so")

# Configurar firma de sum_array: int* arr, int n -> retorna long
lib.sum_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_long]
lib.sum_array.restype = ctypes.c_long

def benchmark_array():
    N = 10000000 # 10 millones de números
    print(f"\n--- Prueba de Rendimiento Real ({N} elementos) ---")
    
    # 1. Preparar datos (Este tiempo no se cuenta en la carrera)
    print("Generando datos en memoria...")
    py_list = list(range(N))
    c_array = (ctypes.c_int * N)(*py_list)
    
    # 2. Medir Ensamblador (ARM64)
    print("Calculando suma en Ensamblador...")
    start_asm = time.time()
    res_asm = lib.sum_array(c_array, N)
    end_asm = time.time()
    
    # 3. Medir Python nativo
    print("Calculando suma en Python...")
    start_py = time.time()
    res_py = sum(py_list)
    end_py = time.time()
    
    # 4. Mostrar Resultados
    print("\n--- RESULTADOS FINALES ---")
    print(f"Suma correcta: {res_py}")
    print(f"Tiempo total en ASM:    {end_asm - start_asm:.6f} segundos")
    print(f"Tiempo total en Python: {end_py - start_py:.6f} segundos")
    
    tiempo_asm = end_asm - start_asm
    tiempo_py = end_py - start_py
    if tiempo_asm < tiempo_py:
        print(f"\n🚀 ¡ÉXITO! Ensamblador fue {tiempo_py / tiempo_asm:.2f} veces más rápido.")

benchmark_array()
