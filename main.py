import sys

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def clasificar(c):
    if c < 0:
        return "Congelante"
    elif c <= 15:
        return "Frio"
    elif c <= 25:
        return "Templado"
    elif c <= 35:
        return "Calido"
    else:
        return "Extremo"

def procesar_linea(linea):
    partes = linea.strip().split(',')

    if len(partes) != 3:
        return None

    ciudad = partes[0].strip()
    temp_str = partes[1].strip()
    unidad = partes[2].strip().upper()

    if unidad not in ['C', 'F']:
        return None

    try:
        temp = float(temp_str)
    except:
        return None
    # Convertir a Celsius
    if unidad == 'F':
        celsius = fahrenheit_a_celsius(temp)
    else:
        celsius = temp
    # Clasificar
    clasificacion = clasificar(celsius)

    return ciudad, celsius, clasificacion


