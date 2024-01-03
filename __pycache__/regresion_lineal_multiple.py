import pandas as pd
import statsmodels.api as sm
import matplotlib as plt
import numpy as np 

# Cargar los datos desde Excel (asegúrate de tener el archivo Excel con tus datos)

data = pd.read_excel("/content/regresion lineal multiple colombia.xlsx")


X = data[['x IED Anual Real','x tasa de interes','x desempleo', 'x gasto publico', 'x exportaciones']]
Y = data['y pib ']


# Agregar una constante al modelo (intercepto)
X = sm.add_constant(X)

# Ajustar el modelo de regresión múltiple
modelo = sm.OLS(Y, X).fit()

# Obtener los coeficientes del modelo
coeficientes = modelo.params

# Imprimir los resultados del modelo
print(modelo.summary())

# Calcular los errores de aproximación
IED_anual_real = data['IED'].sum()
Gasto_Publico_anual_real = data['Gasto_Publico'].sum()
Exportaciones_anual_real = data['Exportaciones'].sum()

Estimacion_Mensual = IED_anual_real / 12  # Suponiendo distribución uniforme
Error_Aproximacion_IED = IED_anual_real - (Estimacion_Mensual * 12)

Estimacion_Mensual_Gasto_Publico = Gasto_Publico_anual_real / 12  # Suponiendo distribución uniforme
Error_Aproximacion_Gasto_Publico = Gasto_Publico_anual_real - (Estimacion_Mensual_Gasto_Publico * 12)

Estimacion_Mensual_Exportaciones = Exportaciones_anual_real / 12  # Suponiendo distribución uniforme
Error_Aproximacion_Exportaciones = Exportaciones_anual_real - (Estimacion_Mensual_Exportaciones * 12)

print(f'Error de Aproximación IED: {Error_Aproximacion_IED}')
print(f'Error de Aproximación Gasto Público: {Error_Aproximacion_Gasto_Publico}')
print(f'Error de Aproximación Exportaciones: {Error_Aproximacion_Exportaciones}')


modelo = sm.OLS(Y, X).fit()
coeficientes = modelo.params
X_transpuesta = X.T
XTX = np.dot(X_transpuesta, X)
print("Matriz X^TX:")
print(XTX)
plt.figure(figsize=(10, 6))
plt.scatter(Y, modelo.fittedvalues, alpha=0.6)
plt.xlabel('Crecimiento Económico Real')
plt.ylabel('Predicción de Crecimiento Económico')
plt.title('Gráfico de Regresión Lineal Múltiple')
plt.grid(True)
plt.show()
