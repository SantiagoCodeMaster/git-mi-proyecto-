import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 
import networkx as nx
import geopandas as gpd


def datos_estadisticos(descripcion,moda,datosfaltantes,porcentajes_faltantes):
  
  # Paso 1: Cargar los datos desde un archivo Excel
  df = pd.read_excel("archivo excel ")

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
  
  return  descripcion,moda,datos_faltantes,porcentaje_faltantes
# Paso 4: Mostrar estadísticas
variable = datos_estadisticos(descripcion,moda,datosfaltantes,porcentajes_faltantes)
print("Estadísticas Descriptivas:")
print(variable.descripcion)
print("\nModa:")
print(variable.moda)
print("\nDatos Faltantes:")
print(variable.datos_faltantes)
print("\nPorcentaje de Datos Faltantes:")
print(variable.porcentaje_faltantes)


#punto numero 2 

# Cargar el archivo GeoJSON con los límites de los departamentos de Colombia
gdf = gpd.read_file("https://raw.githubusercontent.com/Dallene/Municipios-y-veredas-de-Colombia-JSON./main/MunicipiosVeredas19MB.json")

# Cargar los datos de los departamentos y casos de malaria desde los archivos Excel
departamentos = pd.read_excel("/content/codigos_municipios_dane.xlsx")
casos_malaria = pd.read_excel("/content/malaria.py.xlsx")

# Seleccionar el período de tiempo deseado
periodo_seleccionado = 2021  # Cambia el período temporal según tus datos

# Convertir la columna 'Ano' de casos_malaria a cadena
casos_malaria['Ano'] = casos_malaria['Ano'].astype(str)

# Fusionar los datos de departamentos y casos de malaria por año y departamento
casos_departamentos = pd.merge(departamentos, casos_malaria, left_on='Departamento', right_on='Ano')

# Filtrar los datos para el período seleccionado
datos_periodo = casos_departamentos[casos_departamentos['Ano'] == str(periodo_seleccionado)]

# Crear un mapa de cloropletas
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
datos_periodo.plot(column="casos", cmap="YlOrRd", linewidth=0.8, ax=ax, legend=True)
ax.set_title(f"Frecuencia de Casos de Malaria por Departamento en {periodo_seleccionado}")
plt.show()

#punto 3 
# Cargar el archivo GeoJSON con los límites de los municipios de Colombia
#punto 3 
# Cargar el archivo GeoJSON con los límites de los municipios de Colombia
gdf = gpd.read_file("https://raw.githubusercontent.com/Dallene/Municipios-y-veredas-de-Colombia-JSON./main/MunicipiosVeredas19MB.json")

casos = pd.read_excel("/content/codigos_municipios_dane.xlsx")
casos2 = pd.read_excel("/content/malaria.py.xlsx")

casos_malaria = pd.merge(casos, casos2, left_on='Codigo Ciudad', right_on='Ano')  # Reemplaza con la ubicación de tu archivo
# Asegurarse de que los campos de fusión tengan el mismo nombre y tipo de datos
casos_malaria['Codigo Ciudad'] = casos_malaria['Codigo Ciudad'].astype(int)
# Crear un mapa de cloropletas (mapa de colores) para la frecuencia de aparición de casos por municipio y período
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
periodo_seleccionado = 2021  # Cambia el período temporal según tus datos
filtered_data = casos_malaria[casos_malaria['Ano'] == periodo_seleccionado]
filtered_data.plot(column="casos", cmap="YlOrRd", linewidth=0.8, ax=ax, legend=True)
ax.set_title(f"Frecuencia de Casos de Malaria en {periodo_seleccionado}")
plt.show()

#punto 4 
#  pip install tk

# Crear una ventana principal de la aplicación
app = tk.Tk()
app.title("Visualización de Casos de Malaria")

# Función para mostrar la gráfica de serie de tiempo
def mostrar_grafica():
    seleccion = combobox.get()
    periodo = int(entry_periodo.get())

    if seleccion == "Departamento":
        # Filtrar por departamento
        departamento = entry_departamento.get()
        datos_filtrados = casos_malaria[(casos_malaria['Tipo'] == "Departamento") & (casos_malaria['Ubicación'] == departamento)]
    elif seleccion == "Municipio":
        # Filtrar por municipio
        municipio = entry_municipio.get()
        datos_filtrados = casos_malaria[(casos_malaria['Tipo'] == "Municipio") & (casos_malaria['Ubicación'] == municipio)]
    
    # Filtrar por período
    datos_filtrados = datos_filtrados[datos_filtrados['Año'] == periodo]

    # Crear la gráfica de serie de tiempo
    fig,ax = plt.subplots(figsize=(8, 6))
    datos_filtrados.plot(x='Mes', y='Casos', ax=ax, marker='o', linestyle='-')
    ax.set_title(f"Serie de Tiempo de Casos de Malaria en {seleccion}: {departamento if seleccion == 'Departamento' else municipio} - Año {periodo}")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Casos Reportados")

    # Agregar la gráfica a la ventana de la aplicación
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=4, column=0, padx=10, pady=10)

