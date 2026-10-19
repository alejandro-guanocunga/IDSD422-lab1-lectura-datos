# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Ejecutar desde la raíz: python scripts/leer_csv.py

import pandas as pd

# Cargar datos desde el archivo CSV
ventas = pd.read_csv("data/ventas.csv")

# Mostrar primeras filas
print(ventas.head())

# Mostrar dimensiones (filas, columnas)
print("Imprimir las dimensiones del dateframe")
print(ventas.shape)

# Mostrar tipo de dato inferido en cada columna
print("Imprimir los tipos de cada columna")
print(" ")
print(ventas.dtypes)
