# Sistema de Inventario Modular

Sistema desarrollado en Python para gestionar inventario y generar reportes de productos que necesitan reorden, utilizando una arquitectura modular.

---

##  Estructura del proyecto
sistema_inventario/
│
├── data/
│ └── inventario.csv # Datos de entrada
│
├── models/
│ ├── init.py
│ └── producto.py # Clase Producto
│
├── outputs/
│ └── reporte_inventario.csv # Reporte generado
│
├── utils/
│ ├── init.py
│ ├── io.py # Lectura y escritura de archivos
│ └── validators.py # Validaciones de datos
│
├── main.py # Punto de entrada
├── .gitignore
└── README.md


---

## ⚙️ Funcionalidades

- Lectura de inventario desde archivo CSV  
- Validación de datos de productos  
- Creación de objetos `Producto`  
- Identificación de productos que necesitan reorden  
- Ordenamiento por unidades faltantes  
- Generación de reporte en CSV  
- Manejo de registros inválidos  

---

## Lógica del sistema

El flujo principal (`main.py`) sigue estos pasos:

1. Leer datos desde `inventario.csv`  
2. Validar cada registro  
3. Crear objetos `Producto`  
4. Filtrar productos con bajo stock  
5. Ordenar por prioridad (faltantes)  
6. Mostrar resultados en consola  
7. Generar reporte en `outputs/reporte_inventario.csv`  

---

##  Requisitos

- Python 3.x  
- No requiere librerías externas  

---

## Ejecución


```bash
python main.py
 Formato del archivo de entrada

El archivo data/inventario.csv debe contener columnas como:

sku,nombre,categoria,precio,stock,stock_minimo
A001,Teclado,Electrónica,500,10,15
A002,Mouse,Electrónica,200,5,10
 Salida

El sistema genera:

Impresión en consola de productos que necesitan reorden
Archivo: outputs/reporte_inventario.csv

Con los productos ordenados por prioridad.

 Componentes
🔹 Producto (models/producto.py)

Encapsula la lógica del producto:

necesita_reorden()
unidades_faltantes()
🔹 validators.py

Valida:

Campos obligatorios
Tipos de datos
Valores válidos
🔹 io.py

Funciones:

leer_inventario()
escribir_reporte()
 Manejo de errores
Registros inválidos son ignorados
Se muestra advertencia en consola:
Advertencia: Ignorando registro invalido - <error>


Autor: Osvaldo David Guadarrama Villar
Licenciatura en Ciencia de Datos - IPN

Proyecto académico — Sistema de inventario en Python modular.