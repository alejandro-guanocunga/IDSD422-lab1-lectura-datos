# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

import pandas as pd

# TODO 1
ventas = pd.read_csv("data/ventas.csv")

# TODO 2
print("=== TIPOS DE DATOS ===")
print(ventas.dtypes)

# TODO 3
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
print("\n=== PRIMERAS FILAS CON TICKET ===")
print(ventas.head())

# TODO 4: Indicadores
print("\n=== INDICADORES SEMANALES ===")

# Venta promedio por sucursal
venta_prom_sucursal = ventas.groupby("sucursal")["ventas"].mean()
print("\n1. Venta promedio por sucursal:")
print(venta_prom_sucursal)

# Ticket promedio (ventas totales / clientes totales)
ticket_promedio = ventas["ventas"].sum() / ventas["clientes"].sum()
print(f"\n2. Ticket promedio general: {ticket_promedio:.2f}")

# Sucursal con mayor y menor venta
suc_mayor = ventas.loc[ventas["ventas"].idxmax(), "sucursal"]
max_val = ventas["ventas"].max()
suc_menor = ventas.loc[ventas["ventas"].idxmin(), "sucursal"]
min_val = ventas["ventas"].min()
print(f"\n3. Sucursal con mayor venta: {suc_mayor} ({max_val})")
print(f"   Sucursal con menor venta: {suc_menor} ({min_val})")

# Región con mayor venta total
ventas_por_region = ventas.groupby("region")["ventas"].sum()
reg_mayor = ventas_por_region.idxmax()
reg_val = ventas_por_region.max()
print(f"\n4. Región con mayor venta total: {reg_mayor} ({reg_val})")
