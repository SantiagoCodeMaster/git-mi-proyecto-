numeros = [ 1,2,3,4,5,6,7,8,9]
#creando una funcion con lamda para multiplicar por 2 
multiplicar_por_dos= lambda x : x*2  

#creando una funcion  comun que diga si es par o no 
def es_par(num):
     if(num%2==0):
          return True
#usando filter con una funcion comun 
numero_pares = filter(es_par,numeros)

#creando lo mismo pero con lamda 
numeros_pares= filter(lambda numero:numero%2==0,numeros)

print(list(numero_pares))