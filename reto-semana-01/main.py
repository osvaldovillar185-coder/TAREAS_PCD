import sys

def clean_value(value):
    ##Quitar espacios y solo permitir los digitos correctos
    value = value.strip()
    valid_chars= '.-0123456789'
    result=''
    ##Recorremos la cadena y si el digito es correcto lo guardamos
    for char in value:
        if char in valid_chars:
            result +=char
    return result

def convert_int (texto):
    ##Si esta vacio entonces devuelve 0
    if texto == "":
        return 0
    ##Se intenta convertir el texto a un numero y si no se puede entonces se devuelve 0
    try:
        number=float(texto)
        return int(number)
    except ValueError:
        return 0
        
##Procesar lineas y hacer la suma de los elementos
def process_line(line):
    line= line.strip()
    if not line:
        return 0
    values = line.split(",")
    suma=0
    for value in values :
        clean=clean_value(value)
        number = convert_int(clean)
        suma = suma+number
    return suma

def main():
    for line in sys.stdin:
        result = process_line(line)
        print(result)


if __name__ == "__main__":
    main()