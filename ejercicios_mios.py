import numpy as np

def area_triangulo():
  base_longitud= int(input("Por favor, ingrese la longitud de la base del triángulo en metros: "))
  altura_longitud=int(input("Por favor, ingrese la longitud de la altura del triángulo en metros: "))
  Area=base_longitud * altura_longitud /2
  return Area

medicion=area_triangulo()

if medicion is None:
  print("systanix error")
else:
  print("el resultado es:",medicion)

import numpy as np

def calculadora_de_estadisticas():
  try:
   lista= input("Ingresa una lista de números separados por comas: ")
   numeros_str = lista.split(',')
   numeros_enteros = [int(num_str) for num_str in numeros_str]

   for num in numeros_enteros:
      print(num)
  except ValueError:
    print("ingresa numeros validos")

  suma = sum(numeros_enteros)
  print("la suma es:",suma)

  promedio = np.mean(numeros_enteros)
  print("el promedio es:",promedio)

  maximo =max(numeros_enteros)
  print("el valor maximo de la lista es:",maximo)

  minimo = min(numeros_enteros)
  print("el valor minimo de la lista es:",minimo)

  desviacion_estandar= np.std(numeros_enteros)
  print("la desviacion estandar es:",desviacion_estandar)

  return lista,numeros_str,numeros_enteros,suma,promedio,maximo,minimo,desviacion_estandar

calculo =calculadora_de_estadisticas()


class perro:
  def __init__(self,nombre,raza):
    self.nombre = nombre
    self.raza = raza 
  
  def ladrar():
    return("¡Guau! ¡Guau! ")
  
  def presentarse(self):
    return(f"soy {self.nombre} de raza {self.raza}")
  
perro1 = perro("spoke","bulldogfrances")
perro2 = perro("jacob","pitbull")

ladrar1 = perro.ladrar()

print(perro1.presentarse())
print(ladrar1)

class circulo:
  def __init__(self,radio):
    self.radio = radio
  
  def calcular_area(self):
    pi = 3.14159
    area  = self.pi*self.radio**2
    return area,pi
  
  def calcular_perimetro(self):
    pi = 3.14159
    perimetro = 2*pi*self.radio
    return perimetro
  def escalar_radio(self):
    factor = 2 
    factor_escalado = factor * self.radio
    return factor,factor_escalado

calculo_circulo= circulo(5)
print(calculo_circulo.calcular_perimetro())
print(calculo_circulo.calcular_perimetro())
print(calculo_circulo.escalar_radio())

class Coche:
  def __init__(self,marca,modelo,año,velocidad_actual):
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.velocidad_actual = velocidad_actual

  def acelerar(self,arranque):
    arranque = self.velocidad_actual + 10 
    return (f"el coche acelera  a una velocidad {arranque} KM por hora")

  def frenar(self,frenazo):
    frenazo = self.velocidad_actual - 10
    return (f"el coche frena y queda en una velocidad de {frenazo}")
  
  def obtener_información(self):
    return(f"el coche es marca {self.marca} y es modelo  {self.modelo} el año de fabricacion {self.año} y tiene una velocidad actual de {self.velocidad_actual}  km por hora")


Coche_nuevo = Coche("chrevolet","seil",2013,40)
acelerar1 = Coche_nuevo.acelerar(40)
frenar1 = Coche_nuevo.frenar(40)
print(acelerar1)
print(frenar1)
print(Coche_nuevo.obtener_información())

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buzz")
  else:
    print(i)
      
  
def calculadora_de_propinas():
  factura = int(input(" ingrese el monto total de la factura: "))
  propina = int(input("ingresa el monto de dinero que desas dejar de propina: "))
  calculo = factura * propina / 100
  personas = int(input("ingrese el numero de personas que van a compartir la factura: "))
  pago_total = (factura + propina )// personas 
  print(f"el pago que cada persona debe hacer por individual es: {pago_total} pesos" )
  return factura,propina,calculo,personas,pago_total
cal = calculadora_de_propinas()


