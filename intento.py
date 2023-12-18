import random 
class juego_de_tenis:
  def __init__(self,gano,perdio,deuce,love):
    self.gano = gano
    self.perdio = perdio
    self.deuce = deuce
    self.love = love

  def juego_partidas(self):
    self.gano = []
    self.perdio =[]
    self.deuce = []
    self.love = []
    game = [[random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1)]]
    p1_1 = game[0][0]
    p2_1 = game[0][1]
    p1_2 = game[1][0]
    p2_2 = game[1][1]
    p1_3 = game[2][0]
    p2_3 = game[2][1]
    if  p1_1 > 0 and p2_1  == 0:
      self.gano.append(1)
      print(f"p1_1 {self.gano}")
    return game, p1_1, p2_1 ,p1_2, p2_2,p1_3,p2_3

juego1 = juego_de_tenis("gana partida","perdio partida","deuce","love")
desarrollo_de_juego, _, _, _, _, _, _ = juego1.juego_partidas()
print(desarrollo_de_juego)