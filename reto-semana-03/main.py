import sys

def main():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')   

        # Validar formato
        if len(partes) != 4:
            continue

        producto = partes[1]

        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
            
            # --- LIMPIEZA DE DATOS ---
            # Descartar si el precio es infinito, o si hay valores ilógicos (negativos o ceros)
            if precio == float('inf') or precio == float('-inf') or precio <= 0 or cantidad <= 0:
                continue

        except ValueError:
            continue

        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular promedio
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]
        productos[prod]["promedio"] = ingreso / unidades if unidades > 0 else 0

    # Ordenar por ingreso descendente y en caso de empate, alfabéticamente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: (-x[1]["ingreso"], x[0])
    )

    # Salida
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")

    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")


if __name__ == "__main__":
    main()