import math 
def numero_primo(numero):
   if numero <= 1:
        return False
   if numero <= 3:
        return True

   if numero % 2 == 0 or numero % 3 == 0:
        return False

   i = 5
   while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

   return True,numero

def fibonachi(numero):
  f = 5 * numero ** 2+4 
  i = 5 * numero **2-4
  b1 = math.sqrt(f)
  b2 = math.sqrt(i)
  if b2 * b1 == (numero + 4) or b2 * b2 == (numero - 4):
    return True
  else:
    return False
  return numero

def es_par(numero):
  if numero % 2 == 0:
    return True
  else:
    return False
  
  return numero 

prim = int(input("ingresa un numero entero positivo: "))
num_prim = numero_primo(prim)
fibo = fibonachi(prim)
par = es_par(prim)
if  num_prim and fibo and par:
  print(f"{prim} es primo , fibonachi y es par")
elif num_prim and not fibo and not par:
  print(f"{prim} es primo , no es fibonachi y no es par")
elif not num_prim and fibo and par:
  print(f"{prim} no es primo ,fibonachi y es par ")
elif not num_prim and not fibo and par:
  print(f"{prim} no es primo, no es fibonachi pero es par ")
elif num_prim and fibo and not par:
  print(f"{prim} es primo , fibonachi pero no es es par")
elif num_prim and not fibo and par:
  print(f"{prim} es primo, no es fibonachi, es par")
elif not num_prim and fibo and not par:
  print(f"{prim} no es primo, es fibonachi, no es par")
else:
  print(f"{prim} no es primo,ni es fibonachi y tampoco par")
  

