# Perfilador de Datasets - Reto Semana 5

Esta herramienta es un script desarrollado en Python diseñado para analizar archivos en formato CSV y generar reportes detallados sobre la calidad de los datos. El perfilador automatiza la revisión de la estructura del dataset, evaluando los tipos de datos inferidos, contando los valores nulos y verificando la unicidad de los registros.

## Características

* **Análisis Automático:** Lee cualquier archivo CSV estándar y procesa sus columnas.
* **Métricas de Calidad:**
  * Inferencia de tipos de datos por columna (enteros, flotantes, cadenas, etc.).
  * Conteo de valores nulos o celdas vacías.
  * Análisis de unicidad para identificar posibles valores duplicados o claves primarias.
* **Ejecución por Línea de Comandos (CLI):** Permite pasar argumentos dinámicamente para especificar qué archivo analizar y dónde guardar el reporte.
* **Enfoque Estructurado:** Implementado de forma procedural utilizando principalmente la biblioteca estándar de Python, garantizando un código eficiente y fácil de seguir.

## Estructura del Proyecto

reto_semana_5/
├── datos_entrada/      # Directorio para almacenar los archivos CSV a analizar
├── resultados/         # Directorio donde se guardarán los reportes generados
├── perfilador.py       # Código fuente principal de la herramienta
├── requirements.txt    # Lista de dependencias y librerías externas (si aplican)
└── README.md           # Documentación del proyecto
