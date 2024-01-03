#falto el, profe y los pibes van a armar la clase 


#pedir el nombre y la edad de los compañeros 
def obtener_compañeros(cantidad_de_compañeros): 
   #creando la lista con los compañeros  
    compañeros = []
    
#ejecutando un for para pedir informacion a cada compañero 
    for i in range(cantidad_de_compañeros):
       nombre = input("ingrese el nombre del compañero: ")
       edad = int(input("ingrese la edad del compañero: "))
       compañero =(nombre,edad)
       
       #agregando informacion a la lista 
       compañeros.append(compañero)
    #ordenando de mayor a menor segun la lista 
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros [x]devuelve una tupla con (nombre,edad) y despues accedemos al nombre 
    #para definir el asistente y profesor 
    asistente = compañeros[0][0]
    profesor  = compañeros [-1][0]
    
    #retomamos una tupla 
    return asistente,profesor


#desempaquetamos lo que nos retorna la funcion 
asistente,profesor = obtener_compañeros(14)


print(f"el asistente es {asistente} y el profesor es {profesor}")
