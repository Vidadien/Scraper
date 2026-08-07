acciones=["ACCIONES GLOBAL", "ACCIONES COLOMBIA"]
renta=["RENTA FIJA GLOBAL", "RENTA FIJA PESOS", "SOSTENIBLE GLOBAL"]
estable=["CAPITAL", "ESTABLE"]
diver=["DIVER DINAMICO", "DIVER MODERADO", "DIVER CONSERVADOR"]
internacional=["LIQUIDEZ DOLAR", "FINCA RAIZ INTERNACIONAL", "ORO"]
favoritos=["ACCIONES COLOMBIA", "RENTA FIJA PESOS", "CAPITAL", "DIVER CONSERVADOR"]
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from pathlib import Path
archivo = Path(__file__).parent / "fondos.csv"
df = pd.read_csv(archivo)
print("1. Resumen de los fondos")
print("2. regresión cúbica Acciones colombia")
respuesta = input("Seleccione una opción: ")
if respuesta == "1":
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
if respuesta == "2":
    datos=df["ACCIONES COLOMBIA"]/df["ACCIONES COLOMBIA"].iloc[0]
    n=5
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