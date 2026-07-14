acciones=["ACCIONES GLOBAL", "ACCIONES COLOMBIA"]
renta=["RENTA FIJA GLOBAL", "RENTA FIJA PESOS"]
estable=["CAPITAL", "ESTABLE", "SOSTENIBLE GLOBAL"]
diver=["DIVER DINAMICO", "DIVER MODERADO", "DIVER CONSERVADOR"]
internacional=["LIQUIDEZ DOLAR", "FINCA RAIZ INTERNACIONAL", "ORO"]
favoritos=["ACCIONES COLOMBIA", "RENTA FIJA PESOS", "CAPITAL", "DIVER CONSERVADOR"]
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
archivo = Path(__file__).parent / "fondos.csv"
df = pd.read_csv(archivo)
fig, axs = plt.subplots(2,3, figsize=(12, 8), sharex=True)
for fondo in acciones:
    axs[0,0].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[0,0].set_title("Acciones")
    axs[0,0].legend()
    axs[0,0].tick_params(axis='x', labelrotation=90)
for fondo in renta:
    axs[0,1].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[0,1].set_title("Renta Fija")
    axs[0,1].legend()
    axs[0,1].tick_params(axis='x', labelrotation=90)
for fondo in estable:
    axs[0,2].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[0,2].set_title("Estable")
    axs[0,2].legend()
    axs[0,2].tick_params(axis='x', labelrotation=90)
for fondo in diver:
    axs[1,0].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[1,0].set_title("Diversificación")
    axs[1,0].legend()
    axs[1,0].tick_params(axis='x', labelrotation=90)
for fondo in internacional:
    axs[1,1].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[1,1].set_title("Internacional")
    axs[1,1].legend()
    axs[1,1].tick_params(axis='x', labelrotation=90)
for fondo in favoritos:
    axs[1,2].plot(df["Fecha"], df[fondo]/df[fondo].iloc[0], label=fondo)
    axs[1,2].set_title("Favoritos")
    axs[1,2].legend()
    axs[1,2].tick_params(axis='x', labelrotation=90)
plt.show()
