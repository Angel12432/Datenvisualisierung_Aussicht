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
pfad= "Daten\\Datensimulation_Arbeits_Qualifikationen.csv"
daten= pd.read_csv(pfad, sep=";",header=[0,1],index_col=[2,0])