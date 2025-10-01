# Programa en Python para pedir el nombre y año de nacimiento
# Luego calcula la edad y clasifica en un tramo de edad
# También controla errores si el usuario no mete un número

# Importamos la librería datetime para saber el año actual
import datetime  

# Pedimos el nombre al usuario
nombre = input("Por favor, dime tu nombre: ")

# Usamos un bucle while para asegurarnos de que el año sea un número correcto
while True:
    try:
        # Pedimos el año de nacimiento y lo convertimos a número entero
        anio_nacimiento = int(input("¿En qué año naciste? "))

        # Si la conversión funciona, salimos del bucle con 'break'
        break
    except ValueError:
        # Si mete algo que no es un número, mostramos un mensaje y repetimos
        print("Error: debes introducir un número válido para el año.")

# Obtenemos el año actual usando datetime
anio_actual = datetime.datetime.now().year  

# Calculamos la edad restando el año actual menos el de nacimiento
edad = anio_actual - anio_nacimiento

# Mostramos el resultado al usuario
print(f"\nHola {nombre}, tienes {edad} años.")

# Clasificamos la edad en tramos
if edad < 18:
    print("Eres menor de edad.")
elif edad <= 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
