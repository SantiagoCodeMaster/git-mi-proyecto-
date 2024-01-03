import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos desde un archivo CSV o tu fuente de datos
data = pd.read_csv('datos.csv')  # Asegúrate de tener el archivo con los datos

# Preparar los datos para la regresión lineal
X = data[['Inflacion']]  # Variable independiente (inflación)
y = data['PIB']           # Variable dependiente (PIB)

# Crear y ajustar el modelo de regresión lineal
regression_model = LinearRegression()
regression_model.fit(X, y)

# Coeficiente β₁ (pendiente)
beta_1 = regression_model.coef_[0]
print(f'Coeficiente β₁ (pendiente): {beta_1}')

# Coeficiente β₀ (ordenada al origen)
beta_0 = regression_model.intercept_
print(f'Coeficiente β₀ (ordenada al origen): {beta_0}')