# Etiqueta y entrada para seleccionar departamento o municipio
label_tipo = ttk.Label(app, text="Seleccionar Tipo:")
label_tipo.grid(row=0, column=0, padx=10, pady=5)
combobox = ttk.Combobox(app, values=["Departamento", "Municipio"])
combobox.grid(row=0, column=1, padx=10, pady=5)
combobox.set("Departamento")

# Entrada para ingresar el nombre del departamento o municipio
label_ubicacion = ttk.Label(app, text="Nombre del Departamento/Municipio:")
label_ubicacion.grid(row=1, column=0, padx=10, pady=5)
entry_ubicacion = ttk.Entry(app)
entry_ubicacion.grid(row=1, column=1, padx=10, pady=5)

# Entrada para ingresar el año
label_periodo = ttk.Label(app, text="Año:")
label_periodo.grid(row=2, column=0, padx=10, pady=5)
entry_periodo = ttk.Entry(app)
entry_periodo.grid(row=2, column=1, padx=10, pady=5)

# Botón para mostrar la gráfica
boton_mostrar = ttk.Button(app, text="Mostrar Gráfica", command=mostrar_grafica)
boton_mostrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
app.mainloop()

#punto 5 


# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (municipios y departamentos) al grafo
for _, row in casos_malaria.iterrows():
    ubicacion = row['Ubicación']
    tipo = row['Tipo']
    G.add_node(ubicacion, tipo=tipo)

# Agregar relaciones (aristas) entre municipios y departamentos
for _, row in casos_malaria.iterrows():
    ubicacion = row['Ubicación']
    tipo = row['Tipo']
    ano = row['Año']
    casos = row['Casos']

    # Obtener el nodo del municipio o departamento
    nodo_ubicacion = ubicacion + " - " + tipo

    # Agregar la relación con el año como atributo
    G.add_edge(ano - 1, ano, ubicacion=nodo_ubicacion, casos=casos)

# Visualizar el grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black')
labels = nx.get_edge_attributes(G, 'casos')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title("Grafo de Relaciones entre Municipios y Departamentos basado en Casos Reportados por Año")
plt.show()


# Función para actualizar el mapa cuando se cambia el año y la zona
def actualizar_mapa():
    año_seleccionado = int(slider_año.get())
    zona_seleccionada = combobox_zona.get()

    # Filtrar los datos de casos_malaria por año y zona seleccionada
    datos_filtrados = casos_malaria[(casos_malaria['Ano'] == año_seleccionado) & (casos_malaria['Zona'] == zona_seleccionada)]

    # Crear un mapa de cloropletas con los datos filtrados (reemplaza con tu lógica de mapa)
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    # Aquí deberías agregar tu lógica para crear un mapa con los datos
    # Puedes utilizar librerías como geopandas o folium para esta tarea
    # Por ejemplo, para mostrar un mensaje de ejemplo:
    ax.text(0.5, 0.5, "Mapa de ejemplo", fontsize=20, ha='center')
    ax.axis('off')
    plt.show()

# Crear una ventana principal de la aplicación
app = tk.Tk()
app.title("Visualización de Casos de Malaria por Zona")

# Slider para seleccionar el año
label_año = ttk.Label(app, text="Seleccionar Año:")
label_año.grid(row=0, column=0, padx=10, pady=5)
slider_año = tk.Scale(app, from_=2009, to=2020, orient="horizontal")
slider_año.grid(row=0, column=1, padx=10, pady=5)
slider_año.set(2020)  # Establece el año inicial

# Combobox para seleccionar la zona
label_zona = ttk.Label(app, text="Seleccionar Zona:")
label_zona.grid(row=1, column=0, padx=10, pady=5)
zonas_disponibles = casos_malaria['Zona'].unique()
combobox_zona = ttk.Combobox(app, values=zonas_disponibles)
combobox_zona.grid(row=1, column=1, padx=10, pady=5)
combobox_zona.set(zonas_disponibles[0])  # Establece la primera zona como predeterminada

# Botón para actualizar el mapa
boton_actualizar = ttk.Button(app, text="Actualizar Mapa", command=actualizar_mapa)
boton_actualizar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
app.mainloop()


