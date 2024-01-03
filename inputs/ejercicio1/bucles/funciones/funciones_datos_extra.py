#crando una funcion de 3 parametros 
def frase(nombre,apellido,adjetivo): 
    return f"hola {nombre} {apellido} sos muy {adjetivo}"
   
   
#utilizando keywords arguments 
frase_resultante1=frase("santiago", "parada","crack")
frase_resultante2=frase( adjetivo=  "inteligente",nombre="santiago",apellido="parada" )
                        
print(frase_resultante1)
print(frase_resultante2)

#crando la misma funcion con un parametro opcional y un valor por defecto 
def frase(nombre="dalto",apellido="parada",adjetivo="tonto"): 
    return f"hola {nombre} {apellido} sos muy {adjetivo}"

frase_resultante3=frase()

print(frase_resultante3)