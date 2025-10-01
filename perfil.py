# Programa en Python para pedir el nombre y año de nacimiento
# Calcula la edad, clasifica por tramo y añade una adaptación libre:
# muestra en qué década nació el usuario.

import datetime  # Para trabajar con fechas

# Pedimos el nombre
nombre = input("Por favor, dime tu nombre: ")

# Bucle para asegurarnos de que el año de nacimiento sea un número válido
while True:
    try:
        anio_nacimiento = int(input("¿En qué año naciste? "))
        break
    except ValueError:
        print("Error: debes introducir un número válido para el año.")

# Obtenemos el año actual
anio_actual = datetime.datetime.now().year

# Calculamos la edad
edad = anio_actual - anio_nacimiento

# Mostramos la edad
print(f"\nHola {nombre}, tienes {edad} años.")

# Clasificación por tramos
if edad < 18:
    print("Eres menor de edad.")
elif edad <= 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")

# ----------------------
# ADAPTACIÓN:
# Decir en qué década nació el usuario
decada = (anio_nacimiento // 10) * 10
print(f"Naciste en la década de los {decada}.")
