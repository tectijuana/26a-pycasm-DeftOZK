# Proyecto: Integración Python + C + ARM64 Assembly

## Autor
* **Nombre:** Torres Moreno Diego Antonio
* **Matrícula:** 23212077
* **Asignatura:** Lenguajes de Interfaz
* **Institución:** TECNM Campus ITT
* **Fecha:** 16 de abril de 2026

---

## Descripción
Este proyecto implementa una librería de alto rendimiento desarrollada en **ARM64 Assembly**, integrada con **Python** a través de un puente en **C** utilizando la librería `ctypes`. El enfoque principal es el análisis de la eficiencia computacional al ejecutar procesos críticos directamente en el hardware.

## Objetivo
Demostrar la interoperabilidad entre lenguajes de alto y bajo nivel, analizando el impacto del uso de instrucciones nativas en el rendimiento del sistema mediante una comparativa empírica.

---


## Evidencia de Ejecución
Enlace para ver la grabación del flujo completo en **asciinema**:
> **[Ver demostración en asciinema](https://asciinema.org/a/AvnXnN8Aw1NkKBQV)**

## Tecnologías y Herramientas
* **Lenguajes:** Python 3, C (Clang), ARM64 Assembly (AArch64)
* **Entorno:** Termux / Linux (ARM64) - Formato binario ELF
* **Depuración:** GDB (GNU Debugger) para inspección de registros (x0-x7)
* **Automatización:** Makefile Profesional

## Funcionalidades
* **Operaciones básicas:** Implementación de suma, resta, multiplicación, máximo y mínimo en nivel de registros.
* **Procesamiento de arreglos:** Rutinas optimizadas para suma de elementos, conteo de números pares y producto punto.
* **Integración Multi-lenguaje:** Uso de una interfaz de puente en C para la invocación de funciones nativas desde un script de Python.

---

## 📁 Estructura del Proyecto
```
26a-pycasm-DeftOZK/
├── codigo/
│   ├── Makefile    
│   ├── app.py 
│   ├── main.c     
│   ├── ops.S
│   └── test.c
└── README.md       
```

## Instalación y Uso

1. Compilación
Genera la librería compartida y el binario de debug:
```make```

3. Ejecución
Corre el análisis de rendimiento:
```python app.py```

3. Depuración (GDB)
```gdb ./test_debug```

## Resultados esperados

| Método | Tiempo de Ejecución | Optimización |
| :--- | :--- | :--- |
| Python | 0.105969 s | Base (Interpretado) |
| C | 0.045210 s | Media (Compilado con Clang) |
| Assembly | 0.015731 s | Máxima (Nativo) |

### Análisis Técnico:

* **Overhead:** Python presenta tiempos mayores debido a la interpretación de bytecode y la gestión dinámica de objetos.
* **Eficiencia ASM:** El uso directo de registros de 64 bits y la reducción de saltos condicionales en los loops permite una ejecución 6.7 veces más rápida que Python en procesamiento de arreglos.

## Conclusiones

Pude validar que el uso de ARM64 Assembly reduce drásticamente los tiempos de ejecución en tareas críticas, permitiendo un control total sobre el hardware. El proyecto me permitió comprender la Application Binary Interface (ABI) de ARM64, específicamente cómo se gestionan los parámetros en los registros x0 a x7. 

## Autorreflexión

El uso de un Makefile profesional me fue de bastante ayuda para automatizar la compilación y evitar errores de enlace manual. La integración de GDB fue fundamental para validar que los valores en los registros coincidieran con los resultados esperados antes de pasar a la fase de Python.
