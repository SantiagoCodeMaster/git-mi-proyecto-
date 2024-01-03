#creando las listas 
frutas = ["manzana","peras","mandarina","bananas","mango"]
cadena = "Hola santi"
numeros = [1,8,10,7]
#evitando que se coma una pera con la setencia continue 
for fruta in frutas:
    if fruta == "peras":
        continue
    
    print(f"me voy a comer una {fruta}")
  
#evitando que el bucle siga ejecutandose   (el else no se ejecuta tampoco)
for fruta in frutas:
     print(f"me voy a comer una {fruta}") 
    
     if fruta == "manzana":
        break
    
else: 
     print("se vomita ")     
   
 #recorrer una cadena de texto    

for letra in cadena :
     print(letra)   
     
#for multiplicando por 2 la lista de numeros 
numeros_duplicados = list()
for numero in numeros :
    numeros_duplicados.append(numero*2)
    
    print(numeros_duplicados)

#for mutiplicando por 2 sin ciclo de 4  en  una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros ]

print(numeros_duplicados) 