#creamos la funcion 
def sombrero_seleccionador():
  #creamos las listas vacias
  Gryffindor = []
  Slytherin  = []
  Hufflepuff = []
  Ravenclaw = []
  #creamos las 4 preguntas
  pregunta1 = input("¿Cual es tu animal favorito?: a.Leon b.Serpiente c.Terron d.Aguila ") 
  if  pregunta1 ==  "a":
    Gryffindor.append(10)
  elif pregunta1 == "b":
    Slytherin.append(10)
  elif pregunta1 == "c":
    Hufflepuff.append(10)
  else:
    Ravenclaw.append(10)
  
  pregunta2 = input("Llega un troll a hogwarts ¿Ques es lo primero que haces?: a.lo enfrentas para que tu seas el unico herido y se salven los demas b. protegerte a ti y las tuyos, corres buscando un profesor para que los ayude c. peleas con el con ayuda pero quieres llevarte el credito d. encuentras una forma astuta para evitarlo y ala vez manternerlo controlado para que nadie salga herido")
  if  pregunta2 ==  "a":
    Gryffindor.append(10)
  elif pregunta2 == "b":
    Hufflepuff.append(10)
  elif pregunta2 == "c":
    Slytherin.append(10)
  else:
    Ravenclaw.append(10)
  
  pregunta3 = input("¿Cuales es tu materia  de Hogwarts favorita?: a.Herbologia b.Pociones c.Historia de magia d.Criaturas magicas ")
  if  pregunta3 ==  "a":
    Hufflepuff.append(10)
  elif pregunta3 == "b":
    Ravenclaw.append(10)
  elif pregunta3 == "c":
    Slytherin.append(10)
  else:
    Gryffindor.append(10)

  pregunta4 = input("¿Que cualidades valoras mas?: a.Honestidad,trabajo duro y paciencia  b.Osadia,lealtad,valentia  c.Originalidad,ingeno,intelgencia  d.ambicion,astucia,determinacion")
  if  pregunta4 ==  "a":
    Hufflepuff.append(10)
  elif pregunta4 == "b":
    Gryffindor.append(10)
  elif pregunta4 == "c":
    Ravenclaw.append(10)
  else:
    Slytherin.append(10)
    
  pregunta5 = input("¿Que harias si encuentras un cofre donde se escuchan gritos por dentro?: a.estudiarlo para ver si es un conjuro  b.darselo a un profesor el sabra que hacer c.abrirlo para ver que es  d.te lo llevas a escondidas te puede servir para algo")
  if  pregunta5 ==  "a":
    Ravenclaw.append(10)
  elif pregunta5 == "b":
    Hufflepuff.append(10)
  elif pregunta5 == "c":
    Gryffindor.append(10)
  else:
    Slytherin.append(10)
  pregunta6 = input("¿A que casa quieres pertenecer: a.Gryffindor b. Ravenclaw c.Slytherin d.Hufflepuff")
  if  pregunta6 ==  "a":
    Gryffindor.append(3)
  elif pregunta6 == "b":
    Ravenclaw.append(3)
  elif pregunta6 == "c":
    Slytherin.append(3)
  else:
    Hufflepuff.append(6)
  
  suma =  Gryffindor + Slytherin + Hufflepuff +Ravenclaw

  if Gryffindor > Slytherin and Gryffindor >  Hufflepuff and Gryffindor >  Ravenclaw:
    print("¡Gryffindor!, eres una persona valiente con mucho coraje y aparte de eso te destacas por ser caballeroso." )
  elif Slytherin > Gryffindor and  Slytherin  >  Hufflepuff and Slytherin > Ravenclaw:
    print("¡Slytherin!, eres alguien ambicioso al que no se conforma con nada  siempre vas  mas alla y tienes un plan astuto de conseguir lo que quieres.")
  elif  Hufflepuff >  Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
    print("¡Hufflepuff!, eres una persona leal,honesta te destacas por ser alguien trabajador.")
  elif Ravenclaw > Gryffindor and  Ravenclaw  >  Hufflepuff and Ravenclaw > Slytherin:
    print("!Ravenclaw!,eres alguien estudioso que siempre sabe que hacer incluso en los momentos mas dificiles ,eres resolutivo y creativo")
  else:
     adiccion_nueva_pregunta = input("De estas cuatro  cualidades ¿cual crees que tienes?: a.valiente b.amable c.resolutivo d.visionario")
     if  adiccion_nueva_pregunta ==  "a" :
       Gryffindor.append(10)
     elif adiccion_nueva_pregunta == "b": 
      Ravenclaw.append(10)
     elif adiccion_nueva_pregunta == "c":
      Slytherin.append(10)
     else:
      Hufflepuff.append(10)
  

  return Gryffindor,Slytherin, Hufflepuff,Ravenclaw,pregunta1,suma


harry = sombrero_seleccionador()

diccionario = {
    "a" : "Aurek",
    "b" : "Besh",
    "c" : "Cresh",
    "d" : "Dorn",
    "e" : "Esk",
    "f" : "Forn",
    "g" : "Grek",
    "h" : "Herf",
    "i" : "Isk",
    "J" : "Jenth",
    "k" : "Krill",
    "l" : "Leth",
    "m" : "Mern",
    "n" : "Nern",
    "o" : "Osk",
    "p" : "Peth",
    "q" : "Qek",
    "r" : "Resh",
    "s" : "Senth",
    "t" : "Trill",
    "u" : "Usk",
    "v" : "Vev",
    "w" : "Wesk",
    "x" : "Xesh",
    "y" : "Yirt",
    "z" : "Zerek",
    "ch" : "Cherek",
    "ae" : "Enth",
    "eo" : "Onith",
    "kh" : "Krenth",
    "ng" : "Nen",
    "oo" : "Shen",
    "sh" : "Shen",
    "th" : "Thesh",
    " "  : " "
    }
traduccion = input("ingresa cualquier texto o palabra y se traduce a Aurebesh:  ")
for track in traduccion:
  if track in diccionario:
    valor_correspondiente  = diccionario[track]
    print(valor_correspondiente,end='')
  else:
    print("syntasix Error: no des numeros solo texto")
    

diccionario ={
    "hola" : "h_ _ a",
    "almuerzo" : "a_m_ _r_ o",
    "pueblo" : "_ue_ _o"
 }
