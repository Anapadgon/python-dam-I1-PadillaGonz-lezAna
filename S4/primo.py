# Programa que recibe un número y dice si es primo o no.
# Ampliación S3: Menú para repetir cálculos hasta salir.
# Adaptación: mostrar todos los divisores del número.

while True:  # Bucle principal para repetir cálculos
    try:
        # Pedimos un número al usuario
        numero = int(input("Introduce un número entero: "))

        # Inicializamos lista de divisores
        lista_divisores = []

        # Comprobamos si es primo
        if numero < 2:
            print(f"{numero} no es un número primo.")
            lista_divisores = [numero]
        else:
            divisores = 0
            for i in range(1, numero + 1):
                if numero % i == 0:
                    divisores += 1
                    lista_divisores.append(i)  # Guardamos divisor (adaptación libre)

            if divisores == 2:
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")

        # Mostrar todos los divisores (adaptación libre)
        print(f"Divisores de {numero}: {lista_divisores}")

    except ValueError:
        print("Error: debes introducir un número entero válido.")

    # Menú para repetir o salir (ampliación S3)
    repetir = input("\n¿Quieres probar otro número? (s/n): ")
    if repetir.lower() != "s":
        print("¡Hasta luego!")
        break
