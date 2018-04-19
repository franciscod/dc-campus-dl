# Programa
([fuente](https://campus.exactas.uba.ar/course/view.php?id=998&section=1))
---
Programa de Organización del Computador II

A continuación te presentamos el programa de la materia.

### 1\. Introducción

  - Concepto de Computador de Propósito General, y necesidad de un Sistema Operativo.
  - Arquitectura para programación de aplicaciones (Modo Usuario).
  - Arquitectura para programación de sistemas operativos (Modo Kernel).

### 2\. Arquitectura Intel 64

  - Modos de trabajo (Modo Real, Protegido, Virtual 86, y Extensiones de 64 bits).
  - Arquitectura para programación de aplicaciones.
  - Modelos de memoria, modos de direccionamiento y punteros con y sin especificación de segmento.
  - Segmentación.
  - Set de Instrucciones.
  - Modos de Direccionamiento.
  - Ejemplos de uso con algoritmos simples.

### 3\. Ensamblado, vinculación, carga y ejecución

  - Formato de archivos (.o, .exe, .lib, ELF, etc).
  - Estructura del .asm.
  - Información de debugging.

### 4\. Interfase ensamblador-lenguajes de alto nivel

  - Pasaje de parámetros.
  - Estructuras de datos y de control.
  - Interfase con el Sistema Operativo.
  - Librerías estáticas, dinámicas y run-times.
  - Programación orientada a objetos y otros paradigmas.

### 5\. Instrucciones Multimedia

  - Modelo de procesamiento SIMD.
  - Implementaciones SIMD en procesadores IA-32.
  - MMX.
  - SSE, SSE2, SSE3, SSE4.
  - Aplicaciones en procesamiento de señales e imágenes.

### 6\. Microarquitectura

  - Pipeline, superpipeling, arquitectura Superescalar, Paralelismo a Nivel de Instrucciones.
  - Modelo de Ejecución fuera de orden.
  - Modelo VLIW.
  - Modelo EPIC.
  - Ejemplos del mundo real, y comparación entre las diferentes alternativas.
  - Memoria Cache. Principio de funcionamiento. Modelo asociativo.
  - Multicore.
  - Microarquitecturas de los procesadores IA-32: P5, P6, NetBurst, Pentium D, Core.

### 7\. Modelo de programación de Sistemas Operativos - Manejo de Memoria

  - Unidad de Gestión de Memoria de procesadores IA-32.
  - Unidad de Segmentación en Modo Protegido.
  - Unidad de Paginación.
  - Relación con el sistema operativo. Soporte para implementación del Administrador de Memoria Virtual. Memoria compartida entre procesos y entre procesos y el sistema operativo.

### 8\. Modelo de programación de Sistemas Operativos - Interrupciones y
Excepciones

  - Sistema de interrupciones de los procesadores IA-32.
  - Concepto y diferencias entre interrupciones y excepciones.
  - Descriptores asociados. Códigos de error.
  - Interrupciones y Excepciones predeterminadas.
  - Manejo de Interrupciones desde el Sistema Operativo.

### 9\. Modelo de programación de Sistemas Operativos - Protección

  - Sistema de protección en procesadores IA-32.
  - Niveles de privilegio (Anillos de protección).
  - Reglas de protección, para instrucciones, segmentos, páginas, tareas.
  - Relación con el Sistema Operativo: Ejecución en Modo User y en Modo Kernel.
  - Mecanismos para elevar el nivel de privilegio de una tarea (o proceso).

### 10\. Modelo de programación de Sistemas Operativos - Manejo de Tareas

  - Concepto de Multitasking.
  - Contexto de ejecución.
  - Conmutación de tareas en procesadores IA-32.
  - Estructuras y descriptores asociados en procesadores IA-32.
  - Relación de estos recursos con el Sistema Operativo.
  - Scheduling de tareas. Diferentes alternativas.

### 11\. Optimización

  - Técnicas de codificación para optimizar el uso del controlador cache.
  - Técnicas de codificación para optimizar el uso de memoria.
  - Técnicas de codificación para optimizar el aprovechamiento de los recursos de microarquitectura.
  - Técnicas de prefetch en cache.
  - Threading.
  - Optimización en procesadores multicore.

