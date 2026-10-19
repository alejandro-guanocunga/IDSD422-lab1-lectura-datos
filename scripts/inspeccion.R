# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

library(readr)

ventas <- read_csv("data/ventas.csv", show_col_types = FALSE)

# TODO 2
print("=== ESTRUCTURA Y TIPOS ===")
str(ventas)

# TODO 3
ventas$ticket <- ventas$ventas / ventas$clientes
print("=== PRIMERAS FILAS CON TICKET ===")
print(head(ventas))

# TODO 4: Indicadores
cat("\n=== INDICADORES SEMANALES ===\n")

# 1. Venta promedio por sucursal
cat("\n1. Venta promedio por sucursal:\n")
print(aggregate(ventas ~ sucursal, data = ventas, mean))

# 2. Ticket promedio general
ticket_promedio <- sum(ventas$ventas) / sum(ventas$clientes)
cat(sprintf("\n2. Ticket promedio general: %.2f\n", ticket_promedio))

# 3. Sucursal con mayor y menor venta
suc_mayor <- ventas$sucursal[which.max(ventas$ventas)]
max_val <- max(ventas$ventas)
suc_menor <- ventas$sucursal[which.min(ventas$ventas)]
min_val <- min(ventas$ventas)
cat(sprintf("\n3. Sucursal con mayor venta: %s (%d)\n", suc_mayor, max_val))
cat(sprintf("   Sucursal con menor venta: %s (%d)\n", suc_menor, min_val))

# 4. Región con mayor venta total
ventas_region <- aggregate(ventas ~ region, data = ventas, sum)
reg_mayor <- ventas_region$region[which.max(ventas_region$ventas)]
reg_val <- max(ventas_region$ventas)
cat(sprintf("\n4. Región con mayor venta total: %s (%d)\n", reg_mayor, reg_val))
