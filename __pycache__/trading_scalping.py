
import pandas as pd
import numpy as np
import yfinance as yf
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import ta
import warnings
warnings.filterwarnings("ignore")


# El código aquí te permitirá cambiar los gráficos a modo oscuro para aquellos que optéis por programar en modo oscuro
import matplotlib.pyplot as plt

import matplotlib as mpl
from matplotlib import cycler
colors = cycler('color',
                ['#669FEE', '#66EE91', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('figure', facecolor='#313233')
plt.rc('axes', facecolor="#313233", edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors,
       labelcolor='gray')
plt.rc('grid', color='474A4A', linestyle='solid')
plt.rc('xtick', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('legend', facecolor="#313233", edgecolor="#313233")
plt.rc("text", color="#C9C9C9")
plt.rcParams['figure.figsize'] = [20, 8]

#importamos en yahoo finance 
df= yf.download("EURUSD=x", start="2010-01-01")

#cambiamos las fechas de indice date a numeros que cambiar dia a dia para representar las velas 
df['Date'] = pd.to_datetime(df.index)
df['Date'] = df['Date'].apply(mpl_dates.date2num)


#soporte y resistencia 
#creamos dos columnas vacias 

df["soporte"] = np.nan
df["resistencia"] = np.nan

#Después de 5 descensos consecutivos del mínimo, anotamos este precio como el soporte
df.loc[(df["Low"].shift(5) > df["Low"].shift(4))&
       (df["Low"].shift(4) > df["Low"].shift(3))&
       (df["Low"].shift(3) > df["Low"].shift(2))&
       (df["Low"].shift(2) > df["Low"].shift(1))&
       (df["Low"].shift(1) > df["Low"].shift(0)), "soporte"] = df["Low"]

#Después de 5 subidas consecutivas del máximo, observamos este precio como la resistencia      
df.loc[(df["High"].shift(5) < df["High"].shift(4))&
       (df["High"].shift(4) < df["High"].shift(3))&
       (df["High"].shift(3) < df["High"].shift(2))&
       (df["High"].shift(2) < df["High"].shift(1))&
       (df["High"].shift(1) < df["High"].shift(0)), "resistencia"] = df["High"]

print(df)

df_bis = df.loc["2019-01"]

#inicializar el grafico 
fig,ax =plt.subplots()

#dibujar los graficos de velas 
candlestick_ohlc(ax,df_bis[["Date","Open","High","Low","Close"]].values,width=0.6, \
       colorup='#57CE95', colordown='#CE5757', alpha=0.8) 

#poner la fecha como eje x
date_format =mpl_dates.DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
fig.tight_layout()

#represetamos la resistencia atravez de una linea
for resistencia,date in zip (df_bis["resistencia"].dropna(),df_bis["resistencia"].dropna().index):
       plt.hlines(resistencia,xmin=date,xmax=df_bis.index[-1],colors='#CE5757',linestyles=":", linewidth=3)
       

#represetamos el soporte atravez de una linea
for soporte,date in zip (df_bis["soporte"].dropna(),df_bis["soporte"].dropna().index):
       plt.hlines(soporte,xmin=date,xmax=df_bis.index[-1],colors='#CE5757',linestyles=":", linewidth=3)


# Representar líneas de resistencia
plt.plot(df["soporte"].fillna(method="ffill"),color='#CE5757', linestyle=":", linewidth=3)


# Representar líneas de soporte
plt.plot(df["resistencia"].fillna(method="ffill"),color='#57CE95', linestyle=":", linewidth=3)

# Mostrar la figura
fig.show()

#estrategia con soportes y resistencia (solo funciona en scalping cuando hay muchos datos)
#señal
df["signal"] = 0

#suavizar soporte y resistencia 
df["smooth_resistencia"] = df["resistencia"].fillna(method="ffill")
df["smooth_soporte"] = df["soporte"].fillna(method="ffill")


#creamos la condicion de compra 
condition_1_buy = (df["Close"].shift(1) < df["smooth_resistencia"].shift(1))&\
              (df["smooth_resistencia"]*(1+0.0/100)<df["Close"])

# Corrección para la condición de venta
condition_1_sell = (df["Close"].shift(1) > df["smooth_soporte"].shift(1)) & \
                  (df["smooth_soporte"] * (1 + 0.0/100) > df["Close"])



#colocar la señal 
df.loc[condition_1_buy, "signal"] = 1
df.loc[condition_1_sell, "signal"] = -1

duration = 5 

#calculamos el porcentaje 
df["ptc"] = df["Close"].pct_change(1)
#calculamos el porcentaje de beneficio de nuestra estrategia en 5 dias anteriores 
df["return"] = np.array([df["ptc"].shift(i)for i in range(duration)]).sum(axis=0)*(df["signal"].shift(duration))
df["return"].cumsum().plot(figsize=(15,8))

#COMBIANCION  DE LA ESTRATEGIA SMA CON SOPORTE Y RESISTENCIA 
df["SMA fast"] = df["Close"].rolling(30).mean()
df["SMA slow"] = df["Close"].rolling(60).mean()

condition_2_buy = df["SMA fast"] > df["SMA slow"]
condition_2_sell = df["SMA fast"] <  df["SMA slow"]

df["signal"] = 0

df.loc[condition_1_buy & condition_2_buy, "signal"] = 1
df.loc[condition_1_sell & condition_2_sell,"signal"] = -1

df["ptc"] = df["Close"].pct_change(1)
df["return"] = np.array([df["ptc"].shift(i)for i in range(duration)]).sum(axis=0)*(df["signal"].shift(duration))
df["return"].cumsum().plot(figsize=(15,8))



df["rsi"] = ta.momentum.RSIIndicator(df["Close"],window =10).rsi()

#rsi de ayer 
df["rsi yesterday"]= df["rsi"].shift(1)

df["signal"] = 0

condition_3_buy = df["rsi"]  < df["rsi yersterday"]
condition_3_sell = df["rsi"] > df["rsi yesterday"]

df.loc[condition_1_buy & condition_2_buy & condition_3_buy,"signal"]= 1
df.loc[condition_1_sell & condition_2_sell & condition_3_sell,"signal"]= -1


df["ptc"] = df["Close"].pct_change(1)
df["return"] = np.array([df["ptc"].shift(i)for i in range(duration)]).sum(axis=0)*(df["signal"].shift(duration))
df["return"].cumsum().plot(figsize=(15,8))

def support_resistance(df, duration=5,spread=0):
  """EL DATAFRAME NECESITA TENER los siguientes nombres de columna: alta, baja, cierre"""

  # Support and resistance building
  df["support"] = np.nan
  df["resistance"] = np.nan

  df.loc[(df["low"].shift(5) > df["low"].shift(4)) &
        (df["low"].shift(4) > df["low"].shift(3)) &
        (df["low"].shift(3) > df["low"].shift(2)) &
        (df["low"].shift(2) > df["low"].shift(1)) &
        (df["low"].shift(1) > df["low"].shift(0)), "support"] = df["low"]


  df.loc[(df["high"].shift(5) < df["high"].shift(4)) &
  (df["high"].shift(4) < df["high"].shift(3)) &
  (df["high"].shift(3) < df["high"].shift(2)) &
  (df["high"].shift(2) < df["high"].shift(1)) &
  (df["high"].shift(1) < df["high"].shift(0)), "resistance"] = df["high"]


  # Create Simple moving average 30 days
  df["SMA fast"] = df["close"].rolling(30).mean()

  # Create Simple moving average 60 days
  df["SMA slow"] = df["close"].rolling(60).mean()

  df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=10).rsi()

  # RSI yersteday
  df["rsi yersteday"] = df["rsi"].shift(1)

  # Create the signal
  df["signal"] = 0

  df["smooth resistance"] = df["resistance"].fillna(method="ffill")
  df["smooth support"] = df["support"].fillna(method="ffill")


  condition_1_buy = (df["close"].shift(1) < df["smooth resistance"].shift(1)) & \
                    (df["smooth resistance"]*(1+0.5/100) < df["close"])
  condition_2_buy = df["SMA fast"] > df["SMA slow"]

  condition_3_buy = df["rsi"] < df["rsi yersteday"]

  condition_1_sell = (df["close"].shift(1) > df["smooth support"].shift(1)) & \
                    (df["smooth support"]*(1+0.5/100) > df["close"])
  condition_2_sell = df["SMA fast"] < df["SMA slow"]

  condition_3_sell = df["rsi"] > df["rsi yersteday"]



  df.loc[condition_1_buy & condition_2_buy & condition_3_buy, "signal"] = 1
  df.loc[condition_1_sell & condition_2_sell & condition_3_sell, "signal"] = -1


  # Calculamos las ganancias
  df["pct"] = df["close"].pct_change(1)

  df["return"] = np.array([df["pct"].shift(i) for i in range(duration)]).sum(axis=0) * (df["signal"].shift(duration))
  df.loc[df["return"]==-1, "return"] = df["return"]-spread
  df.loc[df["return"]==1, "return"] = df["return"]-spread


  return df["return"]

def preprocessing_min(name):

  df = pd.read_csv(name,delimiter="\t",index_col=["",""],parse_dates=True).dropna()

  df = df.iloc[:,:-2]

  df.columns = ["Open","High","Low","Close","Volumen"]

  return df