valor = diccionario.values()
lista_de_valores = list(diccionario.values())
valores_deseados = lista_de_valores[0]
print(valores_deseados)
user = input("dime la letras que faltan para completar la palabra: ")
while not user == "ol":
   print("Error intenta de nuevo")
   valor = diccionario.values()
   lista_de_valores = list(diccionario.values())
   valores_deseados = lista_de_valores[0]
   print(valores_deseados)
   user = input("dime la letras que faltan para completar la palabra: ")
else:
    print("felicidades atinaste la palabra es hola")

valor = diccionario.values()
lista_de_valores2 = list(diccionario.values())
valores_deseados2 = lista_de_valores[1]
print(valores_deseados2)
user = input("dime la letras que faltan para completar la palabra: ")
while not user == "luez":
   print("Error intenta de nuevo")
   valor = diccionario.values()
   lista_de_valores2 = list(diccionario.values())
   valores_deseados2 = lista_de_valores[1]
   print(valores_deseados2)
   user = input("dime la letras que faltan para completar la palabra: ")
else:
    print("felicidades atinaste la palabra es almuerzo")
valor = diccionario.values()
lista_de_valores3 = list(diccionario.values())
valores_deseados3 = lista_de_valores[2]
print(valores_deseados3)
user = input("dime la letras que faltan para completar la palabra: ")
while not user == "pbl":
   print("Error intenta de nuevo")
   valor = diccionario.values()
   lista_de_valores3 = list(diccionario.values())
   valores_deseados3 = lista_de_valores[2]
   print(valores_deseados3)
   user = input("dime la letras que faltan para completar la palabra: ")
else:
    print("felicidades atinaste la palabra es pueblo")
    
diccionario ={
    "hola" : "h_ _ a",
    "almuerzo" : "a_m_ _r_ o",
    "pueblo" : "_ue_ _o",
    "escapar" : "_sca_ar",
    "hogar"   : "h_ _ar",
    "pregonero" : "p_ _ gon_ro",
    "sociedad"  : "_oc_ _dad",
    "sol" : "s_l",
    "juventud" : "j_ _ _ntu_",
    "desierto" : "de_ _er_ _",
    "lluvia" : "_ _ uvi_",
    "par" : "p_r",
    "tiempo" : "ti_ _po",
    "normal" : "n_ _ ma_"
 }
