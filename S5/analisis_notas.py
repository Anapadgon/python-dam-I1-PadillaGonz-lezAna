#Programa: Resumen estadístico de calificaciones

from collections import Counter  #Importar la colección Counter que sirve para calcular la moda (contar cuántas veces aparece cada elemento en una lista)

#Pedir al usuario las notas separadas por comas, se guardará como texto (una cadena) en la variable entrada
entrada = input("Introduce las calificaciones separadas por comas: ")

#Separar la cadena en una lista (split divide la cadena entrada en partes usando la coma como separador)
lista_texto = entrada.split(",")

#Convertir cada elemento a número y validar
notas = [] #Crea una lista vacía donde iremos guardando las notas convertidas a float
for n in lista_texto: #Recorre cada texto n de la lista creada con split
    try:
        nota = float(n.strip())  #Quitamos espacios al principio o final (strip) y convertimos a número (float)
        notas.append(nota) #Si la conversión a float tiene éxito se añade a la lista notas
    except ValueError:
        print(f"Valor no válido detectado: '{n.strip()}'. Asegúrate de usar solo números.")
        exit()  #Salir del programa si hay error, este código lo detiene

#Comprobar que se ha introducido al menos una nota
if len(notas) == 0:
    print("No se han introducido notas. El programa se cerrará.")
    exit()

#Calcular estadísticas básicas
total = len(notas) #Cuántos elementos hay en la lista
media = round(sum(notas) / total, 2) #Sumamos todas las notas, calcula la media y redondea a 2 decimales
nota_min = min(notas) #Obtiene la nota mínima
nota_max = max(notas) #Obtiene la nota máxima

#Calcular porcentajes de aprobados y sobresalientes
aprobados = 0
sobresalientes = 0

#Recorremos todas las notas una por una
for n in notas:
    if n >= 5:
        aprobados += 1 #Sumamos 1 si la nota es 5 o más
    if n >= 9:
        sobresalientes += 1 #Sumamos 1 si la nota es 9 o más

#Calculamos los porcentajes
porc_aprobados = round((aprobados / total) * 100, 2)
porc_sobresalientes = round((sobresalientes / total) * 100, 2)

#Calcular la(s) moda(s) (nota más repetida)
contador = Counter(notas)  #Cuenta cuántas veces aparece cada nota
max_frecuencia = max(contador.values())  #Busca la cantidad más alta

modas = []  #Lista vacía para guardar las modas
for nota, veces in contador.items():  #Recorremos cada nota y sus repeticiones
    if veces == max_frecuencia:
        modas.append(str(nota))  #Si se repite igual que la máxima, la guardamos

#Mensaje final según la media
if media >= 8:
    mensaje = "Nivel excelente"
elif media >= 5:
    mensaje = "Nivel medio"
else:
    mensaje = "Necesita refuerzo"

#Mostrar resultados
print("\n--- Resumen de calificaciones ---")
print(f"Número total de notas: {total}")
print(f"Media: {media:.2f}")
print(f"Nota mínima: {nota_min}")
print(f"Nota máxima: {nota_max}")
print(f"Porcentaje de aprobados: {porc_aprobados}%")
print(f"Porcentaje de sobresalientes: {porc_sobresalientes}%")

#Si hay varias modas (empate), join une todos los elementos de la lista modas, separándolos con una coma y un espacio
print(f"Nota(s) más repetida(s): {', '.join(modas)}") 

#Mensaje final sobre el nivel del grupo según la media
print(f"Evaluación final: {mensaje}")
