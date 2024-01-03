import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import warnings
warnings.filterwarnings("ignore")
import yfinance as yf

# Importar los datos
df = yf.download("GOOG")
df.columns
# Renombrar las columnas
df = df[["Adj Close"]]
df.columns = ["close"]
df

# Media móvil simple
df["SMA 15"] = df[["close"]].rolling(15).mean().shift(1)
df["SMA 60"] = df[["close"]].rolling(60).mean().shift(1)

print(df)

df[["SMA 15", "SMA 60", "close"]].loc["2010"].plot(figsize=(15,8))

# Volatilidad del Retorno
df["returns"] = df["close"].pct_change(1)

df["MSD 15"] = df[["returns"]].rolling(15).std().shift(1)
df["MSD 60"] = df[["returns"]].rolling(60).std().shift(1)
df[["MSD 15", "MSD 60", "returns"]].loc["2010"].plot(figsize=(15,8))