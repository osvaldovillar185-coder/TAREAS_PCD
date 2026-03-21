# Clasificador de Temperaturas

**Programación para Ciencia de Datos**
Instituto Politécnico Nacional (IPN)
Semestre Febrero–Julio 2026

---

##  Descripción

Este proyecto implementa un programa en Python que procesa un archivo CSV con temperaturas de distintas ciudades del mundo.

El sistema:

* Convierte temperaturas de Fahrenheit a Celsius
* Clasifica el clima según rangos definidos
* Genera un reporte limpio en formato CSV

---

##  Funcionamiento

El programa:

1. Lee datos desde **stdin**
2. Convierte temperaturas a Celsius si es necesario
3. Clasifica cada temperatura en:

   * Congelante
   * Frío
   * Templado
   * Cálido
   * Extremo
4. Ignora líneas inválidas
5. Imprime resultados en **stdout**

---

##  Formato de Entrada

Archivo CSV con el siguiente formato:

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
```

---

##  Formato de Salida

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
```

---

##  Reglas de Clasificación

| Temperatura (°C) | Clasificación |
| ---------------- | ------------- |
| < 0              | Congelante    |
| 0 – 15           | Frío          |
| 16 – 25          | Templado      |
| 26 – 35          | Cálido        |
| > 35             | Extremo       |

---

##  Pruebas

Los casos de prueba se encuentran en la carpeta:

```
tests/
├── entrada1.txt
└── salida_esperada1.txt
```

---

##  Manejo de Errores

El programa ignora automáticamente:

* Temperaturas no numéricas
* Unidades inválidas
* Líneas con formato incorrecto
* Líneas vacías

---

##  Estructura del Proyecto

```
reto-semana-02/
├── main.py
├── README.md
└── tests/
    ├── entrada1.txt
    └── salida_esperada1.txt
```

---

##  Autor

Osvaldo David Villar
IPN - ESCOM
Licenciatura en Ciencia de Datos

---
