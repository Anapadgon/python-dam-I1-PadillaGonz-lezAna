# Programa que recibe una cadena y cuenta las vocales, consonantes,
# letras mayúsculas y el número total de caracteres.
# Incluye una adaptación libre para contar los espacios en blanco.

# Pedimos al usuario que escriba una frase o palabra
texto = input("Escribe una palabra o frase: ")

# Inicializamos contadores
vocales = 0
consonantes = 0
mayusculas = 0
espacios = 0 

# Recorremos cada carácter del texto
for letra in texto:
    if letra.lower() in "aeiou": #Convierte la letra a minúscula para ver si es mayúscula. Después, se mira si es aeiou y se suma al contador.
        vocales += 1
    elif letra.lower().isalpha():  #Si es una letra pero no vocal, es consonante
        consonantes += 1
    if letra.isupper(): #Si es mayúscula
        mayusculas += 1
    if letra == " ": #Espacio en blanco
        espacios += 1

# Contamos el total de caracteres
caracteres = len(texto)

# Mostramos los resultados
print("\n--- RESULTADOS ---")
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Mayúsculas: {mayusculas}")
print(f"Total de caracteres: {caracteres}")
print(f"Espacios: {espacios}")