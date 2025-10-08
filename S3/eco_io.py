# Programa que pide 3 números y calcula suma, media y mayor
# También guarda el prompt, explicación y adaptación en un archivo de texto

# Pedimos 3 números al usuario con control de errores
numeros = []  # Lista vacía donde guardaremos los números

for i in range(1, 4):  # Repetimos 3 veces
    while True:
        try:
            numero = float(input(f"Introduce el número {i}: "))  # float para permitir decimales
            numeros.append(numero)
            break
        except ValueError:
            print("Error: por favor introduce un número válido.")

# Cálculos principales
suma = sum(numeros)            # Suma de todos los números
media = suma / len(numeros)    # Media = suma entre cantidad
mayor = max(numeros)           # Número mayor de la lista

# Adaptación: mostramos también el menor y los números en orden ascendente
menor = min(numeros)
ordenados = sorted(numeros)

# Mostramos los resultados al usuario
print("\nResultados:")
print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Mayor: {mayor}")
print(f"Menor (adaptación): {menor}")
print(f"Números en orden ascendente (adaptación): {ordenados}")
