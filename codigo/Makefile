# ───────────────────────────────────────────────────────────────
#  MAKEFILE · AUTOMATIZACIÓN DE COMPILACIÓN
# ───────────────────────────────────────────────────────────────
#  Asignatura: Lenguajes de Interfaz en TECNM Campus ITT
#  Autor(a): Torres Moreno Diego Antonio
#  Fecha: 2026/04/16
# ───────────────────────────────────────────────────────────────
#  Descripción:
#  Orquesta la compilación de archivos .c y .S, generando el
#  ejecutable de debug y la librería compartida para Python.
# ───────────────────────────────────────────────────────────────

CC = clang
CFLAGS = -g -O0

all: test_debug libops.so

# Genera el ejecutable para GDB usando main.c y el ASM
test_debug: main.c ops.S
	$(CC) $(CFLAGS) main.c ops.S -o test_debug

# Genera la librería dinámica para Python
libops.so: ops.S
	$(CC) -shared -o libops.so ops.S

# Limpia solo los archivos binarios generados
clean:
	rm -f test_debug libops.so *.o
