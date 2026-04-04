#!/usr/bin/env python3

from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario

ARCHIVO_INVENTARIO = "data/inventario.csv"

def crear_productos(datos_raw):
    productos = []
    
    for datos in datos_raw:
        es_valido, error = validar_producto(
            datos.get('sku'),
            datos.get('nombre'),
            datos.get('categoria'),
            datos.get('precio'),
            datos.get('stock'),
            datos.get('stock_minimo')
        )
        
        if not es_valido:
            print(f"Advertencia: {error}")
            continue
        
        producto = Producto(
            sku=datos['sku'],
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=float(datos['precio']),
            stock=int(datos['stock']),
            stock_minimo=int(datos['stock_minimo'])
        )
        productos.append(producto)
    
    return productos

def main():
    print("Sistema de Inventario")

    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    productos = crear_productos(datos_raw)

    print(f"Productos validos: {len(productos)}")

if __name__ == "__main__":
    main()