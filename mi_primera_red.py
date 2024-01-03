#importar las librerias 
import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt

#declaramos los eventos pasados 
entrada = np.array([1,6,30,7,70,43,503,201,1005,99] , dtype= float)
resultados = np.array([0.0254,0.1524,0.762,1.788,0.1778,1.0922,12.776,5.1054,25.527,2.514] , dtype = float)

#topografia de la red 
capa1 = tf.keras.layers.Dense(units = 1,input_shape = [1])

modelo = tf.keras.Sequential([capa1])

# asignamos  optimizador y metrica de perdida 
modelo.compile(
    optimizer= tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
print("entrendando la red")

#entrenamos el modelo 
entrenamiento = modelo.fit(entrada,resultados,epochs=500,verbose= False)

#guardar la red neruonal
modelo.save('RedNeruonal.h5')
modelo.save_weights('pesos.h5')

#observamos el comportamiento de nuestra red
plt.xlabel ("Ciclos de entrenamiento")
plt.ylabel("errores")
plt.plot(entrenamiento.history["loss"])
plt.show()


#veificar si la red entreno 
print("red neuronal entrenada")

#prediccion
 
i = input("ingresar el valor en pulgadas: ")
i = float(i)

prediccion = modelo.predict([i])
print("el valor en metros es: ",str(prediccion))