# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence (Alejandro Mateo Guanocunga Ojeda)
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Recibí y audité los tres reportes semanales de ventas provenientes del ERP de sucursales (`ventas.csv`), la API de la plataforma de fidelización (`ventas.json`) y el consolidado de Finanzas (`ventas.xlsx`). Confirmé que los tres archivos contienen exactamente la misma información transaccional (5 sucursales, 4 variables, $60,040 en ventas totales y 1,577 clientes), sin pérdidas ni discrepancias entre sistemas. El equipo de BI recomienda proceder con la toma de decisiones sobre esta base consolidada, tomando a Guayaquil Centro como referente de volumen comercial ($15,200) y analizando las prácticas de Cuenca por registrar el ticket promedio por cliente más alto ($40.67).

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | Python: `pd.read_csv("data/ventas.csv")` / R: `read_csv("data/ventas.csv")` |
| JSON | API de fidelización | 5 | 4 | Python: `json.load(f)` + `pd.json_normalize(datos)` / R: `fromJSON("data/ventas.json")` |
| Excel | Consolidado de finanzas | 5 | 4 | Python: `pd.read_excel("data/ventas.xlsx", sheet_name="ventas")` / R: `read_excel("data/ventas.xlsx", sheet="ventas")` |

*Responde: ¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*

No, la estructura interna de almacenamiento no cambia el contenido ni el significado de los datos. Aunque el archivo CSV se almacena como texto plano separado por comas, el JSON como una colección jerárquica de pares clave-valor y el archivo Excel como un contenedor binario/XML con hojas de cálculo, una vez que los leí y normalicé en estructuras tabulares (`DataFrame` en Python y `tibble`/`data.frame` en R), comprobé que los tres resguardan exactamente los mismos registros, valores numéricos y categorías.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `dbl` (`numeric`) | Numérica cuantitativa discreta/continua: representa el monto facturado en dólares por sucursal; permite operaciones aritméticas y agregaciones. |
| `clientes` | `int64` | `dbl` (`numeric`) | Numérica cuantitativa discreta: conteo exacto de clientes atendidos en la semana; apta para sumas y cálculo del ticket. |
| `sucursal` | `object` (`str`) | `chr` (`character`) | Categórica nominal (identificador de texto): nombre del punto de venta analizado. |
| `region` | `object` (`str`) | `chr` (`character`) | Categórica nominal: agrupación geográfica (`Sierra` o `Costa`) para segmentar resultados. |

Los tipos inferidos por ambos lenguajes son los esperados y confirman una buena calidad de origen: tanto `ventas` como `clientes` fueron reconocidos directamente como tipos numéricos operables sin requerir limpieza previa, mientras que `sucursal` y `region` se identificaron como cadenas de caracteres.

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*

Si `ventas` o `clientes` se hubieran inferido como texto (`object` en Python o `chr` en R), habría indicado la presencia de caracteres no numéricos o suciedad en los registros; por ejemplo, símbolos de moneda incrustados (`"$12,450"`), separadores de miles mal formateados, espacios en blanco invisibles, letras mezcladas por error de digitación o textos usados para representar valores faltantes (como `"N/A"`, `"null"`, `"sin datos"` o guiones `"-"`).

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*

* **Formato CSV (`ventas.csv`):** Su lectura fue directa porque ya tiene estructura rectangular de filas y columnas delimitadas por comas. Respecto a las variables categóricas (`sucursal` y `region`), en Python (`pandas`) se expresaron bajo el tipo genérico `object` (punteros a cadenas de texto), mientras que en R (`readr`) se cargaron como vectores de caracteres (`chr`), los cuales en R pueden convertirse explícitamente a `factor` cuando se requiere definir niveles categóricos fijos para modelado o agrupación.
* **Formato JSON (`ventas.json`):** No llegó como una tabla directa. En Python, `json.load()` devolvió una lista nativa de diccionarios (`list` de `dict`), por lo que fue necesario "aplanarla" utilizando `pd.json_normalize(datos)` para desanidar las claves y construir el DataFrame de 5 filas por 4 columnas. En cambio, en R la función `jsonlite::fromJSON()` simplificó automáticamente el arreglo de objetos JSON en un `data.frame` rectangular en un solo paso.
* **Formato Excel (`ventas.xlsx`):** A diferencia del CSV, un archivo `.xlsx` es un libro binario que puede contener múltiples pestañas (resúmenes, metadatos o notas). Por ello, fue indispensable indicar explícitamente el parámetro `sheet_name="ventas"` en Python y `sheet="ventas"` en R para garantizar que el script extrajera exactamente la hoja con los datos transaccionales y no una pestaña por defecto incorrecta.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | Media global: **$12,008.00** (Quito Norte: $12,450 · Quito Sur: $9,870 · Guayaquil Centro: $15,200 · Guayaquil Norte: $13,980 · Cuenca: $8,540) |
| Ticket promedio (ventas ÷ clientes) | **$38.07** ($60,040 en ventas totales ÷ 1,577 clientes totales) |
| Sucursal con mayor venta | **Guayaquil Centro** ($15,200 y 410 clientes; ticket de $37.07) |
| Sucursal con menor venta | **Cuenca** ($8,540 y 210 clientes; ticket de $40.67) |
| Región con mayor venta total | **Sierra** ($30,860 en 3 sucursales vs. Costa con $29,180 en 2 sucursales) |

## 5. Conclusiones y recomendación

1. **Integridad confirmada entre sistemas:** Los tres archivos (`ventas.csv`, `ventas.json` y `ventas.xlsx`) son 100 % consistentes entre sí en dimensiones (`5 x 4`), tipos de datos y valores, sumando un total de **$60,040** en ventas y **1,577 clientes**. El ERP, la API de fidelización y el consolidado de Finanzas están correctamente sincronizados para el corte de la semana 39.
2. **Contraste entre volumen de venta y valor de ticket:** Aunque **Guayaquil Centro** lidera la facturación total con **$15,200** gracias a su alto flujo de clientes (410), su ticket promedio es el más bajo ($37.07). Por el contrario, **Cuenca** registra la menor venta total (**$8,540** con 210 clientes), pero posee el **ticket promedio más alto de toda la cadena ($40.67)**, superando el promedio general de la empresa ($38.07).
3. **Desempeño regional y recomendación a gerencia:** La región **Sierra** concentra la mayor venta acumulada (**$30,860**) por contar con tres sucursales operativas, aunque la región **Costa** logra casi el mismo volumen (**$29,180**) con solo dos locales (promedio de $14,590 por local en Costa frente a $10,286.67 en Sierra). Se recomienda a la gerencia replicar las estrategias de venta cruzada de Cuenca en las sucursales de Guayaquil para elevar su ticket por cliente, e implementar campañas de tráfico en Cuenca y Quito Sur. Este análisis es descriptivo para las 5 sucursales en la semana 39 y no proyecta tendencias futuras.
