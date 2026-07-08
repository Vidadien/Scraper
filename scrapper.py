from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
from datetime import datetime
fondos=["CAPITAL","ACCIONES GLOBAL","DIVER DINAMICO","RENTA FIJA GLOBAL","RENTA FIJA PESOS","ACCIONES COLOMBIA",
        "DIVER MODERADO","ESTABLE","LIQUIDEZ DOLAR","SOSTENIBLE GLOBAL","FINCA RAIZ INTERNACIONAL","ORO","DIVER CONSERVADOR"]
archivo = Path(__file__).parent / "fondos.csv"
if archivo.exists():
    df = pd.read_csv(archivo)
else:
    columnas = ["Fecha"] + fondos
    df = pd.DataFrame(columns=columnas)
    df.to_csv(archivo, index=False)
URL = "https://transacciones.davivienda.com/dinamicos/ComercialServlet?item=fondos&canal=inter&consulta=dafuturo"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    html = page.content()
    browser.close()
soup = BeautifulSoup(html, "html.parser")
tabla = soup.find_all("table")[0]
filas = tabla.find_all("tr")
filahoy = filas[5]
filahoy = [c.get_text(" ", strip=True) for c in filahoy.find_all(["td", "th"])]
filahoy = filahoy[1]
hoy = datetime.strptime(filahoy, "%d/%m/%y").date()
print(hoy)
if (df["Fecha"] == str(hoy)).any():
    print("Ya existe un registro para hoy.")
else:
    fila1={"Fecha": str(hoy)}
    for fila in filas:
        columnas = [c.get_text(" ", strip=True) for c in fila.find_all(["td", "th"])]
        if len(columnas) >= 5:
            fondo = columnas[0]
            if fondo in fondos:
                valor_unidad = columnas[3]
                valor=valor_unidad.replace("$", "").replace(",", "")
                if valor.startswith("."):
                    valor = "0" + valor
                valor=float(valor)
                fila1[fondo] = valor
    for fondo in fondos:
        if fondo not in fila1:
            fila1[fondo] = None
    df = pd.concat([df, pd.DataFrame([fila1])], ignore_index=True)
    df.to_csv(archivo, index=False)
