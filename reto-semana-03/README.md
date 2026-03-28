#  Reto Semana 3: Analizador de Ventas

##  Descripción

Este programa procesa un archivo CSV con transacciones de ventas y genera un **reporte consolidado por producto**.

El análisis incluye:

* Total de unidades vendidas por producto
* Ingreso total por producto
* Precio promedio de venta
* Ordenamiento por productos más rentables

---

##  Funcionamiento

El programa:

1. Lee datos desde **stdin**
2. Agrupa las transacciones por producto usando diccionarios
3. Calcula métricas:

   * Unidades vendidas
   * Ingreso total
   * Precio promedio
4. Ordena los resultados por ingreso total (descendente)
5. Imprime un CSV como salida

---

## Formato de Entrada

Archivo CSV con el siguiente formato:

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
```


---

##  Formato de Salida

```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
```

---

##  Ejecución

### Ejecutar con archivo de entrada:

```bash
python main.py < entrada.txt
```

### Guardar salida en archivo:

```bash
python main.py < entrada.txt > salida.txt
```

---

## Estructura del Proyecto

```
reto-semana-03/
├── main.py
├── README.md
├──.gitignore
└── tests
    ├── entrada.txt
    ├── salida.txt

```

---

##  Manejo de Errores

El programa ignora automáticamente:

* Líneas con formato incorrecto
* Valores no numéricos
* Líneas incompletas

---


---

## Autor

**Osvaldo David**
Instituto Politécnico Nacional - ESCOM
Licenciatura en Ciencia de Datos

---

##  Notas

* Los valores monetarios se muestran con **2 decimales**
* El programa está diseñado para trabajar con grandes volúmenes de datos
* Se prioriza eficiencia y claridad del código
---
