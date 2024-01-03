#creando una funcion que nos devuleva numeros primos
#entre cero y el numero que pasamos 

#crear una funcion donde verifique si es numero primo 
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse 
    #por ningun numero entre 2 y ese mismo numero -1 
    for i in range(2,num -1):
    #si es divisible por alguno retomamos false y termina el bucle 
        if num%i==0:return False
 #si termina el bucle , significa que no fue divisible entonces es primo 
    return True

#creando una funcion que retorne una lista con todos los numeros primos 
def primos_hasta(num):
    #creamos la lista 
    primos =[]
    for i in range (2,num ):
        #verificamos si el valor es primo 
        resultado =  es_primo(i)
        
        #en que caso de que lo sea agregamos a la lista 
        if resultado == True:primos.append(i)
        
    #devolvemos la lista 
    return primos

        
#creamos el resultado llamando a la funcion y lo mostramos 
resultado=primos_hasta(12)
print(resultado)