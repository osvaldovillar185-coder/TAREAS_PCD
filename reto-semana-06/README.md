# Reto Semana 6 — Validador de Códigos con Expresiones Regulares

**Programación para Ciencia de Datos** | IPN | Semestre Febrero-Julio 2026

---

## Descripción

Validador automático de códigos de una empresa de logística. Lee códigos desde `stdin`, detecta su tipo y valida su formato usando expresiones regulares. Escribe los resultados como CSV a `stdout`.

## Formatos Soportados

| Tipo | Formato | Ejemplo válido |
|------|---------|----------------|
| Producto | `AAA-NNNN-XX` | `TEC-0001-MX` |
| Envío | `ENV-YYYY-MM-DD-NNNNNN` | `ENV-2024-03-15-001234` |
| Empleado | `EMP-DEP-NNNN` | `EMP-VEN-1234` |
| Factura | `FAC-S-NNNNNN` | `FAC-A-123456` |

## Uso

```bash
python main.py < codigos.txt > salida.txt
```

## Ejemplo

Entrada:
```
TEC-0001-MX
tec-0001-MX
ENV-2024-03-15-001234
EMP-VEN-0123
XXX-1234
```

Salida:
```
codigo,tipo,valido
TEC-0001-MX,producto,VALIDO
tec-0001-MX,producto,INVALIDO
ENV-2024-03-15-001234,envio,VALIDO
EMP-VEN-0123,empleado,INVALIDO
XXX-1234,desconocido,INVALIDO
```

## Estructura del Proyecto

```
reto-semana-06/
├── README.md
├── main.py
└── tests/
    ├── codigos.txt
    └── salida_esperada.txt
```

## Verificar Salida

```bash
python main.py < tests/codigos.txt > mi_salida.txt
diff mi_salida.txt tests/salida_esperada.txt
```

Sin diferencias = correcto.