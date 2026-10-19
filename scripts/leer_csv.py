# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
# TODO 3: imprime las primeras filas para revisar las columnas

import pandas as pd
ventas = pd.read_csv("data/ventas.csv")
print(ventas.head())
print("Imprimir las dimensiones del dateframe")
print(ventas.shape)
print("Imprimir los tipos de cada columna")
print(" ")
print (ventas.dtypes)
