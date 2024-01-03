import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dt = pd.read_excel("/content/ecuador regresion lineal.xlsx")
print(dt.head())

plt.scatter(dt["x inlfacion"],dt["y pib"])
plt.xlabel("inflacion")
plt.ylabel("PIB")
plt.title("grafica de dispersion :pib y inflacion")
plt.show()

x = dt[["x inlfacion"]]
y = dt["y pib"]

regresion_lineal = LinearRegression()
regresion_lineal.fit(x, y)

a = regresion_lineal.coef_[0]
b = regresion_lineal.intercept_
print(f'Coeficiente a: {a}')
print(f'Ordenada al origen b: {b}')

plt.scatter(dt['x inlfacion'], dt['y pib'])
plt.plot(dt['x inlfacion'], regresion_lineal.predict(x), color='red')
plt.xlabel('x inlfacion')
plt.ylabel('y pib')
plt.title('Regresión Lineal: Inflación vs PIB')
plt.show()

r_squared = regresion_lineal.score(x, y)
print(f'Coeficiente de determinación (R²): {r_squared}')


valor_inflacion = 2.5

nueva_inflacion = [[valor_inflacion]]
prediccion_pib = regresion_lineal.predict(nueva_inflacion)
print(f'Predicción del PIB para la inflación {valor_inflacion}: {prediccion_pib[0]}')



nueva_inflacion = [[valor_inflacion]]
prediccion_pib = regresion_lineal.predict(nueva_inflacion)
print(f'Predicción del PIB para la inflación {valor_inflacion}: {prediccion_pib[0]}')

