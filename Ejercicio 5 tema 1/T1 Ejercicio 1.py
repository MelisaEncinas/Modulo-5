""" Escribe una funcion en python para leer el contenido de
un archivo de texto Poema.txt linea por linea y mostrar el mismo en pantalla """

archivo = open('poema.txt', 'r')
print(archivo.read())

""" Escribe una funcion para contar el numero de lineas 
de un archivo de texto historia.txt
Ejemplo: Si el archivo story.txt contiene las sig lineas 
Un niño esta jugando alli 
Hay un parque infantil
Un avion esta en el cielo
El cielo es rosa.
La contraseña puede contener numero y letras 
El resultado debe ser 5
"""

def lineas_archivos(archivo):
    
        with open(archivo, 'r', encoding='utf-8') as archivo:
            num_lineas = sum(1 for _ in archivo)
        return num_lineas

archivo='historia.txt'
resultado = lineas_archivos(archivo)
if resultado is not None:
    print(f"El número de líneas en el archivo es: {resultado}")
    
    
"""Escribe una funcion en Python para contar y mostrar 
el numero total de palabras en un archivo de texto"""

def palabras_archivo_txt(archivo):

 with open(archivo, 'r', encoding='utf-8') as f:
  contenido = f.read()
  palabras = contenido.split()
  num_palabras = len(palabras)
 print(f"El número total de palabras en el archivo es: {num_palabras}")
   
archivo = 'palabras.txt' 
palabras_archivo_txt(archivo)

"""Escriba una funcion en Python para leer lineas de un archivo de texto
notas.txt. Su funcion debe encontrar la aparacion de la palabra el """

def palabra_notas(archivo, palabra):
  
        contador = 0
    # Abre el archivo en modo lectura
        with open(archivo, 'r', encoding='utf-8') as f:
            # Lee línea por línea
            for numero_linea, linea in enumerate(f, start=1):
                # Cuenta el número de apariciones de la palabra en la línea actual
                apariciones_linea = linea.lower().split().count(palabra.lower())
                
                if apariciones_linea > 0:
                    print(f"Línea {numero_linea}: {linea.strip()}")
                
                contador += apariciones_linea
        
        # Muestra el número total de apariciones
        print(f"\nNúmero total de apariciones de la palabra '{palabra}': {contador}")
    
    

# Ejemplo de uso
archivo = 'notas.txt'  # Nombre del archivo de texto
palabra_notas(archivo, 'el')

""" Escriba una funcion funcion_palabras() en python para leer las lineas
de un archivo de texto story.txt , y mostrar aquellas paalabras que 
tengan menos de 4 caracter """

def palabras_four(archivo_txt):
    
     with open(archivo_txt, 'r') as file:
        for linea in file:
         txt = linea.strip()
         if len(txt) < 4:
          print(txt)
        else:
             print("No hay palabras con menos de 4 caracteres")
             
palabras_four('story.txt')


""" Un archivo de texto llamado materia.txt contiene algun texto , que necesita ser mostrado 
de manera que cada caracter siguiente esté separado por un simbolo #.
Escriba una fedinicion de una funcion hash_display() en python que muestre todo el contenido del archivo
matter.txt en el formato deseado

Ejemplo: si el archivo materia.txt tiene el siguiente contenido almacenado: EL MUNDO ES REDONDO.
la funcion hash_display deberia mostrar el siguiente contenido:
T#H#E #W#O#R#L#D#  #I#S#  #R#O#U#N#D# """

def archivo_hash_display():
    
     with open('materia.txt', 'r') as file:
      content = file.read()
      contenido_formateado = '#'.join(content)
      print(contenido_formateado)
    
archivo_hash_display()

"""Escribe un programa en python para generar 26 archivos de textos llamados A.TXT , B.TXT y asi 
sucesivamente hasta Z.txt"""

import string

for letter in string.ascii_uppercase:
    archivo = f"{letter}.txt"
    
    with open(archivo, 'w') as file:
        file.write(f"Este es el archivo {archivo}")
        

print("Archivos creados exitosamente.")


"""Escribe un programa en python para añadir texto a un archivo y mostrar 
el texto en python.txt"""

# Nombre del archivo
archivo = 'python.txt'

# Texto que quieres añadir al archivo
texto_nuevo = 'Añadire este texto en el archivo python.txt'

# Añadir texto al archivo
with open(archivo, 'a') as f:
    f.write( texto_nuevo + '\n')

# Leer y mostrar el contenido del archivo
with open(archivo, 'r') as f:
    contenido = f.read()

print(contenido)

from collections import Counter
import re

archivo = 'frecuencia_archivo.txt'

def contador_de_palabras(archivo):

     with open(archivo, 'r', encoding='utf-8') as archivo:
         texto = archivo.read()
         palabras = re.findall(r'\b\w+\b', texto.lower())
         contador = Counter(palabras)
     return contador
            
frecuencias = contador_de_palabras(archivo)
if frecuencias:
    print("Frecuencia de las palabras:")
    for palabra, frecuencia in frecuencias.items():
        print(f"{palabra}: {frecuencia}")

""" Escribe un programa en python para comprobar si un archivo 
especificado existe"""

import os

archivo = 'palabras.txt'

def archivo_buscar(archivo):
    if os.path.isfile(archivo):
        print(f"El archivo '{archivo}' existe.")
    else:
        print(f"El archivo '{archivo}' no existe.")

archivo_buscar(archivo)

