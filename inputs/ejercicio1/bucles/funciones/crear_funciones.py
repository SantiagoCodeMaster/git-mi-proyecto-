#creando una funcion simple 
#def saludar ():
    #print("hola santi sos un crack ¿como vas?")
    
    
#ejecutando la funcion simple 
#saludar()

#crear una funcion que tenga parametros 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"): 
        adjetivo = "titan"
    else :
        adjetivo = "amor "
    
    print(f"hola {nombre}, mi {adjetivo} ¿como vas?")
    
saludar("camila","mujer")
saludar("santiago","hombre")
saludar("felipe","otre")


#crear una funcion que retorne multiple  valores
def crear_contraseña_random(num) :
     chars = "abcdefjhi"
     num_entero = str(num)
     num = int(num_entero[0])
     c1 = num - 2 
     c2 = num
     c3 = num - 5 
     
     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
     return contraseña, num 
 
password,primer_numero= crear_contraseña_random(40)
print(f"tu contraseña nueva es:{password} ")
print(f"el numero utilizado para creala fue:{ primer_numero} ")
