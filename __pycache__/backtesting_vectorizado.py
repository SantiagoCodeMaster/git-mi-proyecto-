import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib as mlp
import matplotlib.pyplot as plt  
import warnings 
warnings.filterwarnings("ignore")


#INDICE DE SORTINO 
#preparar los datos 
f = yf.download("TSLA", end="2023-09-01")
return_serie = f["Adj Close"].pct_change(1).dropna()
return_serie.name = "return"

#calculamos el indice de sortino 
mean = np.mean(return_serie)#para anulizarlos damos los dias que se matiene abierta la bolsa por año (252)
vol = np.std(return_serie[return_serie<0])#para terminar esta ecuacion luego se hace la raiz cuadrada 252 
sortino = np.sqrt(252)*mean/vol

print(f"sortino: {'%.3f' % sortino}")


#CALCULAR BETA 
sp500 = yf.download("^GSPC")["Adj Close"].pct_change(1)
sp500.name = "sp500"

#concatenamos para hacer la coravianza 
val = pd.concat((return_serie,sp500),axis=1).dropna()

#calculamos la matriz de covarianza 
cov_var_mat = np.cov(val.values, rowvar=False)

#calculamos beta 
cov = cov_var_mat[0][1]
var = cov_var_mat[1][1]

beta = cov/var 

print(f"Beta:{'%.3f' % beta}")


#CALCULAR ALPHA 
alpha = (252*mean*(1-beta))*100
print(f"Alpha:{'%.1f'% alpha} %")

#DRAWDOWN enteder el riesgo maxima de la estrategia mide el rendimiento en cuanto es lo maximo que podemos perder 
def drawdown_function(serie):
    
    #suma de los rendimientos 
   cum = serie.dropna().cumsum()+1
    # Calculamos el máximo de la suma en el período (máximo acumulado) # (1,3,5,3,1) --> (1,3,5,5,5)
   running_max = np.maximum.accumulate(cum)
   # calculo del drawdown 
   drawdown = cum/running_max -1 
   return drawdown
  
drawdown = drawdown_function(return_serie)


plt.figure(figsize=(18,8))

# Representar el drawdown
plt.fill_between(drawdown.index, drawdown*100, 0,
                 drawdown, color="#CE5757", alpha=0.65)

plt.title("drawdown")
plt.ylabel("Drawdown en %")
plt.show()

#maxima de perdida de tesla 
max_drawdrown = - np.min(drawdown)*100
print(f"max drawdown:{'%.1f'% max_drawdrown}%")

def BackTest(serie, annualiazed_scalar=252):

  # Importar el benchmark
  sp500 = yf.download("^GSPC")["Adj Close"].pct_change(1)
  
  # Cambiar el nombre
  sp500.name = "SP500"

  # Concatenar los retornos y el sp500
  val = pd.concat((serie,sp500), axis=1).dropna()
  # Calcular el drawdown
  drawdown = drawdown_function(serie)*100
  
  # Calcular el max drawdown
  max_drawdown = -np.min(drawdown)




  # Put a subplots
  fig, (cum, dra) = plt.subplots(1,2, figsize=(20,6))
  
  # Put a Suptitle
  fig.suptitle("Backtesting", size=20)

  # Returns cumsum chart
  cum.plot(serie.cumsum()*100, color="#39B3C7")

  # SP500 cumsum chart
  cum.plot(val["SP500"].cumsum()*100, color="#B85A0F")

  # Put a legend
  cum.legend(["Portfolio", "SP500"])
  
  # Set individual title
  cum.set_title("Cumulative Return", size=13)

  cum.set_ylabel("Cumulative Return %", size=11)

  # Put the drawdown
  dra.fill_between(drawdown.index,0,drawdown, color="#C73954", alpha=0.65)

  # Set individual title
  dra.set_title("Drawdown", size=13)

  dra.set_ylabel("drawdown en %", size=11)

  # Plot the graph
  plt.show()


  # Calcular el índice sortino
  sortino = np.sqrt(annualiazed_scalar) * serie.mean()/serie.loc[serie<0].std()

  # Calcular el índice  beta
  beta = np.cov(val[["return", "SP500"]].values,rowvar=False)[0][1] / np.var(val["SP500"].values)

  # Calcular el índice  alpha
  alpha = annualiazed_scalar * (serie.mean() - beta*serie.mean())

  # Imprimir los estadísticos
  print(f"Sortino: {np.round(sortino,3)}")
  print(f"Beta: {np.round(beta,3)}")
  print(f"Alpha: {np.round(alpha*100,3)} %")
  print(f"MaxDrawdown: {np.round(max_drawdown,3)} %")
  
  
BackTest(return_serie, annualiazed_scalar=252)

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

BackTest(dfc, 252)