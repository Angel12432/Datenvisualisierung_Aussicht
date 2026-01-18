# Installation der benötigten Pakete
#pip install setuptools
#pip install pandas requests tqdm pyarrow
#pip install plotnine
# Importiere benötigte Bibliotheken
from _operator import index
import pandas as pd
import numpy as np
from plotnine import *
from plotnine import ggsave
import matplotlib.pyplot as plt

pfad = "data\\Tabelle Arbeitlossigkeit_OffeneStellen.csv" ##Offene_Stellen_2023_in_Prozent
daten= pd.read_csv(pfad, sep=";",header=[0,1]) #(pfad, sep=";",header=[0,1],index_col=[2,0])
O_Helfer = daten["Offene Stellen mit Anforderungsniveau Helfer"]
O_Fachkraft = daten["Offene Stellen mit Anforderungsniveau Fachkraft"]
O_Experte = daten["Offene Stellen mit Anforderungsniveau Experte"]
O_Spezialist = daten["Offene Stellen mit Anforderungsniveau Spezialist"]
#O_Helfer_2023 =O_Helfer["2023"]
Raumeinheit = daten["Raumeinheit"]


# Daten für das Kreisdiagramm
labels = ['Kategorie A', 'Kategorie B', 'Kategorie C', 'Kategorie D']
sizes = [15, 30, 45, 10]  # Größen der Segmente
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']  # Farben
explode = (0, 0.5, 0, 0)  # Explodiertes Segment (Kategorie A)

# Kreisdiagramm erstellen
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Gleichmäßige Achsen für einen perfekten Kreis
plt.title('Beispiel-Kreisdiagramm')
plt.show()