lista_de_intentos = []
while not all(i in lista_de_intentos for i in range(1, 14)):
  valor = diccionario.values()
  lista_de_valores = list(diccionario.values())
  valores_deseados = lista_de_valores[0]
  print(valores_deseados)
  user = input("dime cual es la palabra correcta: ")
  if not user == "hola":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(1)
  else:
    print("felicidades atinaste la palabra es hola")

  valor = diccionario.values()
  lista_de_valores2 = list(diccionario.values())
  valores_deseados2 = lista_de_valores[1]
  print(valores_deseados2)
  user = input("dime cual es la palabra correcta: ")
  if not user == "almuerzo":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(2)
  else:
    print("felicidades atinaste la palabra es almuerzo")
  valor = diccionario.values()
  lista_de_valores3 = list(diccionario.values())
  valores_deseados3 = lista_de_valores[2]
  print(valores_deseados3)
  user = input("dime cual es la palabra correcta:  ")
  if  not user == "pueblo":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(3)
  else:
    print("felicidades atinaste la palabra es pueblo")
  valor = diccionario.values()
  lista_de_valores4 = list(diccionario.values())
  valores_deseados4 = lista_de_valores[3]
  print(valores_deseados4)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "escapar":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(4)
  else:
    print("felicidades atinaste la palabra es escapar")
  valor = diccionario.values()
  lista_de_valores5 = list(diccionario.values())
  valores_deseados5 = lista_de_valores[4]
  print(valores_deseados5)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "hogar":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(5)
  else:
    print("felicidades atinaste la palabra es hogar")
  valor = diccionario.values()
  lista_de_valores6 = list(diccionario.values())
  valores_deseados6 = lista_de_valores[5]
  print(valores_deseados6)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "pregonero":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(6)
  else:
    print("felicidades atinaste la palabra es pregonero")
  valor = diccionario.values()
  lista_de_valores7 = list(diccionario.values())
  valores_deseados7 = lista_de_valores[6]
  print(valores_deseados7)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "sociedad":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(7)
  else:
    print("felicidades atinaste la palabra es sociedad")
  valor = diccionario.values()
  lista_de_valores8 = list(diccionario.values())
  valores_deseados8 = lista_de_valores[7]
  print(valores_deseados8)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "sol":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(8)
  else:
    print("felicidades atinaste la palabra es sol")
  valor = diccionario.values()
  lista_de_valores9 = list(diccionario.values())
  valores_deseados9 = lista_de_valores[8]
  print(valores_deseados9)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "juventud":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(9)
  else:
    print("felicidades atinaste la palabra es juventud")
  valor = diccionario.values()
  lista_de_valores10 = list(diccionario.values())
  valores_deseados10 = lista_de_valores[9]
  print(valores_deseados10)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "desierto":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(10)
  else:
    print("felicidades atinaste la palabra es desierto")
  valor = diccionario.values()
  lista_de_valores11 = list(diccionario.values())
  valores_deseados11 = lista_de_valores[10]
  print(valores_deseados11)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "lluvia":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(11)
  else:
    print("felicidades atinaste la palabra es lluvia")
  valor = diccionario.values()
  lista_de_valores12 = list(diccionario.values())
  valores_deseados12 = lista_de_valores[11]
  print(valores_deseados12)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "par":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(12)
  else:
    print("felicidades atinaste la palabra es par")
  valor = diccionario.values()
  lista_de_valores13 = list(diccionario.values())
  valores_deseados13 = lista_de_valores[12]
  print(valores_deseados13)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "tiempo":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(13)
  else:
    print("felicidades atinaste la palabra es tiempo")
  valor = diccionario.values()
  lista_de_valores14 = list(diccionario.values())
  valores_deseados14 = lista_de_valores[13]
  print(valores_deseados14)
  user = input("dime cual es la palabra correcta: ")
  if  not user == "normal":
    print("Error la palabra no es esa,suerte ala proxima")
    lista_de_intentos.append(14)
  else:
    print("felicidades atinaste la palabra es normal")
  break
  print(lista_de_intentos)
if all(i in lista_de_intentos for i in range(1, 15)):
    print("Lo siento, perdiste. Gracias por jugar.")
elif not lista_de_intentos:
    print("¡Felicidades! No erraste en ninguna palabra.")
else:
    print(f"Felicidades, solo erraste en las preguntas {lista_de_intentos} ")

 
  
def codigo_konami():
  user = input("escribe una secuencia de botones de videojuego para a haber si puede sactivar el codigo konami  (coloca un boton ejemplo (arriba) y despues de una coma la otra ,(abajo)sin dejar ningun espacio ): ")
  if user == "arriba,arriba,abajo,abajo,izquierda,derecha,izquierda,derecha,B,A":
    print("codigo konami activado")
  else:
    print("error codigo incorrecto")
  return user
  
konami=codigo_konami()


lista = [[1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000, "-", "-", "-"],[100000,100000,100000,100000,100000,100000,100000,100000,100000, "-", "-", "-"],[10000,10000,10000,10000,10000,10000,10000,10000,10000, "-", "-", "-"],[1000,1000,1000,1000,1000,1000,1000,1000,1000, "-", "-", "-"],[100,100,100,100,100,100,100,100,100, "-", "-", "-"],[10,10,10,10,10,10,10,10,10, "-", "-", "-"],[1,1,1,1,1,1,1,1,1, "-", "-", "-"]]
millones = lista[0]
centenas_de_miles = lista[1]
decena_de_mil = lista[2]
unidad_de_mil= lista[3]
centena = lista[4]
decena = lista[5]
unidad = lista[6]

