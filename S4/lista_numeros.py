import csv #Librería archivos CSV (guardar datos en forma tabla)

# Programa que pide una lista de números separados por comas.
# Los convierte a float, calcula suma, media, máximo y duplicados.
# Adaptación libre: muestra los números únicos y la lista ordenada.
# Además guarda los resultados en un archivo CSV y permite repetir cálculos.

while True:
    entrada = input("Introduce una lista de números separados por comas: ")

    try:
        # Convertimos la entrada en lista de números
        elementos = entrada.split(",")
        numeros = []

        for x in elementos:
            numero = float(x.strip())
            numeros.append(numero)

        # Cálculos principales
        suma = sum(numeros)
        media = suma / len(numeros)
        maximo = max(numeros)
        duplicados = set([x for x in numeros if numeros.count(x) > 1])
        unicos = set(numeros)
        ordenados = sorted(numeros)

        # Mostramos resultados
        print("\n--- RESULTADOS ---")
        print(f"Números introducidos: {numeros}")
        print(f"Suma: {suma}")
        print(f"Media: {media}")
        print(f"Máximo: {maximo}")
        print(f"Duplicados: {duplicados if duplicados else 'No hay duplicados'}")
        print(f"Números únicos: {unicos}")
        print(f"Lista ordenada: {ordenados}")

        # Guardar resultados en CSV

        #Al utilizar append(a) significa que al abrir el archivo no borra lo que estaba antes, sino que añade nuevas filas al final
        with open("resultados_lista.csv", "a", newline="") as f: 
            writer = csv.writer(f) #Crear objeto writer que permite escribir filas en el CSV
            #Guarda los resultados en columnas separadas
            writer.writerow([numeros, suma, media, maximo, list(duplicados), list(unicos), ordenados])

    except ValueError:
        print("Error: asegúrate de escribir solo números separados por comas, sin letras.")

    # Preguntar si quiere repetir
    repetir = input("\n¿Quieres hacer otro cálculo? (s/n): ")
    if repetir.lower() != "s":
        break
