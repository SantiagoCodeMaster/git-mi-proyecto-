#iterar conjuntos/tuplas
animales  =  {"loro","gato","perro","vaca","conejo","pez"}
food = {"carne","pollo", "arroz","pizza","ajiaco","pescado"}
numeros = { 10 , 62 , 32 ,324 , 322,54,}

#recoriendo la conjunto de animales y comida 
for animal in animales:
    print(f"ahora la variable animal es igual a : {animal}")

for  foods in food:
    print(f"ahora la variable food es igual a : {foods}")

#recoriendo la conjunto numero y multiplicando por 10 

for numero in numeros: 
    resultado = numero  * 10
    print(resultado)
    
#iternado dos conjuntos del mismo tamaño al mismo tiempo 
for foods,animal,numero in zip(animales,food,numeros):
  print(f"recorriendo  conjunto 1 : {animales} ")
  print (f"recorriendo conjunto 2:{food}")
  print (f"recorriendo conjunto 3:{numeros}")
  


#la forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros): 
    indice = num[0]
    valor = num[1]
    print(f"indice es{num[0]} y la variable es {num[1]} ")
    
for num in enumerate(numeros):
    print (num)
    print (num[0])
    print (num[1])

#usando el for/else 
for numero in numeros:
    print(f"ejecutando el ultimo bucle,valor actual:{numeros}")

else :
    print("el bucle termino ")
    

#todo lo anterior funciona exactamente igual para tuplas 