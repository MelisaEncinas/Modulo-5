"""A partir del conjunto de datos dado, imprime las 5 primeras y ultimas filas
    """
    
import pandas as pd 

file_path = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_company_sales_data-221102-123259.csv'  
data = pd.read_csv(file_path)

print("Cinco primeras filas:")
print(data.head())

print("Cinco últimas filas:")
print(data.tail())

""" Limpia el conjunto de datos y actualiza el archivo CSV. Reemplaza
todos los valores de las columnas que contengan ? , n.a o NaN """

import pandas as pd

file_path = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_company_sales_data-221102-123259.csv'  # Reemplaza esta ruta con la ruta correcta a tu archivo
data = pd.read_csv(file_path)

data.replace(['?', 'n.a', 'NaN'], 0, inplace=True)
data.fillna(0, inplace=True)


conjunto_limpio = 'Modulo5_company_sales_data_2.csv'
data.to_csv(conjunto_limpio, index=False)

print(f'Archivo CSV limpio guardado en: {conjunto_limpio}')
