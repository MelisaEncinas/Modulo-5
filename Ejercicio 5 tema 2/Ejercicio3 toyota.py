""" Encuentra el nombre de la empresa del coche mas caro- 
Imprime el nombre de la empresa del coche mas caro y su precio """

import csv

archivo = r'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'  

data = []

with open(archivo, 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        try:
            row['price'] = float(row['price'])
            data.append(row)
        except ValueError:
            continue

if data:
    coche_mas_caro = max(data, key=lambda x: x['price'])

    empresa_coche = coche_mas_caro['company']
    precio_maximo = coche_mas_caro['price']

    print(f"Empresa: {empresa_coche}, Precio: {precio_maximo}")
else:
    print("Error en el archivo.")
    
    
"""Imprime todos los datos de los coches Toyota"""

import pandas as pd

archivo = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'
automobile_data_toyota = pd.read_csv(archivo)

coches_toyota = automobile_data_toyota[automobile_data_toyota['company'] == 'toyota']

print(coches_toyota)

""" Cuenta el total de coches por empresa """


import pandas as pd

archivo = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'

automobile_data = pd.read_csv(archivo)

total_coches_por_empresa = automobile_data.groupby('Empresa').size().reset_index(name='total de coches')

print(total_coches_por_empresa)

"""Encuentra el coche con el precio mas alto de precio de cada empresa."""

import pandas as pd

ruta_archivo = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'
automobile_data = pd.read_csv(ruta_archivo)


automobile_data['price'] = pd.to_numeric(automobile_data['price'], errors='coerce')


precios_mas_altos = automobile_data.groupby('company')['price'].max()

print(precios_mas_altos)


"""Encuentra el kilometraje medio de cada empresa
fabricante de automoviles """

import pandas as pd

# Load the uploaded CSV file
archivo = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'
data_km = pd.read_csv(archivo)

data_km.head()
kilometraje_medio = data_km.groupby('company')['average-mileage'].mean()

kilometro = kilometraje_medio.reset_index()
kilometro.columns = ['Empresa', 'Kilometroje Medio']

# Mostrar el resultado
print(kilometro)

"""Ordena todos los coches por la columna de Precio """


import pandas as pd

# Cargar el archivo CSV
archivo = 'C:/Users/martuu/Desktop/Nueva carpeta/Ejercicio 5 tema 2/Modulo5_Automobile_data-221102-123259.csv'

data = pd.read_csv(archivo)

data['price'] = pd.to_numeric(data['price'], errors='coerce')

data = data.dropna(subset=['price'])

orden = data.sort_values(by='price')

print(orden)

"""Concatena dos dataframes utilizando las siguientes condiciones:

GermanCars = {'Company':['Ford'. 'Mercedes', 'BMV', 'Audi'], 'Price':[23845, 171995.135925.71400]}
japanesecars= {'Company':['Toyata', 'Honda','Nissan', 'Mitsubishi'] 'Price': [29995,23600,61500,58900]}"""

import pandas as pd

GermanCars = {
    'Company':['Ford','Mercedes','BMV','Audi'],
    'Price': [23845,171995,135925,71400]
    
}

JapaneseCars = {
    'Company': ['Toyata', 'Honda', 'Nissan', 'Mitsubishi'],
    'Price': [29995,23600,61500,58900]
    
}

datos_germancars = pd.DataFrame(GermanCars)
datos_japanesescars = pd.DataFrame(JapaneseCars)

cars = pd.concat([datos_germancars, datos_japanesescars], ignore_index=True)

print(cars)
""" Combina dos dataframe utilizando la siguiente condicion. 
Crea dos dataframe utilizando los siguientes dos Dicts, fuisionalos y añade el segundo dataframe como una nueva 
columna al primer dataframe

Car_price: {'Company':['Toyota', 'Honda', 'BMV', 'Audi' ], 'Price':[23845,17995,135925,71400]}
Car_Horsepower: {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],'horsepower': [141,89,182,160]}"""


import pandas as pd

car_Price = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'Price': [23845,17995,135925,71400]
}
car_Horsepower = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'Price': [141,89,182,160]
}

df_carprice = pd.DataFrame(car_Price)
df_horsepower= pd.DataFrame(car_Horsepower)

combinar_price_horsepower = pd.merge(df_carprice, df_horsepower, on='Company')

print(combinar_price_horsepower)