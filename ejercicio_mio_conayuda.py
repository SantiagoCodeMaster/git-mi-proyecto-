import random
def pierda_papel_tijera():
  metricas = { 
    "Tie" : 0,
    "jugador1" : 0,
    "jugador2" : 0
}
  juego = {
       (1,3) : "jugador1",
       (1,2) : "jugador2",
       (1,4) : "jugador1",
       (1,5) : "jugador2",
       (2,1) : "jugador1",
       (2,3) : "jugador2",
       (2,4) : "jugador2",
       (2,5) : "jugador1",
       (3,2) : "jugador1",
       (3,1) : "jugador2",
       (3,5) : "jugador1",
       (3,4) : "jugador2",
       (4,2) : "jugador1",
       (4,3) : "jugador1",
       (4,5) : "jugador2",
       (4,1) : "jugador1",
       (5,3) : "jugador2",
       (5,4) : "jugador1",
       (5,1) : "jugador1",
       (5,2) : "jugador2",
       (1,1) : "Tie",
       (2,2) : "Tie",
       (3,3) : "Tie",
       (4,4) : "Tie",
        (5,5) : "Tie"
  }
  for _ in range(10):  # Realiza el bucle n veces
    random_numbers = (random.randint(1, 5), random.randint(1, 5))
    game = juego.get(random_numbers, "Resultado no encontrado en el juego")
    print("Resultado de la partida :", random_numbers)
    if game == "Tie":
      print(game)
    else:
      print("Y el ganador es", game)
    
    if game == "Tie":
     metricas["Tie"] += 1 
    elif game == "jugador1":
     metricas["jugador1"] += 1
    else:
     metricas["jugador2"] += 1

  print(f"resultados finales: {metricas}")
  for jugador,victorias in metricas.items():
   if  victorias == 0:
    print(f"{jugador} tiene {victorias} ganadas ") 
   elif  victorias > 1:
    print(f"{jugador} tiene {victorias} ganadas ") 
   else:
      print(f"{jugador} tiene {victorias} ganada ")
  if metricas["jugador1"] > metricas["jugador2"]:
    print("El ganador es jugador1")
  elif metricas["jugador2"] > metricas["jugador1"]:
    print("El ganador es jugador2")
  else:
    print("Hubo un empate") 

  
       
  return  random_numbers,game,juego,metricas 

partida = pierda_papel_tijera()

def heterograma():
 texto = input("ingresa una cadena de texto: ")
 repetida = False
 letras_vistas = set()
 for heter in texto:
   if heter in letras_vistas:
    repetida = True
    break 
   letras_vistas.add(heter)

 if repetida:
   print(f"la cadena de texto ingresada {texto} no es heterograma ")
 else:
   print(f"la cadena de texto ingresada {texto} es heterograma")
  
 return texto,repetida,letras_vistas

texto_analizado = heterograma()

def isograma():
 texto2 = input("ingresa una cadena de texto: ")
 buleano = False
 for letra in texto2:
  if  texto2.count(letra) == 2:
    buleano = True
    break 
 if buleano:
  print(f"el texto ingresado {texto2} es isograma")

 else:
  print(f"el texto ingresado {texto2} no es isograma")

 return texto2,buleano

texto_analizado2 = isograma()
  

texto3 = input("ingresa una cadena de texto: ")
lista_abecedario = ["a","b","c", "d", "e", "f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v", "w","x","y","z"]
texto3 = texto3.lower()
verificacion = all(text in texto3 for text in lista_abecedario)
if verificacion:
  print(f"el texto {texto3} ingresado es un pangrama")
else:
  print(f"el texto {texto3} ingresado no  es un pangrama")


import numpy as np
inter = input("ingresa un texto mas o menos largo con puntuacion: ")
palabras = inter.split()
numero_de_palabras =[i + 1 for i in range(len(palabras))]
print(f"el numero de palabras es {numero_de_palabras[-1]}")
media_palabras = np.mean(numero_de_palabras)
print(f"la media del numero de palabras es {media_palabras} ")
oraciones = inter.split('.')
numero_oraciones = [i + 1 for i in range(len(oraciones))]
print(f"el numero de oraciones son {numero_oraciones[-1]}")


cifrado_de_cesar = {
    "a" : "b",
    "b" : "c",
    "c" : "d",
    "d" : "e",
    "e" : "f",
    "f" : "g",
    "g" : "h",
    "h" : "i",
    "i" : "j",
    "j" : "k",
    "k" : "l",
    "l" : "m",
    "m" : "n",
    "n" : "ñ",
    "ñ" : "o",
    "o" : "p",
    "p" : "q",
    "q" : "r",
    "r" : "s",
    "s" : "t",
    "t" : "u",
    "u" : "v",
    "v" : "w",
    "w" : "x",
    "x" : "y",
    "y" : "z",
    "z" : "a",  

    }
user = input("di un texto y te lo voy a dar como cifrado con clave uno de cesar: ")
for usus in user:
  if usus in cifrado_de_cesar:
    valor = cifrado_de_cesar[usus]
    print(valor,end='')
  else:
    print("error")

identificando = input("di un texto en el cifrado de cesar con clave 1 y te lo desifro: ")
cifrado_invertido = {valor:clave for clave,valor in cifrado_de_cesar.items()}
for cifrado in identificando:
  if cifrado in cifrado_invertido:
    valores = cifrado_invertido.get(cifrado)
    print(valores,end='')
  else:
    print("error")
     

import time
def cuenta_regresiva(numero):
  if isinstance(numero, str):
    print("ERROR systnaxis invalida") 
  elif  numero < 0:
    print("ERROR numero invalido")
  else:
    while numero > 0:
        numero -= 1
        print(numero)
        time.sleep(2)
        if numero == 0:
          print("booommm se siente que viene diciembre gozate lo que queda 🎵🎶🎼 colegiala,colgiala ")

cuenta_regresiva(12)

