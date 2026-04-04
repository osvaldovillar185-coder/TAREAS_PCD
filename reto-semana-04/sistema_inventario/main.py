#!/usr/bin/env python3

from utils.io import leer_inventario

ARCHIVO_INVENTARIO = "data/inventario.csv"

def main():
    print("Sistema de Inventario")

    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    print(f"Registros leidos: {len(datos_raw)}")

if __name__ == "__main__":
    main()