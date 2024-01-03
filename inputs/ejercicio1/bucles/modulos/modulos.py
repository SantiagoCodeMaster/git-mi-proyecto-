#importando un modulo y asignadole el nombre "m_saludar"


import modulos_saludar as m_saludar

#desde ese modulo, importamos dos funciones 
from modulos_saludar import Saludar as saludar_bien , saludar_raro as saludar_diferente

#creamos las variables con los resultados 
saludo = saludar_bien("santiago")
saludo_raro = saludar_diferente("perro")


#mostrando los resultados 
print(saludo)
print(saludo_raro)

#para ver la propiedades y metodos de el namespace 
print(dir(m_saludar))

#accedemos al nombre de este modulo 
print(__name__ )

#accedemos al nombre del modulo llamado : 
print(m_saludar.__name__ ) 

