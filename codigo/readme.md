# Reporte Técnico: Integración Python + C + ARM64 Assembly

## Autor
* **Nombre:** Torres Moreno Diego Antonio
* **Matrícula:** 23212077
* **Asignatura:** Lenguajes de Interfaz
* **Institución:** TECNM Campus ITT
* **Fecha:** 16 de abril de 2026

---

## 1. Introducción
**¿Qué es ARM64?**
ARM64 (o AArch64) es la arquitectura de 64 bits de los procesadores ARM, diseñados bajo la filosofía RISC (Reduced Instruction Set Computer). Es la arquitectura predominante en dispositivos móviles, sistemas embebidos (como Raspberry Pi) y servidores modernos de alta eficiencia energética.

**¿Por qué usar Assembly?**
Aunque los lenguajes de alto nivel facilitan el desarrollo, el uso de Assembly (Ensamblador) es fundamental para optimizar cuellos de botella críticos donde cada ciclo de reloj cuenta. 👉 *Además, el ensamblador ayuda a entender cómo funciona la computadora a nivel de hardware, dándonos control absoluto sobre los registros y la memoria.*

---

## 2. Marco Teórico
* **Arquitectura ARM:** Se basa en instrucciones de tamaño fijo (32 bits para la instrucción en sí) que operan principalmente sobre registros (arquitectura Load/Store), minimizando el acceso directo a la RAM para acelerar los cálculos.
  
* **Registros (x0–x30):** ARM64 cuenta con 31 registros de propósito general de 64 bits. Para este proyecto, los registros `x0` a `x7` son vitales, ya que se utilizan para recibir los argumentos de las funciones y `x0` se usa para devolver el resultado.
  
* **ABI (Application Binary Interface):** Es el conjunto de reglas que define cómo se comunican los programas a nivel de máquina. Define la convención de llamadas, es decir, qué lenguaje o función se encarga de limpiar la pila y en qué registros deben ir los datos para que C y Python entiendan lo que hizo Assembly.

---

## 3. Desarrollo
El proyecto se dividió en tres capas principales:

1. **Python (`app.py`):** Es la interfaz de alto nivel. Utilizamos la librería `ctypes` para cargar el binario compartido (`.so`). Este script genera grandes volúmenes de datos (arreglos), invoca las funciones de bajo nivel y mide el tiempo de ejecución para la comparativa.
2. **C (`test.c` y `main.c`):** Actúa como el puente o *Wrapper*. Declara las funciones externas con la firma de C (ej. `extern long sum_array(int* arr, int n);`) para que el sistema operativo y Python puedan enlazarlas con el código binario sin errores de segmentación.
3. **Assembly (`ops.S`):** Es el motor lógico. Aquí se escribieron las rutinas puras operando directamente sobre los registros `x0-x7`, implementando loops controlados y operaciones matemáticas nativas como `ADD`, `SUB`, `MUL` y el uso de `CSEL` para comparaciones eficientes.

---

## 4. Resultados
Se realizó una prueba de ejecución procesando arreglos y cálculos repetitivos. Los tiempos obtenidos fueron los siguientes:

| Método | Tiempo de Ejecución | Optimización |
| :--- | :--- | :--- |
| **Python** | 0.105969 ms | Base (Interpretado) |
| **C** | 0.045210 ms | Media (Compilado) |
| **ASM** | **0.015731 ms** | **Máxima (Nativo)** |

---

## 5. Análisis
* **ASM más rápido en loops:** La ventaja brutal del Ensamblador se debe a que la iteración de los arreglos se realiza manteniendo los contadores y las sumatorias directamente en los registros del CPU (`x0`, `x1`, etc.), evitando viajes costosos a la memoria RAM.
* **Overhead de Python:** Python registra el tiempo más lento porque es interpretado. En cada iteración del bucle, la máquina virtual de Python debe verificar los tipos de datos de forma dinámica y realizar operaciones de gestión de memoria (*garbage collection*), lo que genera un "overhead" masivo.

---

## 6. Conclusiones
* **¿Cuándo usar ASM?** Creo que debe utilizarse exclusivamente en sistemas críticos de tiempo real, drivers de hardware, o en funciones específicas de software que representan un cuello de botella masivo (como procesamiento de imágenes, criptografía o IA).
* **Ventajas:** Rendimiento insuperable, control absoluto del hardware y ejecución determinista.
* **Desventajas:** Código muy largo y difícil de mantener, no es portable a otras arquitecturas (el código ARM64 no corre en Intel x86) y requiere un conocimiento profundo de la máquina para no causar errores fatales del sistema.

---

### 7. Evidencias

**1. Compilación del proyecto (`make`):**


<img width="1054" height="91" alt="image" src="https://github.com/user-attachments/assets/2fc995e8-1ff8-4b11-bd81-e67594f15f8f" />

---

**2. Ejecución Python (`app.py` con tiempos):**


<img width="504" height="277" alt="image" src="https://github.com/user-attachments/assets/3099521a-9e7d-4fd0-95e5-81434c5b5c21" />

---

**3. Uso de GDB:**
*(Ejecutando GDB para inspeccionar el flujo y la memoria)*


<img width="820" height="313" alt="image" src="https://github.com/user-attachments/assets/8ac446be-518e-4c17-b121-12563f03800a" />

---

**4. Inspección de Registros (`info registers`):**


<img width="481" height="108" alt="image" src="https://github.com/user-attachments/assets/06fefa08-9943-442b-8ccf-d6932d7f4758" />

---

**5. Desensamblado (`disassemble main` o `disassemble add`):**


<img width="732" height="158" alt="image" src="https://github.com/user-attachments/assets/37463bdf-3bc4-4d76-bb94-0aebab6be6f9" />
