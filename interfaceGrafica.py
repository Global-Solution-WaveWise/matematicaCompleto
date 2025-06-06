import requests
import customtkinter as ckt
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

# --- API Config ---
apiKey = "926b7fe14b4b397ad4b80a4277257b97"
city = "Recife"
weatherApiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=pt_br"

try:
    weatherRequest = requests.get(weatherApiUrl)
    weatherRequest.raise_for_status()
    weatherData = weatherRequest.json()
    weatherDescription = weatherData['weather'][0]['description']
    temperatureKelvin = weatherData['main']['temp']
    temperatureCelsius = temperatureKelvin - 273.15
except requests.exceptions.RequestException as e:
    weatherDescription = "Erro ao carregar descrição"
    temperatureCelsius = 0.0
    print(f"Erro ao obter dados meteorológicos: {e}")

# --- River Level Sim ---
simDays = 10
initialRiverLvl = 1.0 # meters
maxRiverLvl = 3.0 # meters
minRiverLvl = 0.5 # meters
floodAlertLvl = 2.5 # meters

riverLvls = []
currentRiverLvl = initialRiverLvl
days = list(range(1, simDays + 1))

for day in days:
    rainIncrease = random.uniform(0.1, 0.4)
    currentRiverLvl += rainIncrease

    if currentRiverLvl > maxRiverLvl:
        currentRiverLvl = maxRiverLvl
    if currentRiverLvl < minRiverLvl:
        currentRiverLvl = minRiverLvl

    riverLvls.append(currentRiverLvl)

# --- Polynomial Model ---
daysNp = np.array(days)
riverLvlsNp = np.array(riverLvls)

polyDegree = 2
coefficients = np.polyfit(daysNp, riverLvlsNp, polyDegree)
polynomialLvls = np.polyval(coefficients, daysNp)

def formatPolynomialEquation(polyCoeffs):
    eqParts = []
    numCoeffs = len(polyCoeffs)

    for i, coeff in enumerate(polyCoeffs):
        power = numCoeffs - 1 - i
        if coeff == 0:
            continue
        termStr = f"{coeff:.2f}"

        if power > 1:
            termStr += f"x^{power}"
        elif power == 1:
            termStr += "x"

        if i > 0 and coeff > 0:
            eqParts.append(f" + {termStr}")
        elif i > 0 and coeff < 0:
            eqParts.append(f" {termStr}")
        else:
            eqParts.append(termStr)

    return "f(x) = " + "".join(eqParts).lstrip('+').strip() if eqParts else "N/A"

polynomialEquationString = formatPolynomialEquation(coefficients)

# --- CustomTkinter GUI ---
ckt.set_appearance_mode('light')

app = ckt.CTk()
app.title('Monitoramento do nível do rio & Clima')
app.geometry('800x750') # Adjusted window size for non-table layout
app.resizable(True, True)

# --- Weather Info Frame ---
weatherInfoFrame = ckt.CTkFrame(app)
weatherInfoFrame.pack(pady=20, padx=20, fill='x', expand=False)

labelCityTitle = ckt.CTkLabel(weatherInfoFrame, text=f"Cidade: {city}", font=ckt.CTkFont(size=20, weight="bold"))
labelCityTitle.pack(pady=5)

labelWeatherDescription = ckt.CTkLabel(weatherInfoFrame, text=f"Descrição: {weatherDescription}", font=ckt.CTkFont(size=16))
labelWeatherDescription.pack(pady=5)

labelTemperature = ckt.CTkLabel(weatherInfoFrame, text=f"{temperatureCelsius: .1f}°C", font=ckt.CTkFont(size=24, weight="bold"))
labelTemperature.pack(pady=5)

labelPolynomialFunction = ckt.CTkLabel(weatherInfoFrame, text=f"Função Polinomial: {polynomialEquationString}",
                                         font=ckt.CTkFont(size=14, weight="normal"), wraplength=700)
labelPolynomialFunction.pack(pady=5)

# --- Graph Frame ---
graphFrame = ckt.CTkFrame(app)
graphFrame.pack(pady=20, padx=20, fill='both', expand=True)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(days, riverLvls, marker='o', linestyle='-', color='blue', label='Nível Simulado do Rio')
ax.plot(days, polynomialLvls, linestyle='--', color='green',
        label=f'Aproximação Polinomial (Grau {polyDegree})')

ax.axhline(y=floodAlertLvl, color='red', linestyle='--', label=f'Alerta de Enchente ({floodAlertLvl:.1f}m)')

ax.set_title(f'Variação do Nível do Rio em {city} ao Longo de {simDays} Dias de Chuva', fontsize=14)
ax.set_xlabel('Dia', fontsize=12)
ax.set_ylabel('Nível do Rio (metros)', fontsize=12)
ax.set_xticks(days)
ax.tick_params(axis='y', labelsize=10)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=graphFrame)
canvasWidget = canvas.get_tk_widget()
canvasWidget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
canvas.draw()

def onWindowResize(event):
    fig.tight_layout()
    canvas.draw()

app.bind("<Configure>", onWindowResize)

app.mainloop()
