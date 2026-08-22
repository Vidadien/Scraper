import pandas as pd
import numpy
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates
acciones=["ACCIONES GLOBAL", "ACCIONES COLOMBIA"]
renta=["RENTA FIJA GLOBAL", "RENTA FIJA PESOS", "SOSTENIBLE GLOBAL"]
estable=["CAPITAL", "ESTABLE"]
diver=["DIVER DINAMICO", "DIVER MODERADO", "DIVER CONSERVADOR"]
internacional=["LIQUIDEZ DOLAR", "FINCA RAIZ INTERNACIONAL", "ORO"]
favoritos=["ACCIONES COLOMBIA", "RENTA FIJA PESOS", "CAPITAL", "DIVER CONSERVADOR"]
lista=[acciones, renta, estable, diver, internacional, favoritos]
nombres=["Acciones", "Renta Fija", "Estable", "Diversificación", "Internacional", "Favoritos"]
archivo = Path(__file__).parent / "fondos.csv"
df = pd.read_csv(archivo)
print("1. Resumen de los fondos")
print("2. regresión cúbica Acciones colombia")
respuesta = input("Seleccione una opción: ")
if respuesta == "1":
    fig, axs = plt.subplots(2,3, figsize=(12, 8), sharex=True)
    for i in range(6):
        fondo=lista[i]
        for f in fondo:
            axs[i//3,i%3].plot(df["Fecha"], df[f]/df[f].iloc[0], label=f)
            axs[i//3,i%3].set_title(nombres[i])
            axs[i//3,i%3].legend()
            axs[i//3,i%3].tick_params(axis='x', labelrotation=90)
            axs[i//3,i%3].xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.show()
if respuesta == "2":
    datos=df["ACCIONES COLOMBIA"]/df["ACCIONES COLOMBIA"].iloc[0]
    n=3
    diseno=numpy.zeros((len(df),n+1))
    diseno[:,0]=1
    for i in range(1,n+1):
        diseno[:,i]=numpy.arange(1-len(df),1)**i
    sim=diseno.T @ diseno
    sim_inv=numpy.linalg.inv(sim)
    beta=sim_inv @ diseno.T @ datos
    err=datos - diseno @ beta
    s=numpy.sum(err**2)/(len(df)-n-1)
    cov=s*sim_inv
    incertidumbre=numpy.sqrt(numpy.diag(cov))
    wald=beta/ incertidumbre
    print("wald:", wald)
    plt.plot(df["Fecha"], datos, label="Datos")
    plt.plot(df["Fecha"], diseno @ beta, label=f"${beta[0]:.5f} + {beta[1]:.5f}x + {beta[2]:.5f}x^2 + {beta[3]:.5f}x^3$")
    plt.tick_params(axis='x', labelrotation=90)
    plt.title("Regresión cúbica Acciones Colombia")
    plt.xlabel("Fecha")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()