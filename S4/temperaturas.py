# Programa que convierte temperaturas de grados Celsius a Kelvin o Fahrenheit.
# También incluye una adaptación para convertir de Fahrenheit o Kelvin a Celsius.

# Pedimos al usuario que elija el tipo de conversión
print("Conversor de temperaturas")
print("1. Celsius a Kelvin")
print("2. Celsius a Fahrenheit")
print("3. Fahrenheit a Celsius")
print("4. Kelvin a Celsius")

# Usamos try/except para controlar errores si el usuario mete texto en vez de números
try:
    opcion = int(input("Elige una opción (1-4): "))

    # Pedimos la temperatura a convertir
    temperatura = float(input("Introduce la temperatura: "))

    # Según la opción elegida, hacemos la conversión
    if opcion == 1:
        resultado = temperatura + 273.15
        print(f"{temperatura} °C son {resultado} K")

    elif opcion == 2:
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura} °C son {resultado} °F")

    # Adaptación: Fahrenheit a Celsius
    elif opcion == 3:
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura} °F son {resultado} °C")

    # Adaptación: Kelvin a Celsius
    elif opcion == 4:
        resultado = temperatura - 273.15
        print(f"{temperatura} K son {resultado} °C")

    else:
        print("Opción no válida. Debes elegir un número del 1 al 4.")

# Si el usuario mete algo que no es un número, mostramos un mensaje
except ValueError:
    print("Error: debes introducir números válidos.")
