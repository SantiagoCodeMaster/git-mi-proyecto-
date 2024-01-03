#pedirle al usuario 
texto  = input("di una frase crack y te calculo cuanto tardarias diciendolo: ")
palabras_separadas= texto.split(" ")
cantidad_de_palabras = len(palabras_separadas)
tiempo = 120
print(f"dijiste {cantidad_de_palabras} palabras, y te demoraste {cantidad_de_palabras/2} segundos en decirlo " )
print(f"dalto lo diria en  {cantidad_de_palabras* 100 // 2 *1.3 /100} segundos" )
if cantidad_de_palabras > 120:
    print("para flaco tampoco te pedi un testamento")
else :
    print("wow eres muy rapido")
    
resultado = dir(texto)
print(resultado)