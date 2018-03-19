# Inicio
([fuente](https://campus.exactas.uba.ar/course/view.php?id=1017))
---
### Inicio

El análisis estático permite extraer propiedades sobre un programa antes de la
ejecución real del mismo. Esta información puede ser luego utilizada para
realizar transformaciones sobre el mismo (compilación, optimizaciones, etc.)
y/o realizar pruebas sobre su corrección.

## En este curso...

Introduciremos las técnicas y conceptos básicos del análisis estático de
código y sus principales aplicaciones. En particular se estudiará como estas
técnicas se aplican a la verificación automática de software.

![01s](http://www.dc.uba.ar/materias/aap/2015/c1/01s.gif)

## ¿Qué es el análisis de programas?

  - Técnicas que toman el código (fuente, bytecode o asm),como input y razona e infiere propiedades sobre el mismo.
  - Puede ser estático (sin ejecutar), dinámico (ejecutando realmente el programa), híbrido
  - Puede ser sobreaproximado o. subaproximado. O preciso
  - No computable en general.
  - Trade-off: tiempo / memoria / decidibilidad / precisión

## ¿Para qué sirve?

  - Generación de código: Compilación, optimización, transformación…
  - Verificación: Chequear contratos, buscar bugs, generar casos de test…
  - Comprensión: Obtener invariantes, obtener modelos, ingeniería reversa…
  - Seguridad: Buffer overflows, information flow…

Esta es la materia antiguamente conocida como **Análisis y Síntensis
Automático de Programas**

  - [![Foro](https://campus.exactas.uba.ar/theme/image.php/magazine/forum/1462913092/icon) Novedades Foro](https://campus.exactas.uba.ar/mod/forum/view.php?id=52573)

