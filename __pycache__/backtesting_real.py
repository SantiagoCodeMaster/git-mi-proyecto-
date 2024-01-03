import numpy as np
import pandas as pd 
import yfinance as yf 
import matplotlib as mlp 
import warnings 
import backtesting_vectorizado as bv
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



#el real backtesting de nuestra estrategia 

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


def preprocessing_yf(symbol):
  
  #Import the data
  df = yf.download("EURUSD=X").dropna()

  #Rename
  df.columns = ["open", "high", "low", "close", "adj close", "volume"]
  df.index.name = "time"

  # Remove adj close
  del df["adj close"]

  return df


def preprocessing(name): 
    
    #importar los datos 
    df = pd.read_csv(name,delimiter="\t",index_col=0 ,parse_dates=True).dropna()
    
    #eliminar las ultimas dos columnas 
    df = df.iloc[:,:-2]
    
    #renombrar
    df.columns = ["open","high","low","close","volume"]
    df.index.name = "time"
    
    return df 


#YAHOO 
dfc = SMA_estrategia("EURUSD=x", yf = True).loc["2012":]-0.00001

bv.BackTest(dfc, 252)