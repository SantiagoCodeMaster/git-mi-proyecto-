#una forma no optima de sumar valores 
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
        
    return numeros_sumados

resultado =  suma ([5,7,8,1])

print(resultado)

#utilizando el operador * como argumento (*args) 
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("santiago", 5,7,8,1)

print(resultado)


#lo mismo que arriba pero utilizando el operador * como paramentro (*args) 
def suma_total(numeros):
     return  sum([*numeros])

resultado = suma_total ([5,7,8,1])
print(resultado)

