#creando un conjunto con set()

conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset (["dato12","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos 

conjunto1 = {1,2,3,5,7}
conjunto2 = {1,2,3}

#verificando si es un conjunto
resultado= conjunto2.issubset(conjunto1)
resultado2= conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado3= conjunto2.issuperset(conjunto1)
resultado4= conjunto2 >= conjunto1

#verificar si hay algun numero en comun 
resultado5 = conjunto2.isdisjoint(conjunto1)

print(resultado5)

