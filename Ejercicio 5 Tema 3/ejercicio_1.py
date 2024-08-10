"""Crea un array de enteros 4x2 e imprime sus atributos. 
Nota: El elemento debe ser de tipo unsignedint16. Imprime los siguientes atributos:
La shapedel array
Las dimensiones del array.
El tamaño de cada elemento del array en bytes"""


import numpy as np

array = np.array([[1, 2], [4, 6], [8, 10], [12, 14]], dtype=np.uint16)

print("Forma :", array.shape)

print("Dimensiones:", array.ndim)

print("Tamaño de bytes:", array.itemsize)

""" Crea una matriz de enteros 5x2 de un rango entre 
100 y 200 tal que la diferencia entre cada elemento sea 10"""

import numpy as np

def matriz_entero():
    min_rango = 100
    max_rango = 200
    diferencia = 10

    lista = []

    for valor in range(min_rango, max_rango + 1, diferencia):
        lista.append(valor)


    matriz = np.array(lista[:10]).reshape(5, 2)
    
    return matriz

matriz = matriz_entero()
print("Matriz 5x2 con diferencia 10 entre elementos:")
print(matriz)

""" A continuacion se muestra el array Numpy proporcionado.
Devuelve un array de elementos tomando la tercera columna de todas las filas

sampleArray = numpy.array([[11,22,33],[44,55,66].[77,88,99]])"""

import numpy as np

sampleArray = np.array([[11,22,33], [44,55,66], [77,88,99]])

tercera_columna = sampleArray[:, 2]

print(tercera_columna)

""" devuelve un array de filas impares y columnas pares dado el siguiente array

sampleArray = numpy.array ([[3,6,9,12].[15,18,21,24],[27,30,33,36],[39.42,45,47],[51,54,57,60]])"""

import numpy as np

sampleArray= np.array([[3, 6, 9, 12],
                    [15, 18, 21, 24],
                    [27, 30, 33, 36],
                    [39, 42, 45, 48],
                    [51, 54, 57, 60]])

filas_impar= sampleArray[1::2]
columnas_pares= sampleArray[:,::2]

print('FILAS IMPARES')
print(filas_impar)

print('COLUMNAS PARES')
print(columnas_pares)

""" Crea una matriz de resultados sumando las siguientes dos matrices de Numpy.
A continuacion, modifica la matriz de resultados calculando
el cuadrado de cada elemento.

arrayOne= numpy.array([[5, 6, 9],[21,18,27]])
arrayTwo= numpy.array([[15, 33, 24], [4,7 ,1]])"""
 
 
import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

suma_De_matrices = arrayOne + arrayTwo

cuadrado_de_matrices = suma_De_matrices ** 2

print("Matriz de resultados (suma):")
print(suma_De_matrices)

print("\nMatriz de resultados (cuadrado de cada elemento):")
print(cuadrado_de_matrices)

""" Divide la matriz en cuatro submatrices de igual tamaño.
Nota:crea una matriz de enteros 8x3 de un rango entre 10 y 34
de tal manera que la diferencia entre cada elemento sea 1 y 1uego 
divide la matriz en cuatro submatrices de igual tamaño"""

import numpy as np

matrices = np.arange(10, 34).reshape(8, 3)

submatrices = np.split(matrices, 4)

print("Matriz original 8x3:")
print(matrices)

for i, sub_matriz in enumerate(submatrices, start=1):
    print(f"\nSubmatriz {i}:")
    print(sub_matriz)

"""Ordena el siguiente array de NumPy:
Caso 1: ordenar array por la segunda fila 
Caso 2: ordenar array por la segunda columna

sampleArray  = numpy.array([[34, 43, 73], [82,22,12]. [53,94,66]])"""

import numpy as np

sampleArray  = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

#Caso 1: ordenar array por la segunda fila 
caso_uno = np.argsort(sampleArray[1])

segunda_fila = sampleArray[:, caso_uno]

# Obtener los índices que ordenarían la segunda columna
caso_dos = np.argsort(sampleArray[:, 1])

# Ordenar cada columna usando los índices obtenidos
segunda_columna = sampleArray[caso_dos, :]



print("Array ordenado por la segunda fila:")
print(segunda_fila)

print("Array ordenado por la segunda columna:")
print(segunda_columna)

"""Imprime el maximo del eje 0 y el minimo del eje 1 de la 
siguiente matriz bidimensional: 

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])"""

import numpy as np

sampleArray = np.array([[34,43,73],
                        [82,22,12],
                        [53,94,66]])

# Encontrar el máximo del eje 0
maximo_eje_0 = np.amax(sampleArray, axis=0)

# Encontrar el mínimo del eje 1
minimo_eje_1 = np.amin(sampleArray, axis=1)

print("Máximo del eje 0:", maximo_eje_0)
print("Mínimo del eje 1:", minimo_eje_1)

"""Elimina la segunda columna de una matriz dada e inserta
la siguiente columna nueva en su lugar

sampleArray = numpy.array([[34,43.73],[82.22,12],[53,94,66]])
newColumn= numpy.array([[10,10,10]])"""

import numpy as np

sampleArray = np.array([[34,43,73],
                        [82,22,12],
                        [53,94,66]])

newColumn = np.array([[10,10,10]])

sampleArray = np.delete(sampleArray, 1, axis=1)

sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)


print('Matriz actualizada')
print(sampleArray)