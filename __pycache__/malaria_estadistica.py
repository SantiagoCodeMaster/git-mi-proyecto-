import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 
import networkx as nx

def datos_estadisticos(df,columna_zonas,moda):
  #casos', 'latitud' y 'longitud 
  # Paso 1: Cargar los datos desde un archivo Excel
  archivo_excel = "datos_malaria_colombia.xlsx"
  df = pd.read_excel(archivo_excel)

  # Paso 2: Realizar un análisis descriptivo estadístico
  descripcion = df.describe()

      # Calcular la moda
  moda = df.mode().iloc[0]

 # Calcular datos faltantes y porcentaje de datos faltantes
  datos_faltantes = df.isnull().sum()
  porcentaje_faltantes = (datos_faltantes / len(df)) * 100


  dt = pd.read_excel("/content/Malaria_espacial.xlsx")
  dt.dropna()

  # Paso 3: Crear gráficos
  plt.figure(figsize=(12, 6))

   # Histograma
  plt.subplot(2, 2, 1)
  sns.histplot(df['casos'], bins=20, kde=True)
  plt.title('Histograma de Casos de Malaria')

  # grafico de dispersion 
  columna_zonas = 'millibar_mb_Zonal_Winds_Equator_165West_110West'

   # Crear un gráfico de dispersión
  plt.figure(figsize=(10, 6))  # Tamaño del gráfico
  plt.scatter(df[columna_zonas], df['casos'], alpha=0.5)  # Crear el gráfico de dispersión 
  plt.xlabel(columna_zonas)  # Etiqueta del eje X
  plt.ylabel('Casos de Malaria')  # Etiqueta del eje Y
  plt.title('Gráfico de Dispersión entre Casos de Malaria y Zonas')  # Título del gráfico
  plt.grid(True)  # Habilitar la cuadrícula

   # Mostrar el gráfico
  plt.show() 

  # Curva de distribución (QQ plot)
  plt.subplot(2, 2, 3)
  import scipy.stats as stats
  stats.probplot(df['casos'], dist="norm", plot=plt)
  plt.title('Curva de Distribución (QQ plot)')
  
  return df,columna_zonas,moda 
# Paso 4: Mostrar estadísticas
print("Estadísticas Descriptivas:")
print(descripcion)
print("\nModa:")
print(moda)
print("\nDatos Faltantes:")
print(datos_faltantes)
print("\nPorcentaje de Datos Faltantes:")
print(porcentaje_faltantes)

plt.show()

# Llamada a la función
columna_zonas = 'millibar_mb_Zonal_Winds_Equator_165West_110West'
moda = None  # Puedes asignar un valor a la moda si lo deseas
datos_estadisticos(df, columna_zonas, moda)
