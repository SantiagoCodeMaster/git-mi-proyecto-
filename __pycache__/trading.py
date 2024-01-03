import numpy as np
import pandas as pd 
import yfinance as yf 
import matplotlib as mlp 
import warnings 
warnings.filterwarnings("ignore")


import matplotlib.pyplot as plt 

from matplotlib import cycler 

colors  = cycler('color',
                   ['#669FEE', '#66EE91', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'
                       ])
    
plt.rc('figure', facecolor='#313233')
plt.rc('axes', facecolor="#313233", edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors,
       labelcolor='gray')

plt.rc('grid', color='474A4A', linestyle='solid')
plt.rc('xtick', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('legend', facecolor="#313233", edgecolor="#313233")
plt.rc("text", color="#C9C9C9")

#funcion de procesamiento de datos 

def preprocessing(name): 
    
    #importar los datos 
    df = pd.read_csv(name,delimiter="\t",index_col=0 ,parse_dates=True).dropna()
    
    #eliminar las ultimas dos columnas 
    df = df.iloc[:,:-2]
    
    #renombrar
    df.columns = ["open","high","low","close","volume"]
    df.index.name = "time"
    
    return df 

#funcion de procesamiento de datos desde yahoo finance 
def preprocessing_yf(symbol):
    
   #importat los datos 
   df = yf.download(symbol).dropna()
   
   #renombrar 
   df.columns =["open","high","low","close","adj close","volume"]
   
   #eliminar la columna ajd close
   del df["adj close"]
   
   return df 


df = preprocessing_yf("EURUSD=X")


#creamos la media movil simple de 30 dias 
df["SMA fast"] = df["close"].rolling(30).mean()
df["SMA slow"] = df["close"].rolling(60).mean()


#mostramos el resultado en un grafico 
df[["close","SMA fast","SMA slow"]].plot(figsize=(15,8))

# grafico del 2023 o cualquier año 

df[["close","SMA fast","SMA slow"]].loc["2023"].plot(figsize=(15,8))


#empezamos a condicionar nuestra estrategia 
df["position"]=np.nan

df.loc[(df["SMA fast"] > df["SMA slow"]), "position"] = 1
df.loc[(df["SMA fast"] < df["SMA slow"]), "position"] = -1


#representamos toda la señal para que sea correcta 

year = "2023"

# Seleccionar toda la señal en una lista de índices para representar sólo estos puntos
idx_open = df.loc[df["position"]==1].loc[year].index
idx_close = df.loc[df["position"]==-1].loc[year].index

#ponemos el tamaño del grafico 
plt.figure(figsize=(15,6))

#representamos los puntos de señal posible compra y venta  larga 'open' en verde  y 'sell' en rojo 
plt.scatter(idx_open,df.loc[idx_open]["close"].loc[year],color="#57CE95",marker="^")
plt.scatter(idx_close, df.loc[idx_close]["close"].loc[year], color= "red", marker="v")

# Representar la resistencia para asegurarse de que las condiciones se completan
plt.plot(df["close"].loc[year].index, df["close"].loc[year], alpha = 0.35)
plt.plot(df["close"].loc[year].index, df["SMA fast"].loc[year], alpha = 0.35)
plt.plot(df["close"].loc[year].index, df["SMA slow"].loc[year], alpha = 0.35)

plt.show()

#calcular el pocentaje de variacion del activo desde el dia que abre hasta el momento del cierre 
df["pct"] = df["close"].pct_change(1)
#calcular la rentabilidad de la estrategia 
df["return"] = df["pct"] * df["position"].shift(1)

df["return"].plot(figsize=(15,8))

# Balance dirario (1%, 3%, -1%, -2%, 2%, 3%) -- > Balance acumulado (1%, 4%, 3%, 1%, 3%, 6%)

df["return"].cumsum().plot(figsize =(15,8))


#AUTOMATIZACION 
def SMA_estrategia(input, mt5=False, yf=False):

  if mt5:
    df = preprocessing(input)
  
  if yf:
    df = preprocessing_yf(input)

  
  # Crear resistencia mediante un máximo rodante
  df["SMA fast"] = df["close"].rolling(30).mean()

  # Crear soporte mediante un mínimo rodante
  df["SMA slow"] = df["close"].rolling(60).mean()

  df["position"] = np.nan

  # Crear la condición
  df.loc[(df["SMA fast"] > df["SMA slow"]) , "position"] = 1
  df.loc[(df["SMA fast"] < df["SMA slow"]) , "position"] = -1

  df["pct"] = df["close"].pct_change(1)

  # Calcular la rentabilidad de la estrategia

  df["return"] = df["pct"] * (df["position"].shift(1))
  

  return df["return"]

       
SMA_estrategia("/content/EURUSD_D1.csv", mt5=True).cumsum().plot(figsize=(15,8))
SMA_estrategia("EURUSD=X", yf=True).cumsum().plot(figsize=(15,8)) 

#comparacion 
yahoo = SMA_estrategia("EURUSD=X",yf=True)
metatrader = SMA_estrategia("/content/EURUSD_D1.csv", mt5=True)

returns = pd.DataFrame([yahoo,metatrader],index=["yahoo","broker"]).transpose().dropna().cumsum(axis=0)

#representamos el grafico 
#adaptamos el tamaño 
plt.figure(figsize=(20,8))

#representamos el entorno para la comparacion 
plt.plot(returns["yahoo"]*100,label="yahoo")
plt.plot(returns["broker"]*100,label="metatrader")

#titulo y nombre de los ejes 
plt.xlabel("tiempo",size=15)
plt.ylabel("% de beneficios",size=15)
plt.title("diferencia entre las estrategias sobre el mismo activo pero con datos diferentes", size=20)

#leyenda
plt.legend()
plt.show()
