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

