# Programa para enseñar números binarios en Python

def decimal_a_binario(numero):
    return bin(numero)[2:]  # bin() devuelve '0b...' y quitamos el prefijo

def binario_a_decimal(binario):
    return int(binario, 2)  # int() con base 2 convierte de binario a decimal

def mostrar_conversiones():
    print("\n=== Conversión de Decimal a Binario ===")
    for i in range(1, 11):
        print(f"{i} en binario es {decimal_a_binario(i)}")

def juego_binario():
    import random
    print("\n=== Juego de Binarios ===")
    for _ in range(5):
        numero = random.randint(1, 20)
        respuesta = input(f"¿Cuál es el número binario de {numero}? ")
        if respuesta == decimal_a_binario(numero):
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era {decimal_a_binario(numero)}")

def juego_decimal():
    import random
    print("\n=== Juego de Decimales ===")
    for _ in range(5):
        numero = random.randint(1, 20)
        binario = decimal_a_binario(numero)
        respuesta = input(f"El número binario {binario} corresponde a qué número decimal? ")
        if respuesta.isdigit() and int(respuesta) == numero:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era {numero}")

# Programa principal
print("=== Aprende Números Binarios con Python ===")
mostrar_conversiones()
juego_binario()
juego_decimal()

print("\n¡Gracias por jugar y aprender!")
