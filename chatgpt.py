def expresion_matematica():
  user = input("ingrese una expresion matematica: ")
  numerador = user.split()
  if len(numerador) <= 10:
    numero1 = int(numerador[0])
    numero2 = int(numerador[2])
    operador = numerador[1]
    lista = [numero1, operador, numero2]
    print(True)
  else:
    print("syntaxis Error operacion erronea")