import numpy as np 
import scipy as sc
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

#crear el dataset 
n = 500
p = 2 
x,y = make_circles(n_samples =n ,factor = 0.5,noise = 0.05)
y = y[:,np.newaxis]
plt.scatter(x[y[:,0] == 0,0],x[y[:,0] == 0,1],c="skyblue")
plt.scatter(x[y[:,0] == 1,0],x[y[:,0] == 1,1],c="salmon")
plt.axis("equal")
plt.show()
import random 
#clase de la capa de la red 
class neuronal_layer():
  def __init__(self,n_conn,n_neur,act_f):
    self.act_f =  act_f
    self.b = np.random.rand(1,n_neur)  *2 -1
    self.w = np.random.rand(n_conn,n_neur)  *2 -1


sigm = (lambda x : 1 /(1 + np.e **(-x)),

         lambda x: x * (1 - x))
     
relu = lambda x : np.maximum(0,x)

_x = np.linspace(-5,5,100)
plt.plot(_x,relu(_x))


l0 = neuronal_layer(p,4,sigm)
l1 = neuronal_layer(4,8,sigm)
# ...

l0 = neuronal_layer(p,4,sigm)
l1 = neuronal_layer(4,8,sigm)
# ...

def create_nn(topology,act_fun):
  nn = []
  for l,layer  in enumerate(topology[:-1]):
    nn.append(neuronal_layer(topology[l],topology[l+1],act_fun))
  return nn 


topology  = [p,4,8,16,8,4,1]
nuronal_net = create_nn(topology,sigm)
l2_cost = (lambda yp,yr: np.mean((yp -yr)**2),
          lambda yp ,yr: (yp-yr)) 

def train(nuronal_net,x,y,l2_cost,lr=0.5,train=True):

  out = [(None, x)]

  #forward pass 
  for l,layer in enumerate(nuronal_net):
   z = out[-1][1] @ nuronal_net[l].w + nuronal_net[l].b
   a = nuronal_net[l].act_f[0](z)
 

   out.append((z,a))
  

  if train:

    #prograpagacion para atras 
    delta = []

    for l in reversed(range(0,len(nuronal_net))):

      z= out[l+1][0]
      a= out[l+1] [1]
      


      if l == len(nuronal_net) - 1:
        #calcular delta ultima capa 
        delta.insert(0,l2_cost[1](a,y) * nuronal_net[l].act_f[1](a))
      else:
        #calcular delta sobre las capas  siguientes 
        delta.insert(0,delta[0] @ _w.T * nuronal_net[l].act_f[1](a))


      _w = nuronal_net[l].w 
      #decenso del gradiente
      nuronal_net[l].b = nuronal_net[l].b - np.mean(delta[0],axis = 0,keepdims=True)* lr 
      nuronal_net[l].w = nuronal_net[l].w - out[l][1].T @ delta[0]* lr 
    
  return out[-1][1]








train(nuronal_net,x,y,l2_cost,0.5)


  