user= input("elige que unidades quieres operar = ")
if user == "millones":
  for i in range(0,len(millones)-2,11):
    millones[i+8],millones[i+11] = millones[i+11],millones[i+8]
  user2 = input("elige el otro sumando de unidad: ")
  if user2 == "centenas de miles":
     for i in range(0,len(centenas_de_miles)-2,11):
      centenas_de_miles[i+8],centenas_de_miles[i+11] = centenas_de_miles[i+11],centenas_de_miles[i+8]
      suma = centenas_de_miles[11] + millones[11]
      print(suma)
  elif user2 == "decenas de miles":
    for i in range(0,len(decena_de_mil)-2,11):
      decena_de_mil[i+8],decena_de_mil[i+11] = decena_de_mil[i+11],decena_de_mil[i+8]
      suma2 = decena_de_mil[11] + millones[11]
      print(suma2)
  elif user2 =="unidad  de mil":
    for i in range(0,len(unidad_de_mil)-2,11):
      unidad_de_mil[i+8],unidad_de_mil[i+11] = unidad_de_mil[i+11],unidad_de_mil[i+8]
      suma3 = unidad_de_mil[11] + millones[11]
      print(suma3)
  elif user2 == "centena":
    for i in range(0,len(centena)-2,11):
      centena[i+8],centena[i+11] = centena[i+11],centena[i+8]
      suma4 = centena[11] + millones[11]
      print(suma4)
  elif user2 == "decena":
    for i in range(0,len(decena)-2,11):
      decena[i+8],decena[i+11] = decena[i+11],decena[i+8]
      suma4 = decena[11] + millones[11]
      print(suma4)
  elif user2 == "unidad":
    for i in range(0,len(unidad)-2,11):
      unidad[i+8],unidad[i+11] = unidad[i+11],unidad[i+8]
      suma5 = unidad[11] + millones[11]
      print(suma5)
  elif user2 == "millones":
    suma6 = millones[11] + millones[11]
    print(suma6)

elif user == "centenas de miles":
  for i in range(0,len(centenas_de_miles)-2,11):
    centenas_de_miles[i+8],centenas_de_miles[i+11] = centenas_de_miles[i+11],centenas_de_miles[i+8]
  user2 = input("elige el otro sumando de unidad: ")
  if user2 == "millones":
     for i in range(0,len(centenas_de_miles)-2,11):
      millones[i+8],millones[i+11] = millones[i+11],millones[i+8]
      suma = centenas_de_miles[11] + millones[11]
      print(suma)
  elif user2 == "decenas de miles":
    for i in range(0,len(decena_de_mil)-2,11):
      decena_de_mil[i+8],decena_de_mil[i+11] = decena_de_mil[i+11],decena_de_mil[i+8]
      suma2 = decena_de_mil[11] + centenas_de_miles[11]
      print(suma2)
  elif user2 =="unidad  de mil":
    for i in range(0,len(unidad_de_mil)-2,11):
      unidad_de_mil[i+8],unidad_de_mil[i+11] = unidad_de_mil[i+11],unidad_de_mil[i+8]
      suma3 = unidad_de_mil[11] + centenas_de_miles[11]
      print(suma3)
  elif user2 == "centena":
    for i in range(0,len(centena)-2,11):
      centena[i+8],centena[i+11] = centena[i+11],centena[i+8]
      suma4 = centena[11] + centenas_de_miles[11]
      print(suma4)
  elif user2 == "decena":
    for i in range(0,len(decena)-2,11):
      decena[i+8],decena[i+11] = decena[i+11],decena[i+8]
      suma4 = decena[11] + centenas_de_miles[11]
      print(suma4)
  elif user2 == "unidad":
    for i in range(0,len(unidad)-2,11):
      unidad[i+8],unidad[i+11] = unidad[i+11],unidad[i+8]
      suma5 = unidad[11] + centenas_de_miles[11]
      print(suma5)
  elif user2 == "centenas de miles":
    suma6 = centenas_de_miles[11] + centenas_de_miles[11]
    print(suma6)
    
else:
  print("Syntaxis Error")
    