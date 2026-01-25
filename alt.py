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

pfad = "data\\Offen_und_Besetzt.csv" ##Offene_Stellen_2023_in_Prozent
daten= pd.read_csv(pfad, sep=";",header=[0,1]) #(pfad, sep=";",header=[0,1],index_col=[2,0])

#O_Helfer = daten["Offene Stellen mit Anforderungsniveau Helfer"]
O_Fachkraft = daten["Offene Stellen mit Anforderungsniveau Fachkraft"]
O_Spezialist = daten["Offene Stellen mit Anforderungsniveau Spezialist"]
#O_Experte = daten["Offene Stellen mit Anforderungsniveau Experte"]

#B_Helfer = daten["Beschäftigte mit Anforderungsniveau Helfer"]
B_Fachkraft = daten["Beschäftigte mit Anforderungsniveau Fachkraft"]
B_Spezialist = daten["Beschäftigte mit Anforderungsniveau Spezialist"]
#B_Experte = daten["Beschäftigte mit Anforderungsniveau Experte"]

#O_Helfer_2023 =O_Helfer["2023"] 
Raumeinheit = daten["Raumeinheit"]

top_10 = O_Fachkraft.sort_values(by="2023", ascending=False).head(10)

#O_Spezialist_2023 = daten[daten["Offene Stellen mit Anforderungsniveau Spezialist"] == "2023"]






# Daten für das Balkendiagramm
labels= set()
labels =daten["Raumeinheit"]
werte = set()
werte = O_Fachkraft["2023"] #daten[("Offene Stellen mit Anforderungsniveau Spezialist","2023")]
farben = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Balkendiagramm erstellen
plt.figure(figsize=(8, 5))  # Größe des Diagramms
plt.bar(labels, werte, color=farben)

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Beispiel-Balkendiagramm')
plt.xlabel('Kategorien')
plt.ylabel('Werte')

# Diagramm anzeigen
plt.savefig('balkendiagramm.png')  # Optional: Speichern des Diagramms
plt.show()
